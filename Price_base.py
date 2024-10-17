def price(days,room):
    """Считает и выводит стоимость номера."""
    if room  == 1:
        summ = days * 7000
        print('Стоимость за', days, 'дней поездки: ',summ)
    elif room == 2:
        summ = days * 12000
        print('Стоимость за', days, 'дней поездки: ',summ)
    elif room == 3:
        summ = days * 20000
        print('Стоимость за', days, 'дней поездки: ',summ)

def price_num(days,room):
    """Счет стоимости номера."""
    if room  == 1:
        return days * 7000
    elif room == 2:
        return days * 12000
    elif room == 3:
        return days * 20000