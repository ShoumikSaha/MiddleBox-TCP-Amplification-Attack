import scapy.all as scapy
import socket

if __name__ == '__main__':
    dstIP = '10.104.18.89'
    srcPort = 8999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((dstIP, srcPort))
    print("socket binded to %s" % (srcPort))
    s.listen(1)
    print("Socket is listening!")
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        break

