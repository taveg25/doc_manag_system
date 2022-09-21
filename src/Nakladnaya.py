#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NakPos import NakPos

class Nakladnaya(object):

    def __init__(self, number=None):
        '''
        @TODO: Сделать возможность генераци номеров
               по умолчанию, если номер не был задан
               пользователем
        '''
        self.__number = number
        self.__positions = []
    
    @property
    def itogo (self):
        s = ( x.summa for x in self.__positions )
        return sum(s)
        
    def add_pos(self, *args, **kwargs):

        pos = NakPos(*args, **kwargs)
        self.__positions.append(pos)
        
    def show(self):
        print(40*'=')
        print(f'Накладная No {self.__number}')
        print(40*'-')
        for k, pos in enumerate(self.__positions, 1):
            print(f'{k:2}. {pos}')
        print(f'Итого: {self.itogo:7.2f}')
        print(40*'=')