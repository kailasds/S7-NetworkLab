# import the socket library
import socket

def detectError(arr, nr):
	n = len(arr)
	res = 0

	 
	for i in range(nr):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])

	 

		res = res + val*(10**i)

	 
	return int(str(res), 2)
def calcRedundantBits(m):

	 
	for i in range(m):
		if(2**i >= m + i + 1):
			return i
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 1234

s.bind(('', port))
print("socket binded to %s" % (port))
# put the socket into listening mode
s.listen(5)
print("socket is listening")


while True:
	# Establish connection with client.
	c, addr = s.accept()
	print('Got connection from', addr)

	# Get data from client
	data = c.recv(1024)

	print("Received data :", data.decode())

	if not data:
		break

	 
 
	arr = '00101001110'
	m = len(data)
	r = calcRedundantBits(m)
	print("Error Data is " + arr)
	correction = detectError(arr, r)
	if(correction==0):
		c.sendto(("No errors found in data :)").encode(), ('192.168.10.121', 12345))
	else:
		temp=len(arr)-correction+1
		st="The position of error is "+str(temp)
		st=st+" from the left"
		c.sendto((st).encode(), ('192.168.10.121', 12345))

	 

	c.close()

