#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import docs
from decimal import Decimal
import pickle


class Application(object):
    
    def __init__(self):
        self.__current_document = None
        self.__no_doc = {
            '1': ('Создать накладную', self.create_nakl),
            '7': ('Загрузить из файла', self.load_doc),

        }
        self.__with_doc = {
            '2': ('Добавить позицию', self.add_pos_to_nakl),
            '3': ('Показать накладную', self.current_doc_show),
            '4': ('Сменить номер накладной', self.change_nakl_number),
            '5': ('Сохранить в файл', self.save_current_doc),
            '6': ('Уничтожить накладную', self.kill_current_doc),
            
        }
        
    def available_commands(self):
        '''
        Возвращает словарь из команд пользователя,
        доступных в данный момент
        '''
        if self.__current_document is None:
            return self.__no_doc
        else:
            return self.__with_doc
        
    def user_action_sequence(self):
        '''
            Генератор-функция, которая формирует последовательность
            действий пользователя, причем 0 считается всега окончанием
            работы.
        '''
        while True:
            cmd = self.available_commands()
            for symbol, contents in cmd.items():
                print(f'{symbol} - {contents[0]}')
            print('0 - Завершить работу')
            action = input(': ').strip()
            if action == '0':
                break
            elif action in cmd:
                yield cmd[action][1]
            else:
                print('<Unknovn command>')
    
    def create_nakl(self):
        num = input('Номер: ').strip()
        self.__current_document = docs.Nakladnaya(number=int(num))
            
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
        
    def change_nakl_number(self):
        number = input('Новый номер: ').strip()
        self.__current_document.number = int(number)
        
    def current_doc_show(self):
        self.__current_document.show()
        
    def kill_current_doc(self):
        self.__current_document = None
        
    def save_current_doc(self):
        filepath = input('Файл: ').strip()
        with open(filepath, 'wb') as trg:
            pickle.dump(self.__current_document, trg, fix_imports=False)
        
    def load_doc(self):
        filepath = input('Файл: ').strip()
        with open(filepath, 'rb') as src:
            self.__current_document = pickle.load(src, fix_imports=False)
        
    def run(self):
        for action_func in self.user_action_sequence():
            action_func()
            
            
            
            