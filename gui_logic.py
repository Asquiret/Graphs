import matplotlib
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from gui import Ui_Dialog
from drawer import Drawer as drawer
from tkinter import filedialog

matplotlib.use('TkAgg')


class GuiProgram(Ui_Dialog):
    """ Класс контроллер - интерпретирует действия пользователя """

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        """ Вызывается при создании нового объекта класса """
        # Создание окна
        Ui_Dialog.__init__(self)
        # Установка пользовательского интерфейс
        self.setupUi(dialog)

        # Поля класса
        # Параметры 1 графика
        self.drawer_1 = drawer(
            layout=self.layout_plot_1,
            widget=self.widget_plot_1
        )
        # Параметры 2 графика
        self.drawer_2 = drawer(
            layout=self.verticalLayout_2,
            widget=self.widget_plot_2
        )
        # Обработка нажатий клавиш
        self.add_gas.clicked.connect(self.gas_data)
        self.add_without_gas.clicked.connect(self.without_gas_data)
        self.draw_two_measuring.clicked.connect(self.draw_measure)
        self.draw_difference.clicked.connect(self.draw_difference_graph)
        self.pushButton_threshold.clicked.connect(self.threshold)
        self.absorbations.clicked.connect(self.show_parts)
        self.array1 = []
        self.array2 = []

    def gas_data(self):
        self.gas_file, _ = QFileDialog.getOpenFileName()  # Открываем диалоговое окно выбора файла
        self.lineEdit_add_gas.setText(self.gas_file)
        # return self.gas_file  # Возвращаем значение переменной

    def without_gas_data(self):
        self.without_gas_file, _ = QFileDialog.getOpenFileName()  # Открываем диалоговое окно выбора файла
        self.lineEdit_add_without_gas.setText(self.without_gas_file)
        # return self.without_gas_file  # Возвращаем значение переменной

    def draw_measure(self):
        self.open_file(self.lineEdit_add_gas.text())
        self.frequency_data = self.array_x
        self.gamma_with_gas_data = self.array_y
        self.open_file(self.lineEdit_add_without_gas.text())
        self.gamma_without_gas_data = self.array_y
        self.frequency_data = self.array_x
        self.drawer_1.draw_two_line_xyy(self.frequency_data, self.gamma_with_gas_data, self.gamma_without_gas_data)

    def open_file(self, file):
        # Открываем файл с данными для первого графика
        fle = open(file, "r")
        # читаем строку файла
        fle.readline()
        lne = fle.readline()  # Записываем данные из строки в переменную
        # Создаём пустой массив для дальнейшей работы с ним
        self.array_x = []
        self.array_y = []
        # Цикл работает пока не встретит "звёздочки"
        while lne[0] != '*':
            val = lne.split()
            self.array_x.append(float(val[1]))
            self.array_y.append(float(val[4]))
            lne = fle.readline()
        fle.close()  # Закрываем файл
        return self.array_x, self.array_y

    def draw_difference_graph(self):

        gamma_with_gas = np.array(self.gamma_with_gas_data)
        gamma_without_gas = np.array(self.gamma_without_gas_data)
        self.difference_gamma = np.array(abs(gamma_with_gas - gamma_without_gas))

        # self.c = []
        # for i in range(len(self.gamma_with_gas_data)):
        #     self.c.append(abs(self.gamma_with_gas_data[i] - self.gamma_without_gas_data[i]))
        self.drawer_2.draw_one_line_xy(self.frequency_data, self.difference_gamma)
        return self.difference_gamma

    def threshold(self):
        percent_threshold = float(self.lineEdit_threshold.text())
        self.value_threshold = np.max(self.difference_gamma) * (percent_threshold / 100)
        self.drawer_2.draw_xy_and_line(self.frequency_data, self.difference_gamma, self.value_threshold)

    def show_parts(self):
        """ Функция нахождения начальных точек участков выше порога и создания массива со всеми значениями выше
        порога"""

        self.bigmassive = []
        # Создаём словарь состоящий из значений частоты и значений разности гаммы как координат x и y соответственно
        self.indexes = dict(zip(self.frequency_data, self.difference_gamma))

        for key, val in self.indexes.items():
            # Если значение выше порога, а предыдущее меньше, то выполняется функция
            if (val >= self.value_threshold) and (self.befor_value < self.value_threshold):
                position = list(self.indexes).index(key)  # Индекс точки начала участка выше порога
                self.make_massive(position) # Вызов функции создающий массив точек одного участка
                self.bigmassive.append(self.mass) # Добавление одного участка в массив всех участков
            self.befor_value = val
        print(self.bigmassive)


    def make_massive(self, position):
        """Функция для создания массива значений выше порога одного участка"""
        list_keys = list(self.indexes.keys())
        list_meanings = list(self.indexes.values())
        new_keys = list_keys[position:]
        new_meanings = list_meanings[position:]

        # Создание нового обрезанного словаря
        new_indexes = dict(zip(new_keys, new_meanings))

        self.smol_gamma = []
        self.mass = []
        # Ключи словаря записываются пока Value больше порога
        for key, val in new_indexes.items():
            if val >= self.value_threshold:
                self.mass.append(key)
                self.smol_gamma.append(val)
            else:
                break
        self.max_part_point(self.mass, self.smol_gamma)

    def max_part_point(self, mass, smol_gamma):
        smol_massive = dict(zip(mass, smol_gamma))
        max_gamma = max(smol_massive.values())

        for key, val in smol_massive.items():
            if val==max_gamma:
                print(key)
                break