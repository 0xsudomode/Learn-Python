# Learning python - lession 1
# A simple tcp client : ) 
# use nc -nlv 127.0.0.1 9999 to receive the connection back 

import socket

# define the socket !
host = '127.0.0.1'
port = 9999

# create a socket object 

'''
AF_INET (Address Family - Internet):

    AF_INET represents the address family used for IPv4 (Internet Protocol version 4) addresses.
    It's used when creating a socket that will communicate over the Internet using IPv4.
'''

'''
SOCK_STREAM (Socket Type - Stream):

    SOCK_STREAM represents the socket type for a streaming socket, which provides a reliable, stream-oriented connection.
    It's used when you want to establish a connection that is reliable, ordered, and without data loss. TCP is a stream-oriented protocol, and it is commonly used with SOCK_STREAM.
    
'''
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client.connect((host,port))
    request = "Hello there !"
    
    # Convert the unicode string (text) into a sequence of bytes using the UTF-8 encoding. 
    client.send(request.encode('utf-8'))
    print('sending a get request to localhost ...')
    
    # defining the buffer size that will receive the data 
    data = client.recv(4096)    
    print(data.decode('utf-8'))
except Exception as e:
    print(f"Error : {e}")
finally:
    client.close()
    print("Connection closed.")