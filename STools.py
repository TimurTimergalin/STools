from interface1 import Ui_MainWindow
from PyQt5 import QtWidgets as Wid
from PyQt5 import QtGui as Gui
from PyQt5 import QtCore as Core
from PyQt5 import QtSql as Sql
import sys
from constatnts import _translate, all_lessons, week_day, NUMBER_OF_LESSONS
import sqlite3
from dbwork import DBWork as Db
import datetime
from important import Important


class STools(Wid.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('STools')
        self.mid()
        self.timetable()

    def mid(self):
        self.marks = []
        self._5.clicked.connect(self.mark_clicked)
        self._4.clicked.connect(self.mark_clicked)
        self._3.clicked.connect(self.mark_clicked)
        self._2.clicked.connect(self.mark_clicked)
        self._1.clicked.connect(self.mark_clicked)
        self.clear_.clicked.connect(self.clear_mid)
        self.delete_.clicked.connect(self.delete_mid)
        self.save_.clicked.connect(self.save_mid)
        self.import_.clicked.connect(self.import_mid)

    def timetable(self):
        self.tables = [self.t_monday, self.t_tuesday, self.t_wednesday, self.t_thursday, self.t_friday, self.t_saturday]
        tomorrow = week_day[(datetime.datetime.today().weekday() + 1) % 7]
        self.label.setText(_translate("MainWindow",
                                      f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Завтра {tomorrow}</span></p></body></html>"))
        self.full_tables()
        self.change_clicked = False
        self.change_.clicked.connect(self.change_timetable)
        self.important_.clicked.connect(self.important_clicked)

    def mark_clicked(self):
        mark = self.sender().text()
        self.marks.append(int(mark))
        mid_mark = '%.2f' % (sum(self.marks) / len(self.marks))
        new_list = self.list.text() + f'{mark} '
        self.middle.setText(_translate("MainWindow",
                                       f"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">{mid_mark}</span></p></body></html>"))
        self.list.setText(new_list)

    def clear_mid(self):
        self.marks.clear()
        self.list.setText('')
        self.middle.setText(_translate("MainWindow",
                                       "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">0.0</span></p></body></html>"))

    def delete_mid(self):
        if not self.marks:
            return
        self.marks.pop()
        if not self.marks:
            self.clear_mid()  # Стирание единсвенной оценки эквивалентно полной очистке
        else:
            mid_mark = '%.2f' % (sum(self.marks) / len(self.marks))
            new_list = ' '.join(self.list.text().split()[:-1])
            self.middle.setText(_translate("MainWindow",
                                           f"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">{mid_mark}</span></p></body></html>"))
            self.list.setText(new_list)

    def save_mid(self):
        all_lessons1 = all_lessons[:-1]
        lesson_name, i = Wid.QInputDialog.getItem(self, 'Сохранить балл', 'Выберите прдемет', all_lessons1, 37, False)
        if i and lesson_name:
            new_text = ''.join(list(map(lambda x: str(x), self.marks)))
            Db.save_middle(lesson_name, new_text)

    def import_mid(self):
        result = Db.get_middle()

        if result:
            result = list(map(lambda x: x[0], result))
            lesson_name, i = Wid.QInputDialog.getItem(self, 'Импортировать балл', 'Выберите предмет', result, 37, False)
            if i and lesson_name:
                self.marks = Db.import_middle(lesson_name)
                mid_mark = '%.2f' % (sum(self.marks) / len(self.marks))
                new_text = ' '.join(list(map(lambda x: str(x), self.marks)))
                self.middle.setText(_translate("MainWindow",
                                               f"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">{mid_mark}</span></p></body></html>"))
                self.list.setText(new_text)

    def full_tables(self):
        def item(day, lesson):
            values = Db.get_timetable()
            item_ = Wid.QTableWidgetItem(values[day][lesson])
            item_.setFlags(Core.Qt.ItemIsSelectable | Core.Qt.ItemIsEnabled)
            if item_.text() in Db.get_important():
                item_.setBackground(Gui.QColor(255, 255, 0))
            return item_
        for i in range(NUMBER_OF_LESSONS):
            for j in range(len(self.tables)):
                self.tables[j].setItem(i, 0, item(j, i))
                self.tables[j].setCellWidget(i, 0, None)
                self.tables[j].horizontalHeader().setSectionResizeMode(0, Wid.QHeaderView.Stretch)

    def change_to_combos(self):
        def combo(day, lesson):
            combo_ = Wid.QComboBox()
            combo_.addItems(all_lessons)

            values = Db.get_timetable()
            combo_.setCurrentText(values[day][lesson])
            return combo_

        for i in range(NUMBER_OF_LESSONS):
            for j in range(len(self.tables)):
                self.tables[j].setCellWidget(i, 0, combo(j, i))

    def change_to_text(self):
        def text(day, lesson):
            value = self.tables[day].cellWidget(lesson, 0).currentText()
            return value

        for i in range(NUMBER_OF_LESSONS):
            for j in range(len(self.tables)):
                cur_lesson = text(j, i)
                cur_item = Wid.QTableWidgetItem(cur_lesson)
                if cur_lesson in Db.get_important():
                    cur_item.setBackground(Gui.QColor(255, 255, 0))
                cur_item.setFlags(Core.Qt.ItemIsSelectable | Core.Qt.ItemIsEnabled)
                Db.save_timetable(j, i, cur_lesson)
                self.tables[j].setItem(i, 0, cur_item)
                self.tables[j].setCellWidget(i, 0, None)
                self.tables[j].horizontalHeader().setSectionResizeMode(0, Wid.QHeaderView.Stretch)

    def change_timetable(self):
        self.change_clicked = not self.change_clicked

        if self.change_clicked:
            self.change_to_combos()
        else:
            self.change_to_text()

    def important_clicked(self):
        dialog = Important(self)
        dialog.show()