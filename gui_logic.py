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
        return self.gas_file  # Возвращаем значение переменной

    def without_gas_data(self):
        self.without_gas_file = filedialog.askopenfilename()  # Открываем диалоговое окно выбора файла
        return self.without_gas_file  # Возвращаем значение переменной

    def draw_measure(self):
        self.open_file(self.gas_file)
        frequency_data = self.array_x
        gamma_with_gas_data = self.array_y
        self.open_file(self.without_gas_file)
        gamma_without_gas_data = self.array_y
        self.drawer_1.draw_two_line_xyy(frequency_data, gamma_with_gas_data, gamma_without_gas_data)


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
        c = []
        for i in range(len(self.list_1)):
            c.append(self.list_1[i] - self.list_2[i])
        self.drawer_2.draw_line(c)
