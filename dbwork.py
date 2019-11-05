import sqlite3
from constatnts import week_dict


class DBWork:
    @staticmethod
    def save_middle(lesson, marks):
        con = sqlite3.connect('saves/middle/Middle.sqlite3')
        cur = con.cursor()

        lessons = cur.execute("""SELECT lesson FROM lessons""").fetchall()
        lessons = list(map(lambda x: x[0], lessons))
        if lesson in lessons:
            cur.execute(f"""Update lessons
            SET marks = ?
            WHERE lesson = ?""", (marks, lesson))
        else:
            cur.execute(f"""INSERT INTO lessons VALUES (?, ?)""", (lesson, marks))
        con.commit()

    @staticmethod
    def import_middle(lesson):
        con = sqlite3.connect('saves/middle/Middle.sqlite3')
        cur = con.cursor()

        marks = cur.execute("""SELECT marks FROM lessons
        WHERE lesson = ?""", (lesson,)).fetchall()
        marks = str(marks[0][0])
        marks = list(map(lambda x: int(x), list(marks)))
        return marks

    @staticmethod
    def get_middle():
        con = sqlite3.connect('saves/middle/Middle.sqlite3')
        cur = con.cursor()

        result = cur.execute("""SELECT lesson FROM lessons WHERE marks <> ''""").fetchall()
        return result

    @staticmethod
    def get_timetable():
        tables = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        values = []

        con = sqlite3.connect('saves/lessons/timetable.sqlite3')
        cur = con.cursor()
        for i in tables:
            result = cur.execute(f"""SELECT lesson FROM {i}""").fetchall()
            result = list(map(lambda x: x[0], result))
            values.append(result)
        return values

    @staticmethod
    def save_timetable(day, lesson_num, lesson):
        con = sqlite3.connect('saves/lessons/timetable.sqlite3')
        cur = con.cursor()

        cur.execute(f"""UPDATE {week_dict[day]}
SET lesson = ?
WHERE № = {lesson_num + 1}""", (lesson,))
        con.commit()

    @staticmethod
    def save_important(lst):
        con = sqlite3.connect('saves/lessons/important.sqlite3')
        cur = con.cursor()
        cur.execute("""DELETE FROM important""")
        for i in lst:
            cur.execute("""INSERT INTO important VALUES(?)""", (i,))
        con.commit()

    @staticmethod
    def get_important():
        con = sqlite3.connect('saves/lessons/important.sqlite3')
        cur = con.cursor()
        result = cur.execute("""SELECT lesson from important""").fetchall()
        return list(map(lambda x: x[0], result))
