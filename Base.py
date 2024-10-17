import sqlite3
from Clients_base import *


conn = sqlite3.connect('client1.db')
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



