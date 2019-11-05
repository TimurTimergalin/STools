from important_interface import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore
from dbwork import DBWork as Db


class Important(QtWidgets.QDialog, Ui_Form):
    def __init__(self, par=None):
        super().__init__(par)
        self.par = par
        self.setupUi(self)  # Временное решение
        self.connect_boxes()
        self.ok_.clicked.connect(self.ok)
        self.list_of_clicked = []

    def connect_boxes(self):  # Ккрипт автоматизации будет вскоре написан
        self.checkBox.stateChanged.connect(self.add_to_list)
        self.checkBox_2.stateChanged.connect(self.add_to_list)
        self.checkBox_3.stateChanged.connect(self.add_to_list)
        self.checkBox_4.stateChanged.connect(self.add_to_list)
        self.checkBox_5.stateChanged.connect(self.add_to_list)
        self.checkBox_6.stateChanged.connect(self.add_to_list)
        self.checkBox_7.stateChanged.connect(self.add_to_list)
        self.checkBox_8.stateChanged.connect(self.add_to_list)
        self.checkBox_9.stateChanged.connect(self.add_to_list)
        self.checkBox_10.stateChanged.connect(self.add_to_list)
        self.checkBox_11.stateChanged.connect(self.add_to_list)
        self.checkBox_12.stateChanged.connect(self.add_to_list)
        self.checkBox_13.stateChanged.connect(self.add_to_list)
        self.checkBox_14.stateChanged.connect(self.add_to_list)
        self.checkBox_15.stateChanged.connect(self.add_to_list)
        self.checkBox_16.stateChanged.connect(self.add_to_list)
        self.checkBox_17.stateChanged.connect(self.add_to_list)
        self.checkBox_18.stateChanged.connect(self.add_to_list)
        self.checkBox_19.stateChanged.connect(self.add_to_list)
        self.checkBox_20.stateChanged.connect(self.add_to_list)
        self.checkBox_21.stateChanged.connect(self.add_to_list)
        self.checkBox_22.stateChanged.connect(self.add_to_list)
        self.checkBox_23.stateChanged.connect(self.add_to_list)
        self.checkBox_24.stateChanged.connect(self.add_to_list)
        self.checkBox_25.stateChanged.connect(self.add_to_list)
        self.checkBox_26.stateChanged.connect(self.add_to_list)
        self.checkBox_27.stateChanged.connect(self.add_to_list)
        self.checkBox_28.stateChanged.connect(self.add_to_list)
        self.checkBox_29.stateChanged.connect(self.add_to_list)
        self.checkBox_30.stateChanged.connect(self.add_to_list)
        self.checkBox_31.stateChanged.connect(self.add_to_list)
        self.checkBox_32.stateChanged.connect(self.add_to_list)
        self.checkBox_33.stateChanged.connect(self.add_to_list)
        self.checkBox_34.stateChanged.connect(self.add_to_list)
        self.checkBox_35.stateChanged.connect(self.add_to_list)
        self.checkBox_36.stateChanged.connect(self.add_to_list)
        self.checkBox_37.stateChanged.connect(self.add_to_list)

    def add_to_list(self, state):
        if state == QtCore.Qt.Checked:
            self.list_of_clicked.append(self.sender().text())
        else:
            self.list_of_clicked.remove(self.sender().text())

    def ok(self):
        Db.save_important(self.list_of_clicked)
        if self.par.change_clicked:
            self.par.change_to_text()
            self.par.change_clicked = False
        else:
            self.par.full_tables()
        self.close()