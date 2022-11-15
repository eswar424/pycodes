import socket

s=socket.socket()
print("socket sucessfully created")
port=40674
s.bind(("",port))
print("socket binded to %s"%(port))
s.listen(5)
print("socket is listen")
while True:
	c,addr=s.accept()
	print('got connection from',addr)
	c.send(B'THANKNYOU FOR CONNECTION')
	c.close()