import sqlite3
from constatnts import week_dict


# Класс, в котором происходит работа с db
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

    @staticmethod
    def save_link(table, lesson, link):
        con = sqlite3.connect('saves/links/links.sqlite3')
        cur = con.cursor()

        all_links = cur.execute(f"""SELECT lesson from {table}""").fetchall()
        all_links = list(map(lambda x: x[0], all_links))

        if lesson in all_links:
            cur.execute(f"""UPDATE {table}
SET link = ?
WHERE lesson = ?""", (link, lesson))
        else:
            cur.execute(f"""INSERT INTO {table} VALUES(?, ?)""", (lesson, link))

        con.commit()

    @staticmethod
    def get_links():
        con = sqlite3.connect('saves/links/links.sqlite3')
        cur = con.cursor()

        result1 = cur.execute("""SELECT * from books""").fetchall()
        result2 = cur.execute("""SELECT * from gdz""").fetchall()
        return result1, result2

    @staticmethod
    def get_lesson_links():
        con = sqlite3.connect('saves/links/links.sqlite3')
        cur = con.cursor()

        result1 = cur.execute("""SELECT lesson from books""").fetchall()
        result2 = cur.execute("""SELECT lesson from gdz""").fetchall()

        result1 = list(map(lambda x: 'Учебники-' + x[0], result1))
        result2 = list(map(lambda x: 'ГДЗ-' + x[0], result2))

        return result1 + result2

    @staticmethod
    def get_link(table, lesson):
        con = sqlite3.connect('saves/links/links.sqlite3')
        cur = con.cursor()
        result = cur.execute(f"""SELECT link from {table}
WHERE lesson = ?""", (lesson,)).fetchall()
        if result:
            result = result[0][0]
        return result

    @staticmethod
    def del_link(table, lesson):
        con = sqlite3.connect('saves/links/links.sqlite3')
        cur = con.cursor()

        cur.execute(f"""DELETE from {table}
WHERE lesson = ?""", (lesson,))
        con.commit()