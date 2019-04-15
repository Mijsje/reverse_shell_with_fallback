#!/usr/bin/python
from subprocess import Popen
import sys
import time

heartbeat = sys.argv[1]
firstTry = sys.argv[2]
secondTry = sys.argv[3]
#thirdTry = sys.argv[4]
#fourthTry = sys.argv[5]

while 1:
	Popen("python " + heartbeat, shell=True)

	print("Starting " + firstTry)
        p = Popen("python3 " + firstTry, shell=True)
        p.wait()

        print("Starting " + secondTry)
        p = Popen("python " + secondTry, shell=True)
        p.wait()

	time.sleep(60)

#        print("Starting " + thirdTry)
#        p = Popen("python " + thirdTry, shell=True)
#        p.wait()

#        print("Starting " + fourthTry)
#        p = Popen("python " + fourthTry, shell=True)
#        p.wait()

