"""
Shima Iraniparast, Tino Nyakurerwa
"""

# Import socket module
from socket import * 
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = input(' Input lower case sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print('From server: ', modifiedSentence.decode())
clientSocket.close()

# Python TCP Client A

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = raw_input("tcpClientA: Enter message/ Enter exit:") 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE)     
    data = tcpClientA.recv(BUFFER_SIZE)
    print " Client2 received data:", data
    MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientA.close() 

