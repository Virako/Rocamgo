import socket

s = socket.socket()
s.connect(('igs.joyjoy.net', 7777))

while True:
    try:
        mensaje = s.recv(4096)
        print mensaje 
        if mensaje == '':
            print "Guest"
            s.send("guest")
            print "Guest"
    except: 
        print "erro der copon"
        s.close()
        break

