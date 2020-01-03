#! /usr/bin/python

#import sockets & system module
import sys
import socket 
from thread import *

#set IP to loopback, reserve port, and set buffer size
TCP_IP = '127.0.0.1'
TCP_PORT = 8090 
BUFFER_SIZE = 1024

try: 
  # Create AF_INET (IPv4), STREAM TCP socket 
  tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error, e: 
  print 'Error occured while creating socket. Error code: ' + str(e[0]) + ', Error message : ' + e[1]
  sys.exit(); 

#Bind socket to host and port
tcp_socket.bind((TCP_IP, TCP_PORT))
#listening for incoming connection (max queued connection is 10)
tcp_socket.listen(10)
print "Listening..."

#Function for handling connections. Used to create threads
def ClientConnectionHandler(connection): 
  BUFFER_SIZE = 1024
  #send msg to client 
  connection.send('Welcome to the server')
  #keep the thread alive
  while True: 
    #Receive data from client
    data = connection.recv(BUFFER_SIZE)
    reply = 'Data received:' + data
    if not data: 
      break
    connection.sendall(reply)
  #exit loop
  connection.close()

#keep server alive 
while True:
  #Waits for incoming connection (blocking call)
  connection, address = tcp_socket.accept()
  print 'Connected with: ', address
  start_new_thread(ClientConnectionHandler, (connection,))

tcp_socket.close()


