import sqlite3

class Restaurant:
    """Создает класс с клиентами ресторана."""
    
    def __init__(self, surname, day, month, time, quantity):
        self.surname = surname
        self.day = day
        self.month = month
        self.time = time
        self.quantity = quantity

    def __str__(self):
        """Вывод информации о клиенте."""
        n_day = str(self.day).zfill(2)
        n_month = str(self.month).zfill(2)
        return f'Фамилия: {self.surname}, Дата: {n_day}.{n_month}, Время: {self.time}, Количество человек: {self.quantity}'

    def save_to_db(self):
        """Сохраняет информацию о клиенте в базу данных."""
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO restaurants (surname, day, month, time, quantity)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.surname, self.day, self.month, self.time, self.quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_client(surname):
        """Удаляет запись о клиенте по фамилии из базы данных."""
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM restaurants WHERE surname=?', (surname,))
        conn.commit()
        conn.close()
        if cursor.rowcount > 0:
            print(f"Запись о клиенте {surname} удалена.")
        else:
            print(f"Клиент с фамилией {surname} не найден.")

    @staticmethod
    def find_client(surname):
        """Ищет клиента по фамилии в базе данных."""
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM restaurants WHERE surname=?', (surname,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return Restaurant(*result[1:])
        else:
            return 'Клиент не найден'


def create_table():
    """Создает таблицу для хранения информации о клиентах."""
    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
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

def display_all_clients():
    """Отображает всех клиентов из базы данных."""
    with sqlite3.connect('restaurant.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM restaurants')
        results = cursor.fetchall()

        if results:
            for row in results:
                client = Restaurant(*row[1:])  # Игнорируем ID
                print(client)
        else:
            print("Нет записей в базе данных.")

# Создаем таблицу, если она не существует
create_table()

"""# Пример использования класса
restorant_client1 = Restaurant('Жабраилов', 22, 2, 19, 4)
restorant_client1.save_to_db()

restorant_client2 = Restaurant('Синицын', 1, 3, 22, 2)
restorant_client2.save_to_db()"""


