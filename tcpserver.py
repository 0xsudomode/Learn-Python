# creating a simple python server 
import socket 

def startserver(host,port):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    '''
    So, the bind method is essentially saying, "I want this server to listen for incoming connections on IP address '127.0.0.1' and port 9999." This way, when clients connect to this address and port, the server can accept those connections. If you don't call bind, the operating system will assign a random port, and you won't have control over which port your server is using.
    '''
    server.bind((host,port))
    
    '''
    When a client attempts to connect to the server, the server can accept the connection and add it to a queue. If there are more connection requests than the backlog value, additional connection attempts may be refused. The exact behavior can depend on the operating system.
    '''
    server.listen(5)
    print(f'[+] Server started and listening on :{host}:{[port]}')
    
    while True:
        '''
         you call server.accept(), it returns a new socket object (client) representing the connection to the client. This client socket object is an instance of the socket class from the socket module. You then use this client socket object to communicate with the connected client by sending and receiving data.
        '''
        client,client_address = server.accept()
        print(f'[+] Accepted connection from : {client_address}')
        welcome = 'Welcome to the tcp server !'
        client.sendall(welcome.encode())
        
        while True:
            data = client.recv(1024)
            if not data :
                break
            message = data.decode()
            print(f'[+] Recieved data from {client_address} : \r\n {message}')
            #client.sendall(data) -> if you want to echo back the data to the client
        print(f"Connection with {client_address} closed.")
        client.close()
            
'''
When a Python script is run, the Python interpreter sets a special built-in variable called __name__ to the string '__main__'. This means that if the script is being run as the main program, the condition if __name__ == '__main__': will be True.

Imported Module: If the script is imported as a module into another script, the __name__ variable is set to the name of the module (not '__main__'). In this case, the condition if __name__ == '__main__': will be False.
'''
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999
    startserver(host,port)