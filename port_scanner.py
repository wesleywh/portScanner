#!/usr/bin/env python
import socket				#for socket scanning
from threading import *			#for threading
import subprocess			#to run the clean command and system exit
import sys
from datetime import datetime
#from queue import Queue		#for threading (using queues)
import argparse				#used for allowing command line switches 

def main():
	#Available command line options
	parser = argparse.ArgumentParser(description='Allow command line arguments.')
	parser.add_argument('-H',metavar='H', nargs="+", help="Target host to scan")
	parser.add_argument('-p',metavar="p", nargs="+", help="List of Ports to Scan")

	#all all available arguments to the 'args' variable
	args = parser.parse_args()
	
	#check what time the scan started
	t1=datetime.now()
	scanports = []

	#parse the arguments for the ports and assign port numbers to be scanned
	if "-" in args.p[0]:
		temp = []
		temp = args.p[0].replace('-',' ').split(' ')
		temp[-1] = int(temp[-1])
		for portnumber in range(1,temp[-1]):
			scanports.append(portnumber);
	elif len(args.p) > 1:
		for portnumber in args.p:
			scanports.append(portnumber);
	else:
		scanports = args.p	

	#assign the variables
	for host in args.H:
		#remoteServer = host
		#remoteServerIP = socket.gethostbyname(remoteServer)
	
		#print a banner with info on which host we are about to scan
		print "-" * 60
		print "Please wait, scanning remote host",host
		string = "Scanning Ports "
		for portInput in args.p:
			string += portInput+" "
		print string
		print "-" * 60

		#threaded port scanning
		scan(host, scanports)

	#Checking the time again
	t2=datetime.now()

	#Calculates the differences of time, to see how log it took to run the script
	total = t2 - t1

	#print information to screen
	print "Scanning Completed in: ", total

def scan(host, ports):
	#Using the range function to specify ports (scan ports between 1 and 1024)
	#We also put in some error handling for catching errors
	threads = []
	for port in ports:
		t = Thread(target=worker, args=(host,port))
		threads.append(t)
		t.start()

def worker(remoteServerIP, port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "Port {}: \t Open".format(port)
		sock.close()
	except KeyboardInterrupt:
		print "Canceled the scan."
		sys.exit()
	except socket.gaierror:
		print "Hostname could not be resolved. Exiting."
		sys.exit()
	except socket.error:
		print "Could not connect to server"
		sys.exit()

if __name__ == "__main__":
	subprocess.call('clear', shell=True) #clear the screen
	main()				     #execute main code
