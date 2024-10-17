def add_sale(sale):
    """Добавляет акции."""
    sales_list.append((sale))

def print_sales():
    """Вывод списка акций."""
    k = 1
    print('Акции:')
    for i in sales_list:
        print(f"{k}.{i}")
        k += 1

def remove_sale():
    """Удаляет акцию."""
    if len(sales_list) == 0:
        print("Нет акций для удаления.")
    else:
        print("Акции:")
        print_sales()
        n = int(input("Введите номер акции для удаления: "))
        if n > 0 and n <= len(sales_list):
                sales_list.pop(n-1)
                print("Акция удалена.")
                return
        else:
                print("Нет акции с таким номером.")

def edit_sale():
    """Изменяет акцию."""
    if len(sales_list) == 0:
        print("Нет акций для удаления.")
    else:
        print("Акции:")
        print_sales()
        n = int(input("Введите номер акции для изменения: "))
        if n > 0 and n <= len(sales_list):
                sale = input("Введите новое название акции: ")
                sales_list[n-1] = sale
                print("Акция изменена.")
                return
        else:
                print("Нет акции с таким номером.")



sales_list = []

add_sale('Скидка 20% на посещение массажа в спа')
add_sale('Коктейли за баром c 50% скидкой')