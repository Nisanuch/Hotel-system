from Staf_base import *

def change_position(surname, position):
    """Изменяет должность сотрудника."""
    for i, employee in enumerate(staff_list):
        if employee[0] == surname:
            staff_list[i] = (employee[0], employee[1], employee[2], position, employee[4])
            print(f"Для сотрудника {surname} обновлены данные: позиция - {position}.")
            return
    print(f"Сотрудник {surname} не найден.")

def change_salary(surname, salary):
    """Изменяет зарплату сотрудника."""
    for i, employee in enumerate(staff_list):
        if employee[0] == surname:
            staff_list[i] = (employee[0],employee[1],employee[2],employee[3],salary)
            print(f"Для сотрудника {surname} обновлены данные: зарплата - {salary}.")
            return
    print(f"Сотрудник {surname} не найден.")

def add_fine(surname,fine):
    """Добавляет штраф сотруднику."""
    for i, client in enumerate(fine_list):
        if client[0] == surname:
            client[1] += fine
            print(f"Штраф сотруднику {surname} добавлен.")
            return
    else:
        fine_inf = (surname, fine)
        fine_list.append(fine_inf)
        print(f"Штраф сотруднику {surname} добавлен.")                                                       
        
def print_fines():
    """Вывод списка сотрудников c штрафами."""
    k = 1
    print('ФИО, Штраф:')
    for i in fine_list:
        print(f"{k}.{i}")
        k += 1

fine_list = []