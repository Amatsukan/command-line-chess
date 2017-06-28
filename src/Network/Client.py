#! /usr/bin/python3

import socket

class Client:
	def __init__(self, host, port = 8000):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port
		self.socket.connect((self.host,self.port))

	def send(self, str):
	   self.socket.send(str.encode())

	def receive(self):
	   return self.socket.recv(1024).decode()

	def close_conection(self):
		self.socket.close()