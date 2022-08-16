# first of all import the socket library
import socket			

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345			

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("socket is listening")		

# a forever loop until we interrupt it or
# an error occurs
c, addr = s.accept()
print ('Got connection from', addr )
while True:

# Establish connection with client.
	num = c.recv(1024).decode()
	if(num=='q'):
		break
	num = int(num)
	if(num%2==0):
		print(num, 'is an Even number')
		c.send('Even number'.encode())
	else:
		print(num, 'is an Odd number')
		c.send('Odd number'.encode())

# Close the connection with the client
c.close()

# Breaking once connection closed
	
	
