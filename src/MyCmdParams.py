#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
import logging
from pathlib import Path


class MyCmdParams(object):
    
    def __init__(self):
        self.__args = self.__get_parser().parse_args()
        
    def __get_parser(self):
        parser = argparse.ArgumentParser(description='This is a very cool program')
        #добавим параметр цмд
        parser.add_argument('wpcode', type=str, help='Code of workplace')
        # опция со значением задаваемым пользователем
        parser.add_argument('--config-path', '-c', 
                            dest='conf_path', type=Path,
                            action='store', default=None,
                            help='Path to config file')

        #Опция-константа
        parser.add_argument('--debug', dest = 'level', 
                            action='store_const', const=logging.DEBUG, 
                            default=logging.WARNING,
                            help='Debug logging mode')
        parser.add_argument('--info', dest = 'level', 
                            action='store_const', const=logging.INFO, 
                            default=logging.WARNING,
                            help='Info logging mode')
        parser.add_argument('--warning', dest = 'level', 
                            action='store_const', const=logging.WARNING, 
                            default=logging.WARNING,
                            help='Warning logging mode (default)')
        parser.add_argument('--error', dest = 'level', 
                            action='store_const', const=logging.ERROR, 
                            default=logging.WARNING,
                            help='Error logging mode')
        parser.add_argument('--fatal-error', dest = 'level', 
                            action='store_const', const=logging.CRITICAL, 
                            default=logging.WARNING,
                            help='Log fatal errors only, not recommended')
                            
        # Опция-переключатель
        parser.add_argument('--internet', dest='internet_on', 
                            action='store_true', default=False, 
                            help='Internet enabled')
        parser.add_argument('--no-internet', dest='internet_on', 
                            action='store_false',default=False,
                            help='Local connection only (default)')
                            
        return parser
                            
    # редко используемые параметы цмд
    def param(self, name):
        return getattr(self.__args, name)

    # часто используемые параметры
    
    @property
    def wp_name(self):
        return self.__args.wpcode
        
    @property
    def config_path(self):
        if self.__args.conf_path is not None:
            return self.__args.conf_path.absolute()
        return Path.cwd()/'docs.conf'
    
    
    
    
    




                                                            