#!/bin/python3
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])#Translate hostname to IPv4
else:
	print("Invalid amount of argumetns.")
	print("Syntax: python3 scanner.py <ip>")
#Banner
print("#" * 50)
print("Scanning Target: " + target)
print("Scan Start: "+str(datetime.now()))
print("#" * 50)

try:
	for port in range (1,99):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port))#returns an error indicator
		#print("Checking port: {}".format(port))
		if result==0:
			print ("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
