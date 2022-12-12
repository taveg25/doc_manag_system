#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
from queue import Queue
from http.server import HTTPServer
from .MyRequestHandler import MyRequestHandler

class MyHttpServer(HTTPServer):

    def __init__(self, server_address, queue_size=10):
        super().__init__(server_address, MyRequestHandler)
        self.__queue = Queue(queue_size)
        
    @property
    def queue(self):
        return self.__queue
    
    @classmethod
    def srv_start(cls, server_address, queue_size):
        server = cls( server_address, 20)


        thread = threading.Thread(group=None, 
                                  target=server.serve_forever)
        
        thread.start()
        
        return (server, thread)

