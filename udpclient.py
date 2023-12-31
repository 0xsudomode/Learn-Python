# IMPORTANT !!!!!!!!! ---> make sure to run nc -lnvup (-u for udp mode)
# (sudo permission is needed else nc won't receive anything)

import socket 

# Define socket 
host = '127.0.0.1'
port = 9999

# Create a socket object 
# Since this is a UDP-based client, we must specify a datagram socket 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    data = b'This is a data test to receive data over UDP :)\r\n'
    client.sendto(data, ((host, port)))
    print('Data sent ...')

    # Receive data and sender's address
    received_data, sender_address = client.recvfrom(4096)

    print(f"Received from {sender_address}: {received_data.decode('utf-8')}")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
    print('Connection closed.')
