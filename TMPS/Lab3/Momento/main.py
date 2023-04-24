import sqlite3


class Originator:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.current_state = None
        self.cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

    def create_memento(self):
        return Memento(self.current_state)

    def restore(self, memento):
        self.current_state = memento.get_saved_state()

    def save(self, id, name, age):
        self.cursor.execute("INSERT INTO employees VALUES (?, ?, ?)", (id, name, age))
        self.connection.commit()
        self.current_state = (id, name, age)

    def get_state(self):
        return self.current_state

    def load_data(self):
        self.cursor.execute("SELECT * FROM employees ORDER BY id DESC LIMIT 1")
        result = self.cursor.fetchone()
        if result:
            self.current_state = result


class Memento:
    def __init__(self, state):
        self.saved_state = state

    def get_saved_state(self):
        return self.saved_state


class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self.mementos:
            print(memento.get_saved_state())

# Пример использования

db_name = "employees.db"
originator = Originator(db_name)
caretaker = Caretaker()

originator.save(1, "Иван Иванов", 25)
originator.load_data()
caretaker.add_memento(originator.create_memento())

originator.save(2, "Петр Петров", 30)
originator.load_data()
caretaker.add_memento(originator.create_memento())

originator.save(3, "Анна Сидорова", 35)
originator.load_data()
caretaker.add_memento(originator.create_memento())

# Восстанавливаем предыдущее состояние
originator.restore(caretaker.get_memento(1))
print("Текущее состояние после восстановления: ", originator.get_state())
caretaker.show_history()
