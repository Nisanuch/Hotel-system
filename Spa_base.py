import sqlite3

class Spa:
    """Создает класс c клиентами спа."""
    
    def __init__(self, surname, day, month, time, quantity):
        self.surname = surname
        self.day = day
        self.month = month
        self.time = time
        self.quantity = quantity

    def __str__(self):
        """Вывод списка клиентов спа."""
        n_day = str(self.day).zfill(2)
        n_month = str(self.month).zfill(2)
        return f'Фамилия: {self.surname}, Дата: {n_day}.{n_month}, Время: {self.time} , Количество процедур: {self.quantity}'

    def save_spa_to_db(self):
        conn = sqlite3.connect('spa.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO spa_clients (surname, day, month, time, quantity)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.surname, self.day, self.month, self.time, self.quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_spa_client(surname):
        # Удаляет клиента
        conn = sqlite3.connect('spa.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM spa_clients WHERE surname=?', (surname,))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            print(f"Запись о клиенте {surname} удалена.")
        else:
            print(f"Клиент с фамилией {surname} не найден.")

    @staticmethod
    def find_spa_client(surname):
        # Ищет клиента
        conn = sqlite3.connect('spa.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM spa_clients WHERE surname=?', (surname,))
        result = cursor.fetchone()
        conn.close()

        if result:
            # Создаем объект Spa из результата запроса
            return Spa(*result[1:])
        else:
            return 'Клиент не найден'


def get_spa_clients():
    conn = sqlite3.connect('spa.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM spa_clients')
    rows = cursor.fetchall()
    conn.close()
    return rows


# Создание таблицы в базе данных, если она не существует
conn = sqlite3.connect('spa.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS spa_clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT,
        day INTEGER,
        month INTEGER,
        time INTEGER,
        quantity INTEGER
    )
''')
conn.commit()
conn.close()

'''# Пример использования класса
spaclient1 = Spa('Прунцова', 15, 3, 10, 2)
spaclient2 = Spa('Жабраилов', 10, 3, 12, 1)
spaclient3 = Spa('Шишанова', 15, 3, 9, 3)

# Сохранение клиентов в БД
spaclient1.save_spa_to_db()
spaclient2.save_spa_to_db()
spaclient3.save_spa_to_db()'''


