#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from Nakladnaya import Nakladnaya
from decimal import Decimal

n1 = None


while True:
    print('1 - Создать накладную')
    print('2 - Добавить позицию')
    print('3 - Показать накладную')
    print('4 - Сменить номер накладной')
    print('5 - Сохранить в файл')
    print('0 - Завершить работу')
    action = input(': ')
    if action == '0':
        break
    elif action == '1':
        num = input('Номер: ')
        n1 = Nakladnaya(number=int(num))
    elif action == '2':
        title = input('Наименование: ').strip()
        quantity = int(input('Количество: ').strip())
        price = input('Стоимость: ').strip()
        summa = input('Сумма: ').strip()
        if price == '':
            price = None
        else:
            price = Decimal(price)
        if summa == '':
            summa = None
        else:
            summa = Decimal(summa).quantize(Decimal('0.01'))
        n1.add_pos(title, quantity, price, summa)
    elif action == '3':
        if n1 is not None:
            n1.show()
        else:
            print('<накладная отсутствует>')
    else:
        print('<неизвестная команда>')