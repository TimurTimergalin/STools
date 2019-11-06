# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc/add.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.box_gdz_or_books = QtWidgets.QComboBox(Dialog)
        self.box_gdz_or_books.setGeometry(QtCore.QRect(68, 50, 281, 22))
        self.box_gdz_or_books.setObjectName("box_gdz_or_books")
        self.input_link = QtWidgets.QLineEdit(Dialog)
        self.input_link.setGeometry(QtCore.QRect(68, 140, 281, 41))
        self.input_link.setObjectName("input_link")
        self.ok_ = QtWidgets.QPushButton(Dialog)
        self.ok_.setGeometry(QtCore.QRect(120, 260, 75, 23))
        self.ok_.setObjectName("ok_")
        self.cancel_ = QtWidgets.QPushButton(Dialog)
        self.cancel_.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.cancel_.setObjectName("cancel_")
        self.input_lesson = QtWidgets.QLineEdit(Dialog)
        self.input_lesson.setGeometry(QtCore.QRect(68, 90, 281, 41))
        self.input_lesson.setObjectName("input_link_2")
        self.input_lesson.setToolTip('Введите название предмета')
        self.input_link.setToolTip('Введите ссылку')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_.setText(_translate("Dialog", "OK"))
        self.cancel_.setText(_translate("Dialog", "Cancel"))
