# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(894, 669)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_add_gas = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_add_gas.setObjectName("lineEdit_add_gas")
        self.gridLayout.addWidget(self.lineEdit_add_gas, 0, 1, 1, 1)
        self.add_gas = QtWidgets.QPushButton(self.widget)
        self.add_gas.setObjectName("add_gas")
        self.gridLayout.addWidget(self.add_gas, 0, 0, 1, 1)
        self.lineEdit_add_without_gas = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_add_without_gas.setObjectName("lineEdit_add_without_gas")
        self.gridLayout.addWidget(self.lineEdit_add_without_gas, 1, 1, 1, 1)
        self.add_without_gas = QtWidgets.QPushButton(self.widget)
        self.add_without_gas.setObjectName("add_without_gas")
        self.gridLayout.addWidget(self.add_without_gas, 1, 0, 1, 1)
        self.draw_two_measuring = QtWidgets.QPushButton(self.widget)
        self.draw_two_measuring.setObjectName("draw_two_measuring")
        self.gridLayout.addWidget(self.draw_two_measuring, 2, 0, 1, 2)
        self.draw_difference = QtWidgets.QPushButton(self.widget)
        self.draw_difference.setObjectName("draw_difference")
        self.gridLayout.addWidget(self.draw_difference, 3, 0, 1, 2)
        self.verticalLayout.addWidget(self.widget)
        self.label_plot_1 = QtWidgets.QLabel(Dialog)
        self.label_plot_1.setObjectName("label_plot_1")
        self.verticalLayout.addWidget(self.label_plot_1, 0, QtCore.Qt.AlignHCenter)
        self.widget_plot_1 = QtWidgets.QWidget(Dialog)
        self.widget_plot_1.setObjectName("widget_plot_1")
        self.layout_plot_1 = QtWidgets.QVBoxLayout(self.widget_plot_1)
        self.layout_plot_1.setObjectName("layout_plot_1")
        self.verticalLayout.addWidget(self.widget_plot_1)
        self.label_plot_2 = QtWidgets.QLabel(Dialog)
        self.label_plot_2.setObjectName("label_plot_2")
        self.verticalLayout.addWidget(self.label_plot_2, 0, QtCore.Qt.AlignHCenter)
        self.widget_plot_2 = QtWidgets.QWidget(Dialog)
        self.widget_plot_2.setObjectName("widget_plot_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_plot_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.widget_plot_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(4, 6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_gas.setText(_translate("Dialog", "Add file with gas"))
        self.add_without_gas.setText(_translate("Dialog", "Add file without gas"))
        self.draw_two_measuring.setText(_translate("Dialog", "Draw graphs of two measuring"))
        self.draw_difference.setText(_translate("Dialog", "Draw graph of difference between two graph"))
        self.label_plot_1.setText(_translate("Dialog", "Two graphs of two measuring"))
        self.label_plot_2.setText(_translate("Dialog", "Difference between graphs"))
