import sqlite3

class Client:
  """Создает класс c клиентами."""
  def __init__(self, surname, name, patronymic, id, entrance, num_days,level_room,room_number,points):
    self.surname = surname
    self.name = name
    self.patronymic = patronymic
    self.id = id
    self.entrance = entrance
    self.num_days = num_days
    self.level_room = level_room
    self.room_number = room_number
    self.points = points
  



clients_list=[]

conn = sqlite3.connect('client3.db')
cursor = conn.cursor()
# Создание таблицы для хранения информации о клиентах
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        surname TEXT,
        name TEXT,
        patronymic TEXT,
        passport_id INTEGER,
        entrance_date TEXT,
        num_days INTEGER,
        level_room INTEGER,
        room_number INTEGER,
        points INTEGER
    )
''')
conn.commit()



def add_client_to_db(client):
    cursor.execute('''
        INSERT INTO clients (surname, name, patronymic, passport_id, entrance_date, num_days, level_room, room_number, points)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (client.surname, client.name, client.patronymic, client.id, client.entrance, client.num_days, client.level_room, client.room_number, client.points))
    conn.commit()

def show_points(surname):
    """Получает количество баллов клиента по его фамилии."""
    cursor.execute('SELECT points FROM clients WHERE surname = ?', (surname,))
    result = cursor.fetchone()
    
    if result:
        print(f'Ваши баллы: {result[0]}')
    else:
        print(f'No client found with surname: {surname}')

"""
new_client1 = Client('Прунцова', 'Алиса', 'Сергеевна', 4444, '20.02.2024', 2, 2, 29, 200)
add_client_to_db(new_client1)

new_client2 = Client('Синицын', 'Михаил', 'Сергеевич', 3333, '20.02.2024', 3, 2, 12, 300)
add_client_to_db(new_client2)

new_client3 = Client('Жабраилов', 'Амирхан', 'Русланович', 2222, '20.02.2024', 2, 3, 45, 400)
add_client_to_db(new_client3)

new_client4 = Client('Шишанова', 'Анастасия', 'Вячеславовна', 1111, '20.02.2024', 1, 1, 50, 500)
add_client_to_db(new_client4) """