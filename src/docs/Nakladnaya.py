#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from .NakPos import NakPos
from .Document import Document


class Nakladnaya(Document):

    def __init__(self, number=None):
        '''
        @TODO: Сделать возможность генераци номеров
               по умолчанию, если номер не был задан
               пользователем.
               добавить: адрес доставки, дата выписки, 
               дата отправки, дата факт доставки.
        '''
        super().__init__(number)
        self.__address = None
        self.__subscribe = None
        self.__positions = []
        
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, new_address):
        if self.__subscribe is None:
            self.__address = new_address
        else:
            print('В подписанную накладную изменения не вносят')
    @property
    def good(self):
        if self.__address is None:
            return False
        if len(self.__positions) == 0:
            return False
        return all( (p.good for p in self.__positions) )
    
    
    @property
    def subscribe(self):
        return self.__subscribe
    
    @subscribe.setter
    def subscribe(self, new_subscribe):
        if self.good:
            self.__subscribe = new_subscribe
        else:
            print('Плохую накладную нельзя подписывать')
    
    @property
    def itogo (self):
        s = ( x.summa for x in self.__positions )
        return sum(s)
        
    def add_pos(self, *args, **kwargs):
        if self.__subscribe is None:
            pos = NakPos(*args, **kwargs)
            self.__positions.append(pos)
        else:
            print('В подписанную накладную изменения не вносят')
        
        
    def show(self):
        print(40*'=')
        if not self.good:
            print('ПЛОХаЯ НАКлАДАНАЯ')
        print(f'Накладная No {self.number}')
        ct = self.created.strftime('%Y.%m.%d %H:%M')
        print(f'  Создана: {ct}')
        if self.address is not None:
            print(f'  Адрес доставки: {self.address}')
        print(40*'-')
        for k, pos in enumerate(self.__positions, 1):
            print(f'{k:2}. {pos}')
        print(f'Итого: {self.itogo:7.2f}')
        if self.subscribe is not None:
            print(f'Накладная подписана: {self.subscribe}')
        print(40*'=')