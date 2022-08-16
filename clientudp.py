#!usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP

udp_host = '192.168.10.124'		# Host IP
udp_port = 12345			        # specified port to connect

msg = "Hello Python!"
print "UDP target IP:", udp_host 
print "UDP target Port:", udp_port

sock.sendto(msg,(udp_host,udp_port))		# Sending message to UDP server
