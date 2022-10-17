#!/usr/bin/env python3

import itertools 
import sys
import math

# first of all import the socket library
import socket			

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")


port = 12342			

s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")		


c, addr = s.accept()
print ('Got connection from', addr )


def decryptMessage(cipher,key):
	
	msg = ""
	k_indx = 0
	msg_indx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)
	col = len(key)
	row = int(math.ceil(msg_len / col))
	key_lst = sorted(list(key))
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1
	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot","handle repeating words.")
	null_count = msg.count('_')
	if null_count > 0:
		return msg[: -null_count]
	return msg

while True:
	cipher = c.recv(1024).decode()
	key= c.recv(1024).decode()
	print("Ciphertext: {}".format(cipher))
	plain = decryptMessage(cipher, key)
	print("Plaintext: {}".format(plain))
c.close()
