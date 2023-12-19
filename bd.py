from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class BD:
    def __init__(self):
        super(BD, self).__init__()
        self.create_tables()

    def create_tables(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("portal.db")
        if not db.open():
            return False

        query = QSqlQuery()

        # Таблица "ученики"
        query.exec("""CREATE TABLE IF NOT EXISTS ученики (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      имя TEXT,
                      фамилия TEXT,
                      логин TEXT,
                      пароль TEXT DEFAULT no)""")

        # Таблица "преподаватели"
        query.exec("""CREATE TABLE IF NOT EXISTS преподаватели (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      имя TEXT,
                      фамилия TEXT,
                      логин TEXT,
                      пароль TEXT DEFAULT no)""")

        # Таблица "успеваемость"
        query.exec("""CREATE TABLE IF NOT EXISTS успеваемость (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      id_ученика INTEGER,
                      id_преподавателя INTEGER,
                      предмет TEXT,
                      оценка INTEGER,
                      FOREIGN KEY (id_ученика) REFERENCES ученики(id),
                      FOREIGN KEY (id_преподавателя) REFERENCES преподаватели(id))""")

        return True
