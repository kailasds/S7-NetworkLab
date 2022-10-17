# Import socket module
import socket		

def calcRedundantBits(m):

	 
	for i in range(m):
		if(2**i >= m + i + 1):
			return i

def posRedundantBits(data, r):

	 
	j = 0
	k = 1
	m = len(data)
	res = ''

	 
	for i in range(1, m + r+1):
		if(i == 2**j):
			res = res + '0'
			j += 1
		else:
			res = res + data[-1 * k]
			k += 1

	 
	return res[::-1]


def calcParityBits(arr, r):
	n = len(arr)

	 
	for i in range(r):
		val = 0
		for j in range(1, n + 1):

			 
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])
			 
		arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
	return arr

s = socket.socket()	

# Define the port on which you want to connect
port = 1234	

# connect to the server on local computer
s.connect(('192.168.10.124', port))

 
data = str(input("Enter the data in binary : "))

m = len(data)
r = calcRedundantBits(m)

 
arr = posRedundantBits(data, r)

 
arr = calcParityBits(arr, r)
 

 
print("Data sent to server :",arr)
s.sendto(arr.encode(),('192.168.10.121', 12345))


# receive data from the server
print("Received feedback from server :",s.recv(1024).decode())

# close the connection
s.close()

