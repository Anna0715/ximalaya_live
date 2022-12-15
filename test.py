# import socket
# r = socket.gethostbyname(socket.gethostname())
# print(r)
from netifaces import interfaces, ifaddresses, AF_INET
addresses=[]
for name in interfaces():
    addresses = [i['addr'] for i in ifaddresses(name).setdefault(AF_INET, [{'addr':'No IP '}] )]
print(' '.join(addresses))