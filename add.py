from PyQt5 import QtWidgets, QtGui, QtCore
from add_interface import Ui_Dialog
from dbwork import DBWork as Db


# Диалоговое окно, отвечающее за работу кнопки "Добавить" раздела ссылки
class Add(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Добавить ссылку')

        self.par = parent

        self.box_gdz_or_books.addItems(['Учебники и другие пособия', 'ГДЗ'])

        self.cancel_.clicked.connect(self.close)
        self.ok_.clicked.connect(self.ok)

    def ok(self):  # Функция для кнопки "ОК"
        if not self.input_link.text() or not self.input_lesson.text():
            self.close()
            return
        elif self.box_gdz_or_books.currentText() == 'Учебники и другие пособия':
            lesson = self.input_lesson.text()
            link = self.input_link.text()
            for_save = ['books', lesson, link]
        else:
            lesson = self.input_lesson.text()
            link = self.input_link.text()
            for_save = ['gdz', lesson, link]

        Db.save_link(*for_save)
        self.par.full_link_tables()
        self.close()
