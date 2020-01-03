#! /usr/bin/python

#import sockets & system module
import socket 
import sys

#set IP to loopback, set port set buffer size
TCP_IP = '127.0.0.1'
TCP_PORT = 8090
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = "Hello, World!"

try: 
  # Create AF_INET (IPv4), STREAM TCP socket 
  tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error, e: 
  print 'Error occured while creating socket. Error code: ' + str (e[0]) + ', Error message : ' + e[1]
  sys.exit(); 

tcp_socket.connect((TCP_IP, TCP_PORT)) 

#send message
try: 
  tcp_socket.send(MESSAGE_TO_SERVER)
except socket.error, e: 
  print 'Error occured while sending data to server. Error code: ' + str(e[0]) + ', Error message: ' + e[1]
  sys.exit() 

print 'Message to the server send successfully' 
data = tcp_socket.recv(BUFFER_SIZE)
tcp_socket.close()
print "Response from server: ", data

#tcp_socket.bin((TCP_IP, TCP_PORT))


