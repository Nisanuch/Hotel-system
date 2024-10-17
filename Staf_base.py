def add_staff(surname, name, patronymic, possition, salary):
    """Добавление сотрудника в список."""

    staff_list.append((surname, name, patronymic, possition, salary))

def print_staff():
    """Вывод списка сотрудников."""
    k = 1
    print('ФИО, Позиция, Зарплата:')
    for i in staff_list:
        print(f"{k}.{i}")
        k += 1

def remove_staff(surname):
    """Удаляет сотрудника по фамилии."""
    for i, employee in enumerate(staff_list):
        if employee[0] == surname:
            del staff_list[i]
            print(f"Сотрудник {surname} уволен.")
            return
    print(f"Сотрудник {surname} не найден.")

staff_list = []

add_staff('Григорьев', 'Владимир', 'Вячеславович', 'Управляющий', 500000)
add_staff('Слепнева', 'Анжелика', 'Витальевна', 'Портье', 100000)
add_staff('Кудрявцев', 'Евгений', 'Генадьевич', 'Главный инженер', 150000)