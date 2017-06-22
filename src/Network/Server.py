import socket
from threading import *

import requests

class Server:

    def __init__(self, port = 8000):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = requests.get('http://ip.42.pl/raw').text
        self.port = port
        self.serversocket.bind((self.host, self.port))
        print ("Server started and listening on {}:{}".format(self.host,self.port))
        self.Response="OK"


    class User(Thread):
        def __init__(self, socket, address, server):
            Thread.__init__(self)
            self.sock = socket
            self.addr = address
            self.start()

        def run(self):
            while 1:
                print('Client sent:', self.sock.recv(1024).decode())
                self.sock.send( b'{}'.format(Response) )

    def start():
        serversocket.listen(1)
        while 1:
            clientsocket, address = serversocket.accept()
            User(clientsocket, address, self)