from Clients_base import *
from Spa_base import *
from Restourant_base import *
from Preferences_base import *
from Staf_base import *
from Changes_employee import * 
from Sales_base import *
from Price_base import *
from Cheking import *
from Clients import *
from Clients_base import *


key0 = 0
while key0 != 4:
    print('Кто входит в систему?')
    print('1.Гость\n2.Сотрудник отеля\n3.Управляющий отелем\n4.Выход\n')
    per = int(input())
    if per == 1:
        print("Вы вошли как гость\n")
        cust_sur = input('Введите фамилию: ')
        print()
        if check_client(cust_sur):
            print('Здравствуйте!')
            print(get_client_by_surname(cust_sur,fields='name, patronymic'))
            print()
            key8 = 0
            while key8 != 4:
                print()
                print('Что вы хотите сделать?')
                cust_choise = int(input('1.Записаться в СПА\n2.Забронировать столик\n3.Пароль от WI-FI\n4.Акции\n5.Мои бонусы\n6.Назад\n'))
                if cust_choise == 1:
                    cust_day = int(input('B какой день Вы хотите посетить СПА? '))
                    cust_month = int(input('B какой месяц Вы хотите посетить СПА? '))
                    cust_time = int(input('B какое время Вы хотите посетить СПА? '))
                    cust_quantity = int(input('Какое количество процедур хотите посетить в СПА? '))
                    spa_client1 = Spa(cust_sur, cust_day, cust_month, cust_time, cust_quantity)
                    Spa.save_spa_to_db(spa_client1)
                    print('Вы записались в СПА')
                    print()
                    spa_client1 = ''
                elif cust_choise == 2:
                    cust_day = int(input('B какой день Вы хотите посетить ресторан? '))
                    cust_month = int(input('B какой месяц Вы хотите посетить ресторан? '))
                    cust_time = int(input('B какое время Вы хотите посетить ресторан? '))
                    cust_quantity = int(input('Какое количество человек будет? '))
                    restorant_client1 = Restaurant(cust_sur, cust_day, cust_month, cust_time, cust_quantity)
                    restorant_client1.save_to_db()
                    restorant_client1 = ''
                    print('Вы забронировали столик в ресторане')
                    print()
                elif cust_choise == 3:
                    print('Login: Emerates hotel\nPassword:123Fiesta456')
                    print()
                elif cust_choise == 4:
                    print_sales()
                    print()
                elif cust_choise == 5:
                    show_points(cust_sur)
                    print()
                elif cust_choise == 6:
                    key8 = 4

        else:
            print('Такой фамилии нет в списке\n')

    elif per == 2:
        
            print("Вы вошли как сотрудник")
            print()
            sur_emp = input('Введите фамилию: ')
            cod_emp = int(input('Введите пароль: '))
            print()
            if check_emp(sur_emp,cod_emp):
                greeting_employee(sur_emp)
                print()
                key2 = 0
                while key2 != 6:
                    print()
                    print('Что хотите сделать?')
                    emp_choise = int(input('1.Заселение клиента\n2.Просмотр базы клиентов\n3.Запси в СПА\n4.Брони столиков\n5.Предпочтения гостей\n6.Назад\n'))
                    if emp_choise == 1:
                        """Заселение"""
                        client_surname = input('Введите Фамилию клиента: ')
                        client_name = input('Введите Имя клиента: ')
                        client_patronymic = input('Введите Отчество клиента: ')
                        client_id = input('Введите паспортные данные клиента: ')
                        ent_data = input('Введите дату заезда: ')
                        num_data = int(input('Насколько дней?: '))
                        room_class = int(input('Какой уовень номера? \n1.Стандарт \n2.Люкс \n3.Президентский \n'))
                        room_num = input('Номер комнаты? ')
                        print(price(num_data,room_class))
                        client_points = 0.1 * price_num(num_data,room_class)
                        new_client = Client(client_surname,client_name,client_patronymic,client_id,ent_data,num_data,room_class,room_num,client_points)
                        add_client_to_db(new_client)
                        new_client = ''
                        print('Клиент успешно зарегистрирован!')
                        
                    elif emp_choise == 2:
                        """База клиентов"""
                        cursor.execute("SELECT * FROM clients")

                        # Получение результатов
                        rows = cursor.fetchall()

                        # Вывод результатов
                        for row in rows:
                            print(row)


                    elif emp_choise == 3:
                        """Спа"""
                        key3 = 0
                        while key3 != 4:
                            spa = int(input('1.Просмотр записей\n2.Записать клиента\n3.Удалить запись\n4.Найти запись о клиенте\n5.Назад\n'))
                            if spa == 1:
                               # Получение списка клиентов
                                clients_data = get_spa_clients()
                                print("Список клиентов:")
                                for client in clients_data:
                                    print(client)
                            elif spa == 2:
                                client_surname = input('Введите Фамилию клиента: ')
                                spa_day = input('Введите день записи: ')
                                spa_month = input('Введите месяц записи: ')
                                spa_time = int(input('Введите время записи: '))
                                spa_num_data = int(input('Сколько процедур?: '))
                                new_spa_client = Spa(client_surname, spa_day, spa_month, spa_time, spa_num_data)
                                print('Клиент записан')
                                Spa.save_spa_to_db(new_spa_client)
                                new_spa_client = ''
                            elif spa == 3:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Spa.remove_spa_client(client_surname))
                            elif spa == 4:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Spa.find_spa_client(client_surname))
                                print()
                            elif spa == 5:
                                key3 = 4
                            else:
                                print('Неправильный выбор')

                    

                    elif emp_choise == 4:
                        """Брони столиков"""
                        key4 = 0
                        while key4 != 4:
                            table = int(input('1.Просмотр записей\n2.Забронировать столик клиенту\n3.Удалить бронь\n4.Найти столик по фамилии\n5.Назад\n'))
                            if table == 1:
                                display_all_clients()
                            elif table == 2:
                                client_surname = input('Введите Фамилию клиента: ')
                                table_day = input('Введите дату бронирования: ')
                                table_month = input('Введите месяц бронирования: ')
                                table_time = int(input('Введите время бронирования: '))
                                table_num_data = int(input('Сколько человек?: '))
                                restorant_client1 = Restaurant(client_surname, table_day, table_month, table_time, table_num_data)
                                restorant_client1.save_to_db()
                                print('Столик забронирован')
                            elif table == 3:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Restaurant.remove_client(client_surname))
                            elif table == 4:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Restaurant.find_client(client_surname))
                                print()
                            elif table == 5:
                                key4 = 4
                            else:
                                print('Неправильный выбор')

                    elif emp_choise == 5:
                        """Предпочтения гостей"""
                        key5 = 0
                        while key5 != 4:
                            preferences = int(input('1.Просмотр предпочтений\n2.Добавить предпочтения\n3.Удалить предпочтения\n4.Найти предпочтения по фамилии\n5.Назад\n'))
                            if preferences == 1:
                                # Вызов функции для отображения всех предпочтений
                                display_all_preferences()
                                print()
                            elif preferences == 2:
                                client_surname = input('Введите Фамилию клиента: ')
                                preference = input('Введите предпочтение: ')
                                print(add_preference(client_surname, preference))
                                print('Предпочтения добавлены')
                                print()

                            elif preferences == 3:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(remove_preferences(client_surname))
                            elif preferences == 4:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(find_preferences(client_surname))
                                print()
                            elif preferences == 5:
                                key5 = 4
                            else:
                                print('Неправильный выбор')
                    
                
                    elif emp_choise == 6:
                        key2 = 6
                    else:
                        print('Неправильный выбор')
            else:
                print('Неправильный ввод')
                print()
    elif per == 3:
        print("Вы вошли как управляющий")
        print()
        sur_head = input('Введите фамилию: ')
        cod_head = int(input('Введите пароль: '))
        print()
        if check_head(sur_head,cod_head):
            greeting_head(sur_head)
            print()
            key2 = 0
            while key2 != 6:
                print('Что хотите сделать?')
                head_choise = int(input('1.Заселение клиента\n2.Просмотр базы клиентов\n3.Запси в СПА\n4.Брони столиков\n5.Предпочтения гостей\n6.Базы сотрудников\n7.Акции\n8.Назад\n'))
                if head_choise == 1:
                        """Заселение"""
                        client_surname = input('Введите Фамилию клиента: ')
                        client_name = input('Введите Имя клиента: ')
                        client_patronymic = input('Введите Отчество клиента: ')
                        client_id = input('Введите паспортные данные клиента: ')
                        ent_data = input('Введите дату заезда: ')
                        num_data = int(input('Насколько дней?: '))
                        room_class = int(input('Какой уовень номера? \n1.Стандарт \n2.Люкс \n3.Президентский \n'))
                        room_num = input('Номер комнаты? ')
                        print(price(num_data,room_class))
                        client_points = 0.1 * price_num(num_data,room_class)
                        new_client = Client(client_surname,client_name,client_patronymic,client_id,ent_data,num_data,room_class,room_num,client_points)
                        add_client_to_db(new_client)
                        new_client = ''
                        print('Клиент успешно зарегистрирован!')
                        
                elif head_choise == 2:
                        """База клиентов"""
                        cursor.execute("SELECT * FROM clients")

                        # Получение результатов
                        rows = cursor.fetchall()

                        # Вывод результатов
                        for row in rows:
                            print(row)

                elif head_choise == 3:
                        """Спа"""
                        key3 = 0
                        while key3 != 4:
                            spa = int(input('1.Просмотр записей\n2.Записать клиента\n3.Удалить запись\n4.Найти запись клиента по фамилии\n5.Назад\n'))
                            if spa == 1:
                                # Получение списка клиентов
                                clients_data = get_spa_clients()
                                print("Список клиентов:")
                                for client in clients_data:
                                    print(client)
                            elif spa == 2:
                                client_surname = input('Введите Фамилию клиента: ')
                                spa_day = input('Введите день записи: ')
                                spa_month = input('Введите месяц записи: ')
                                spa_time = int(input('Введите время записи: '))
                                spa_num_data = int(input('Сколько процедур?: '))
                                new_spa_client = Spa(client_surname, spa_day, spa_month, spa_time, spa_num_data)
                                print('Клиент записан')
                                Spa.save_spa_to_db(new_spa_client)
                                new_spa_client = ''
                            elif spa == 3:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Spa.remove_spa_client(client_surname))
                            
                            elif spa == 4:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Spa.find_spa_client(client_surname))
                                print()

                            elif spa == 5:
                                key3 = 4
                            else:
                                print('Неправильный выбор')

                    

                elif head_choise == 4:
                        """Брони столиков"""
                        key4 = 0
                        while key4 != 4:
                            table = int(input('1.Просмотр записей\n2.Забронировать столик клиенту\n3.Удалить бронь\n4.Найти столик по фамилии\n5.Назад\n'))
                            if table == 1:
                                display_all_clients()
                            elif table == 2:
                                client_surname = input('Введите Фамилию клиента: ')
                                table_day = input('Введите дату бронирования: ')
                                table_month = input('Введите месяц бронирования: ')
                                table_time = int(input('Введите время бронирования: '))
                                table_num_data = int(input('Сколько человек?: '))
                                restorant_client1 = Restaurant(client_surname, table_day, table_month, table_time, table_num_data)
                                restorant_client1.save_to_db()
                                print('Столик забронирован')
                            elif table == 3:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Restaurant.remove_client(client_surname))
                                print()
                            elif table == 4:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(Restaurant.find_client(client_surname))
                                print()
                            elif table == 5:
                                key4 = 4
                            else:
                                print('Неправильный выбор')

                elif head_choise == 5:
                        """Предпочтения гостей"""
                        key5 = 0
                        while key5 != 4:
                            preferences = int(input('1.Просмотр предпочтений\n2.Добавить предпочтения\n3.Удалить предпочтения\n4.Найти предпочтения по фамилии\n5.Назад\n'))
                            if preferences == 1:
                                # Вызов функции для отображения всех предпочтений
                                display_all_preferences()
                                print()
                            elif preferences == 2:
                                client_surname = input('Введите Фамилию клиента: ')
                                preference = input('Введите предпочтение: ')
                                print(add_preference(client_surname, preference))
                                print('Предпочтения добавлены')
                                print()

                            elif preferences == 3:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(remove_preferences(client_surname))
                                print()
                            elif preferences == 4:
                                client_surname = input('Введите Фамилию клиента: ')
                                print(find_preferences(client_surname))
                                print()
                            elif preferences == 5:
                                key5 = 4
                            else:
                                print('Неправильный выбор')
                    
                elif head_choise == 6:
                    """Просмотр базы сотрудников"""
                    key6 = 0
                    while key6 != 4:
                        staff = int(input('1.Просмотр сотрудников\n2.Добавить сотрудника\n3.Уволить сотрудника\n4.Изменить должность сотрудника\n5.Изменить заработную плату\n6.Штрафы\n7.Назад\n'))
                        if staff == 1:
                            """База сотрудников"""
                            k = 1
                            for i in staff_list:
                                print(f"{k}.{i}")
                                k += 1
                            print()
                        elif staff == 2:
                            """Добавление сотрудника"""
                            surname = input('Введите Фамилию сотрудника: ')
                            name = input('Введите Имя сотрудника: ')
                            patronymic = input('Введите Отчество сотрудника: ')
                            position = input('Введите должность сотрудника: ')
                            salary = int(input('Введите заработную плату сотрудника: '))
                            print(add_staff(surname, name, patronymic, position, salary))
                            print('Сотрудник добавлен')
                            print()
                        elif staff == 3:
                            """Увольнение сотрудника"""
                            surname = input('Введите Фамилию сотрудника: ')
                            print(remove_staff(surname))
                            print()
                        elif staff == 4:
                            """Изменение должности"""
                            surname = input('Введите Фамилию сотрудника: ')
                            position = input('Введите новую должность сотрудника: ')
                            change_position(surname, position)
                            print()
                        elif staff == 5:
                            """Изменение заработной платы"""
                            surname = input('Введите Фамилию сотрудника: ')
                            salary = int(input('Введите новую заработную плату сотрудника: '))
                            change_salary(surname, salary)
                            print()
                        elif staff == 6:
                            """Штрафы"""
                            key7 = 0
                            while key7 != 3:
                                choise = int(input('1.Посмотреть штрафы\n2.Добавить штраф\n3.Назад\n'))
                                if choise == 1:
                                    print(print_fines())
                                    print()
                                elif choise == 2:
                                    surname = input('Введите Фамилию сотрудника: ')
                                    fine = int(input('Введите сумму штрафа сотрудника: '))
                                    add_fine(surname,fine)
                                    print()
                                elif choise == 3:
                                    key7 = 3
                                else:
                                    print('Неправильный выбор')
                        elif staff == 7:
                            key6 = 4
                        else:
                            print('Неправильный выбор')


                elif head_choise == 7:
                    """Акции"""
                    key9 = 0
                    while key9 != 4:
                        choise = int(input('\n1.Посмотреть акции\n2.Добавить акцию\n3.Удалить акцию\n4.Изменить акцию\n5.Назад\n'))
                        if choise == 1:
                            print_sales()
                            print()
                        elif choise == 2:
                            sale = input('Введите суть акции: ')
                            add_sale(sale)
                            print()
                        elif choise == 3:
                            remove_sale()
                            print()
                        elif choise == 4:
                            edit_sale()
                        elif choise == 5:
                            key9 = 4
                            print()
                        else:
                            print('Неправильный выбор')
                
                elif head_choise == 8:
                        key2 = 6
                else:
                        print('Неправильный выбор')
        else:
            print('Неправильный ввод')
            print()

    elif per == 4:    
        print("Вы вышли из системы")
        key0 = 4
    else:
        print("Неправильный ввод.")
