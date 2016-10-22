# Fall 2016 CSci4211: Introduction to Computer Networks
# This program serves as the server of DNS query
# Written in Python v3

import sys, threading, os
from socket import *
from threading import Lock
from LRUCache import LRUCache

cacheLock = Lock()
cache = LRUCache(5)

#main and monitorquit function written by instructor
def main():
	try:
		#create a socket object, SOCK_STREAM for TCP
		sSock = socket(AF_INET, SOCK_STREAM)
	except error as msg:
		sSock = None # Handle exception
	try:
		#bind socket to the current address on port 5001
		host = "localhost"
		port = 5001
		sSock.bind((host, port))
		#Listen on the given socket maximum number of connections queued is 20
		sSock.listen(20)
	except error as msg:
		sSock = None # Handle exception

	# If the socket cannot be opened, quit the program.
	if sSock is None:
		print("Error: cannot open socket")
		sys.exit(1)

	#start the control thread, which may terminate the program while encountering input "exit"
	monitor = threading.Thread(target=monitorQuit, args=[])
	monitor.start()

	print("Server is listening...")

	while 1:
		#blocked until a remote machine connects to the local port 5001
		connectionSock, addr = sSock.accept()
		server = threading.Thread(target=dnsQuery, args=[connectionSock, addr[0]])
		server.start()


def dnsQuery(connectionSock, srcAddress):
	data = connectionSock.recv(1024).decode()

	#domain names are case insensitive
	data = data.lower()

	if data == "hangup":
		connectionSock.close()

	try:
		#First, check cache for the stored domain name
		#if the name is found, return that
		cacheLock.acquire()
		ip_from_cache = cache.query(data)
		cacheLock.release()

		if (ip_from_cache != None):
			returnMessage = "\'Local DNS:" + data + ":" + ip_from_cache + "\'"
	    #If the host name was not found in the local DNS cache,
	    #use the function to look it up, 
	    #store it in cache, and return to the client
		else:
			ip_from_cache = gethostbyname(data)

			cacheLock.acquire()
			cache.add(data, ip_from_cache)
			cacheLock.release()

			returnMessage = "\'Root DNS:" + data + ":" + ip_from_cache + "\'"

	except gaierror:
		returnMessage = "\'Host Not Found\'"

	connectionSock.send(returnMessage.encode())
	connectionSock.close()

def monitorQuit():
	while 1:
		sentence = input()
		if sentence == "exit":
			#os.getpid() returns the parent thread id, which is the id of
			#the main program and hence terminates the main program
			os.kill(os.getpid(),9)

main()
