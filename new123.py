import socket
import sys
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("socket is created")
except socket.error as err:
	print("socket creation failed with error %s"%(err))
port =80
try:
	host_ip=socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("there is error in resloving host")
	sys.exit()
s.connect((host_ip,port))
print("sucuss")