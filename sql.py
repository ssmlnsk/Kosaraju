import sqlite3


class DBFile:
    """
    Класс с функциями для взаимодействия с базой данных
    """
    def __init__(self, filename):
        """
        Создание базы данных
        :param filename: название базы данных
        """
        self.con = sqlite3.connect('data/' + filename + '.db')

    def save_db(self, edges):
        """
        Функция сохранения данных в базу данных
        :param edges: рёбра графа
        :return: None
        """
        cur = self.con.cursor()
        cur.execute("DROP TABLE IF EXISTS tbl")
        cur.execute("""CREATE TABLE tbl(
            id INTEGER PRIMARY KEY,
            n1 INT,
            n2 INT);
        """)
        self.con.commit()
        cur.executemany("INSERT INTO tbl(n1,n2) VALUES(?,?);", edges)
        self.con.commit()
        self.con.close()

    def load_db(self):
        """
        Функция загрузки данных из базы данных в приложение
        :return: results
        """
        cur = self.con.cursor()
        cur.execute("SELECT n1,n2 FROM tbl")
        results = cur.fetchall()
        return results
