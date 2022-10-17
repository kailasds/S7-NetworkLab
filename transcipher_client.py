#!/usr/bin/env python3

import itertools 
import sys
import math
# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12342			
connecting = True
# connect to the server on local computer
s.connect(('192.168.10.124', port))

	

def encryptMessage(msg,key):
	cipher = ""
	k_indx = 0
	msg_len = float(len(msg))
	msg_lst = list(msg)
	key_lst = sorted(list(key))
	col = len(key)
	row = int(math.ceil(msg_len / col))
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)
	matrix = [msg_lst[i: i + col]
		for i in range(0, len(msg_lst), col)]
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx]
			for row in matrix])
		k_indx += 1
	return cipher

while(connecting):
	st = input("Input the string to encrypt: ") 
	key = input("Enter the key: ").lower()
	if (not st.isalpha() or not key.isalpha()):  
		print("Failure")
		sys.exit(1)
	cipher = encryptMessage(st, key) 
	print("Ciphertext: {}".format(cipher))
	s.send(cipher.encode())
	s.send(key.encode())
s.close()
