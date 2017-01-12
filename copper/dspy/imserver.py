import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

print 'waiting for connection...'

conn, addr = sock.accept()

print 'connected:', addr

while True:
    data = conn.recv(1024)
    if not data:
	break
    print 'data> ', data

conn.close()

print 'connection closed.'