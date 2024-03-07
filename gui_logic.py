import matplotlib
from PyQt5 import QtWidgets
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
        self.array1 = []
        self.array2 = []

    def gas_data(self):
        self.gas_file = filedialog.askopenfilename()  # Открываем диалоговое окно выбора файла
        self.lineEdit_add_gas.setText(self.gas_file)  # Записываем полученный путь к файлу в LineEdit
        self.gas_file = self.lineEdit_add_gas.text()  # Обновляем переменную на случай если вручную ввёл путь к файлу
        return self.gas_file  # Возвращаем значение переменной

    def without_gas_data(self):
        self.without_gas_file = filedialog.askopenfilename()  # Открываем диалоговое окно выбора файла
        self.lineEdit_add_without_gas.setText(self.without_gas_file)  # Записываем полученный путь к файлу в LineEdit
        self.without_gas_file = self.lineEdit_add_without_gas.text()  # Обновляем переменную на случай если вручную ввёл путь к файлу
        return self.without_gas_file  # Возвращаем значение переменной

    def draw_measure(self):
        # Открываем файл с данными для первого графика
        fle = open(self.gas_file, "r")
        # читаем строку файла
        fle.readline()
        lne = fle.readline()  # Записываем данные из строки в переменную
        # Создаём пустой массив для дальнейшей работы с ним
        self.array1 = []
        # Цикл работает пока не встретит "звёздочки"
        while lne[0] != '*':
            val = lne.split()
            self.array1.append(float(val[4]))
            lne = fle.readline()
        fle.close()  # Закрываем файл
        self.list_1 = self.array1  # Записываем данные массива в переменную

        # Открываем файл с данными для второго графика
        self.file = open(self.without_gas_file, "r")
        self.file.readline()  # читаем строку файла
        self.line = self.file.readline()  # Записываем данные из строки в переменную
        # Создаём пустой массив для дальнейшей работы с ним
        self.array2 = []
        while self.line[0] != '*':
            val = self.line.split()  # Делим строку по пробелам
            self.array2.append(float(val[4]))  # Добавляем в массив четвёртый член из всех членов строки
            self.line = self.file.readline()
        self.file.close()  # Закрываем файл
        self.list_2 = self.array2  # Записываем данные массива в переменную
        self.drawer_1.draw_two_line(self.list_1, self.list_2)  # Строим два графика по полученным данным

    def draw_difference_graph(self):
        c = []
        for i in range(len(self.list_1)):
            c.append(self.list_1[i] - self.list_2[i])
        self.drawer_2.draw_line(c)
