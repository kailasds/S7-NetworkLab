# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12345			
connecting = True
# connect to the server on local computer
s.connect(('192.168.10.124', port))
while(connecting):
	
	
	# receive data from the server and decoding to get the string.

	num = str(input('Input a number(enter q to quit) '))
	if(num=='q'):
		connecting = False
	s.send(num.encode())
	print s.recv(1024).decode()
	# close the connection
s.close()	
	

