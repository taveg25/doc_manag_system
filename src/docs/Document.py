#!/usr/bin/ena python3
# -*- coding: utf-8 -*-

from datetime import datetime


class Document(object):

    def __init__(self, number=None):
        self.__created = datetime.now()
        self.__number = number
    
    @property
    def created(self):
        return self.__created

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        self.__number = new_number

    def show(self):
        print(40*'=')
        print(f'Документ No {self.number}')
        ct = self.created.strftime('%Y.%m.%d %H:%M')
        print(f'Создан {ct}')
        print(40*'=')