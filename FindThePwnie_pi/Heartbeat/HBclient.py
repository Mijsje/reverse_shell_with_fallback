#!/usr/bin/env python2
import socket
import sys
import requests
import time
from datetime import datetime

while 1:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error:
		print("Failed to connect")
		sys.close();

	print("Socket Created")

	ip = "10.10.10.10" ## remote server IP
	port = 443 ## remote server port

	print("IP address: " + ip)


	s.connect((ip, port))

	print("Socket connected to " + ip + " on port: " + str(port))

	message = datetime.now().strftime('%Y-%m-%d,%H:%M:%S') + "," + socket.gethostname() + "," + s.getsockname()[0]
	try:
		s.sendall(message.encode())
	except socket.error:
		print("Did not send Successfully")
		sys.exit()

	print("Message Sent Successfully")

	reply = s.recv(4096)

	print(reply.decode())

	s.close()
	time.sleep(60)
