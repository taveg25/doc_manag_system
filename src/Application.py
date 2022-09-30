#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Nakladnaya import Nakladnaya
from decimal import Decimal


class Application(object):
    
    def __init__(self):
        self.__current_document = None
    
    
    def user_action_sequence(self):
        '''
            Генератор-функция, которая формирует последовательность
            действий пользователя, причем 0 считается всега окончанием
            работы.
        '''
        while True:
            print('1 - Создать накладную')
            print('2 - Добавить позицию')
            print('3 - Показать накладную')
            print('4 - Сменить номер накладной')
            print('5 - Сохранить в файл')
            print('0 - Завершить работу')
            action = input(': ').strip()
            if action == '0':
                break
            yield action
    
    def create_nakl(self):
        num = input('Номер: ').strip()
        self.__current_document = Nakladnaya(number=int(num))
            
    def add_pos_to_nakl(self):
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
        self.__current_document.add_pos(title, quantity, price, summa)
        
    def run(self):
    
        for action in self.user_action_sequence():
            if action == '1':
                self.create_nakl()
            elif action == '2':
                self.add_pos_to_nakl()
            elif action == '3':
                self.__current_document.show()
            else:
                print('<неизвестная команда>')