from PyQt5 import QtWidgets, QtGui, QtCore
from dbwork import DBWork as Db
from constatnts import all_lessons


# Диалоговое окно, отвечающее за работу кнопки "Важные" в пазделе "расписание"
class Important(QtWidgets.QDialog):
    def __init__(self, par=None):
        super().__init__(par)
        self.par = par
        self.setGeometry(200, 200, 900, 375)
        self.setWindowTitle('Важные')
        self.connect_boxes()
        self.make_button()
        self.list_of_clicked = []

    def connect_boxes(self):  # Создание интерфейса
        lessons = all_lessons[:-1]
        for i in range(len(lessons)):
            box = QtWidgets.QCheckBox(self)
            width = 125
            height = 25
            space = 25
            x = space * (i % 6 + 1) + width * (i % 6)
            y = space * (i // 6 + 1) + height * (i // 6)
            box.setGeometry(x, y, width, height)
            box.setText(lessons[i])
            box.stateChanged.connect(self.add_to_list)

    def make_button(self):  # Добавление кнопки "ОК"
        self.ok_ = QtWidgets.QPushButton(self)
        self.ok_.setText('OK')
        self.ok_.setGeometry(475, 325, 125, 50)
        self.ok_.clicked.connect(self.ok)

    def add_to_list(self, state):  # Функция для QCheckBox
        if state == QtCore.Qt.Checked:
            self.list_of_clicked.append(self.sender().text())
        else:
            self.list_of_clicked.remove(self.sender().text())

    def ok(self):  # Функция для кнопки "ОК"
        Db.save_important(self.list_of_clicked)
        if self.par.change_clicked:
            self.par.change_to_text()
            self.par.change_clicked = False
        else:
            self.par.full_tables()
        self.close()