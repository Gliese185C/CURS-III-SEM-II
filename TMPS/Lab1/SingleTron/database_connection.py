import sqlite3

class Database:
    __instance = None

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Нельзя создавать более одного экземпляра класса Database")
        else:
            Database.__instance = self

        # Создаем соединение с базой данных
        self.connection = sqlite3.connect('example.db')
        self.cursor = self.connection.cursor()

        # Создаем таблицу, если она еще не существует
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS example_table
                            (id INTEGER PRIMARY KEY, name TEXT)''')

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def insert_data(self, name):
        # Вставляем данные в таблицу базы данных
        self.cursor.execute("INSERT INTO example_table (name) VALUES (?)", (name,))
        self.connection.commit()
        print(f"Данные '{name}' успешно добавлены в базу данных.")

    def select_data(self):
        # Получаем все данные из таблицы базы данных
        self.cursor.execute("SELECT * FROM example_table")
        data = self.cursor.fetchall()
        print("Данные в базе данных:")
        for row in data:
            print(row)


