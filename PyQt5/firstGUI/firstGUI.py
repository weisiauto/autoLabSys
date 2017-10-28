# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEditPriceBox = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPriceBox.setGeometry(QtCore.QRect(80, 120, 171, 41))
        self.textEditPriceBox.setObjectName("textEditPriceBox")
        self.labelPrice = QtWidgets.QLabel(self.centralwidget)
        self.labelPrice.setGeometry(QtCore.QRect(10, 140, 54, 12))
        self.labelPrice.setObjectName("labelPrice")
        self.spinBoxTaxRate = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxTaxRate.setGeometry(QtCore.QRect(80, 190, 171, 31))
        self.spinBoxTaxRate.setProperty("value", 20)
        self.spinBoxTaxRate.setObjectName("spinBoxTaxRate")
        self.labelTaxRate = QtWidgets.QLabel(self.centralwidget)
        self.labelTaxRate.setGeometry(QtCore.QRect(10, 200, 54, 12))
        self.labelTaxRate.setObjectName("labelTaxRate")
        self.pushButtonCalTax = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCalTax.setGeometry(QtCore.QRect(80, 280, 131, 31))
        self.pushButtonCalTax.setObjectName("pushButtonCalTax")
        self.textEditResult = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditResult.setGeometry(QtCore.QRect(80, 350, 171, 41))
        self.textEditResult.setObjectName("textEditResult")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPrice.setText(_translate("MainWindow", "Price"))
        self.labelTaxRate.setText(_translate("MainWindow", "Tax Rate"))
        self.pushButtonCalTax.setText(_translate("MainWindow", "Calculate Tax"))
        self.label.setText(_translate("MainWindow", "Sales Tax Calculator"))

