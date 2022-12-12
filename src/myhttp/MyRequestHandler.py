#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from http.server import BaseHTTPRequestHandler
import queue

class MyRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/count':
            N = self.server.queue.qsize()
            self.send_response(200)
            self.send_header('Content-type', 
                            'text/html; charset=utf-8')
            self.end_headers()
            answer = f'''
                <html>
                  <body>
                    <p> В очереди {N} элементов </p>
                  </body>
                </html>
            '''.encode('utf-8')
            self.wfile.write(answer)
        elif self.path == '/first':
        
            self.send_response(200)
            self.send_header('Content-type', 
                            'text/html; charset=utf-8')
            self.end_headers()
            
            try:
            
                elem = self.server.queue.get(block=True, timeout=5)
                name = elem['title']
                price = elem['price']
                answer = f'''
                <html>
                  <body>
                    <table border="1">
                        <tr><td>Наименование</td><td>{name}</td></tr>
                        <tr><td>Цена</td><td>{price}</td></tr>
                    </table>
                  </body>
                </html>
            '''.encode('utf-8')
            except queue.Empty:

                answer = f'''
                    <html>
                      <body>
                        <p> Очередь пустая </p>
                      </body>
                    </html>
                '''.encode('utf-8')
            self.wfile.write(answer)
        else:
            self.send_error(404, 'Path not founf')


    def do_POST(self):
        
        try:
            data_size = int(self.headers['Content-length'])
            data = self.rfile.read(data_size)
            data = data.decode('utf-8')
            data = json.loads(data)
            self.server.queue.put(data, block=True, timeout=5)
            
            #временно
            print(self.server.queue.qsize())
            
            self.send_response(200)
            self.send_header('Content-type', 
                            'text/plain; charset=utf-8')
            self.end_headers()
            answer = 'Все хорошо do post'.encode('utf-8')
            self.wfile.write(answer)
        
        except queue.Full:
            self.send_error(423, 'Queue is full')