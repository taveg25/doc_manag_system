#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from configparser import ConfigParser, NoOptionError, NoSectionError

from pathlib import Path

#Создаем собственный тип исключений
class WorkplaceNotFound(Exception): pass


class MyConfig(ConfigParser):

    def __init__(self, conf_path=None):
        super().__init__()
        if conf_path is not None:
            self.read(conf_path)
        
    @property
    def doc_path(self):
        try:
            general = self.get('GENERAL', 'doc_path')
            return Path(general).absolute()
        except ( NoSectionError, NoOptionError):
            return Path.cwd() / 'docs'
            
    def workplace(self, code):
        
        try:
        # Проверили, чт код рабочего места имеется
            if code not in self['WORKPLACES'].values():
                raise WorkplaceNotFound(code)
            
            # определяем параметры рабочего места
            wp = self[code]
            ip_addr = wp.get('IP', None)
            port = wp.get('port', None)
            if port is not None:
                port = int(port)
                
            return(ip_addr, port)
        
        except KeyError as exc:
            raise WorkplaceNotFound(code) from exc
    
    @property
    def workplaces(self):
        try:
            return list(self['WORKPLACES'].values() )
        except KeyError:
            return []
    
    
    
    
    
        