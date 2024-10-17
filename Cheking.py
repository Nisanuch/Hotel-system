from Clients_base import *
from Staf_base import *
import sqlite3

def check_client(surname):
    with sqlite3.connect('client.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM clients WHERE surname=?', (surname,))
        count = cursor.fetchone()[0]
        
        return count > 0
    

def get_client_by_surname(surname, fields="name, patronymic"):
    """Получает имя и отчество клиента по фамилии и возвращает строку с полным именем."""
    with sqlite3.connect('client.db') as conn:
        cursor = conn.cursor()

        # Формируем запрос с динамическими полями
        query = f"SELECT {fields} FROM clients WHERE surname=?"
        cursor.execute(query, (surname,))

        result = cursor.fetchone()

        if result:
            name, patronymic = result
            # Проверяем, что оба поля не пустые
            if name and patronymic:
                return f"{name} {patronymic}"
            else:
                return name or patronymic  # Возвращаем то, что есть
        else:
            return None

def check_emp(surname,code):
    if code == 123:
        for i,emp in enumerate(staff_list):
            if emp[0] == surname:
                return True
        else:
                return False
    else:
         print('Неправильный пароль')
            
def greeting_employee(surname):
     for i,employee in enumerate(staff_list):
        if employee[0] == surname:
            print(f'Здравствуйте, {employee[1]} {employee[2]}!')

def check_head(surname,code):
    if code == 321:
        for i,head in enumerate(staff_list):
            if head[0] == surname and head[3] == 'Управляющий':
                return True
        else:
                return False
    else:
         print('Неправильный пароль')
            
def greeting_head(surname):
     for i,head in enumerate(staff_list):
        if head[0] == surname:
            print(f'Здравствуйте, {head[1]} {head[2]}!')