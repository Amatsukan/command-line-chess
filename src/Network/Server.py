import socket
import requests
from threading import *
from netifaces import interfaces, ifaddresses, AF_INET

class Server:

    def __init__(self, host="localhost", port = 8000):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host#"10.3.0.37"
        self.port = port
        print ("Server started and listening on {}:{}".format(self.host,self.port))
        self.serversocket.bind((self.host, self.port))
        self.Response="OK"
        self.oponent = None


    class User(Thread):
        def __init__(self, socket, address, server):
            Thread.__init__(self)
            self.sock = socket
            self.addr = address
            self.start()

        def receive(self):
            return self.sock.recv(1024).decode()

        def send(self, msg):
            self.sock.send( b'{}'.format(msg) )

    def start(self):
        self.serversocket.listen(1)
        while 1:
            clientsocket, address = self.serversocket.accept()
            
            if(self.oponent == None or self.oponent.addr == address):
                self.oponent = self.User(clientsocket, address, self)

    def send_to_oponent(self, msg):
        return self.oponent.send(msg)

    def receive_from_oponent(self):
        return self.oponent.receive()

    def get_interfaces():
        ret = ""
        for ifaceName in interfaces():
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
            ret = '{}\n{}: {}'.format(ret, ifaceName, ', '.join(addresses))
        return ret