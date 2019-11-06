from PyQt5 import QtCore as Core
import sqlite3


def f_all_lessons():
    cur = sqlite3.connect('misc/all_lessons.sqlite3').cursor()
    result = cur.execute(f"""SELECT lesson from all_lessons""").fetchall()
    return list(map(lambda x: x[0], result))


all_lessons = f_all_lessons()
_translate = Core.QCoreApplication.translate

week_day = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

week_dict = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday'
}

NUMBER_OF_LESSONS = 7

to_en = {
    'ГДЗ': 'gdz',
    'Учебники': 'books'
}