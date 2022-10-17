#!/usr/bin/env python3

import itertools 
import sys

# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12345			
connecting = True
# connect to the server on local computer
s.connect(('192.168.10.124', port))

	

def shift(a, b, reverse=False):
	# a and b are chars
	x = (ord(a) - ord('a') + ord(b) - ord('a')) % 26 
	if reverse:
		x = (ord(a) - ord(b) + 26) %26
	x +=ord('a')
	return chr(x)

def encrypt(st, key): 
	output = ""
	for (a, b) in zip(st, itertools.cycle(key)): 
		upperFlag = False
		if a.isupper():
			a = a.lower() 
			upperFlag = True
		new_char = shift(a, b) 
		if upperFlag:
			new_char = new_char.upper() 
		output += new_char
	return output

while(connecting):
	st = input("Input the string to encrypt: ") 
	key = input("Enter the key: ").lower()
	if (not st.isalpha() or not key.isalpha()):  
		print("Failure")
		sys.exit(1)
	ciphertext = encrypt(st, key) 
	print("Ciphertext: {}".format(ciphertext))
	s.send(ciphertext.encode())
	s.send(key.encode())
s.close()
