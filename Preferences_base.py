import sqlite3

class Preferences:
    def __init__(self, surname, pref):
        self.surname = surname
        self.prefs = [pref]  # Инициализируем список предпочтений

    def __str__(self):
        return f"Фамилия: {self.surname}, Предпочтения: {self.prefs}"

    def save_to_db(self):
        conn = sqlite3.connect('preferences.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO preferences (surname, preference)
            VALUES (?, ?)
        ''', (self.surname, self.prefs[0]))  # Сохраняем первое предпочтение
        conn.commit()
        conn.close()
        
    @staticmethod
    def remove_from_db(surname):
        conn = sqlite3.connect('preferences.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM preferences WHERE surname=?', (surname,))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            print(f"Запись о клиенте {surname} удалена.")
        else:
            print(f"Клиент с фамилией {surname} не найден.")

    @staticmethod
    def find_preferences_from_db(surname):
        conn = sqlite3.connect('preferences.db')
        cursor = conn.cursor()
        cursor.execute('SELECT preference FROM preferences WHERE surname=?', (surname,))
        results = cursor.fetchall()
        conn.close()

        if results:
            return [row[0] for row in results]
        else:
            return "Клиент не найден"


def create_preferences_table():
    conn = sqlite3.connect('preferences.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            surname TEXT,
            preference TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_preference(surname, pref):
    # Проверяем, существует ли клиент
    if Preferences.find_preferences_from_db(surname) != "Клиент не найден":
        conn = sqlite3.connect('preferences.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE preferences SET preference = ? WHERE surname = ?
        ''', (pref, surname))
        conn.commit()
        conn.close()
    else:
        new_client = Preferences(surname, pref)
        new_client.save_to_db()

def remove_preferences(surname):
    Preferences.remove_from_db(surname)

def find_preferences(surname):
    preferences = Preferences.find_preferences_from_db(surname)
    return preferences

def display_all_preferences():
    conn = sqlite3.connect('preferences.db')
    cursor = conn.cursor()
    cursor.execute('SELECT surname, preference FROM preferences')
    results = cursor.fetchall()
    conn.close()

    if results:
        for row in results:
            print(f"Фамилия: {row[0]}, Предпочтение: {row[1]}")
    else:
        print("Нет записей в базе данных.")




# Создание таблицы в базе данных
create_preferences_table()

'''# Примеры добавления предпочтений
add_preference('Жабраилов', 'Положить на стул мягкие подушки')
add_preference('Синицын', 'Поставить в номер лампу для записывания видеороликов')
add_preference('Жабраилов', 'Тихая музыка')  # Обновление предпочтения

# Поиск предпочтений клиента
print(find_preferences('Жабраилов'))
print(find_preferences('Синицын'))

# Удаление предпочтений клиента
remove_preferences('Синицын')'''
