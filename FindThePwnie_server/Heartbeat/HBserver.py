#!/usr/bin/python
import socket
import sys
from thread import *

file = open('heartbeats.csv', 'w+')
file.write("Public IP,Date,Time,hostname,private IP" + "\n")
file.close()

host = '' ## leave empty
port = 443 ## listening port

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
        print("Failed to connect")
        sys.close();

print("Socket Created")

try:
        s.bind((host, port))
except socket.error:
        print("Binding Failed");
        sys.exit()

print("Socket has been bound")

s.listen(10)

print("Socket is Ready")

def clientthread(conn):
	try:
		file = open('heartbeats.csv', 'a')
		conn.send("Welcome to the server")

		while 1:
			data = conn.recv(1024)
			reply = data
			if not data:
				break;
			infotext = addr[0] + "," + reply
			file.write(infotext + "\n")
			conn.sendall(reply)

		file.close()
		conn.close()
	except Exception:
		import traceback


while 1:
	conn, addr = s.accept()
	start_new_thread( clientthread, (conn,))

s.close()
