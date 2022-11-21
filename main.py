# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#import scapy
import scapy.all as scapy
from warnings import filterwarnings
import socket

from attacker import build_packet, send_packet
#from victim import recv_packet
#from victim_new import receive

import warnings



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    victimIP = '10.104.18.91'
    victimPort = 5000

    srcIP = victimIP
    srcPort = victimPort
    packet = build_packet(srcIP, srcPort)
    #packet = scapy.IP(dst='www.google.com')/scapy.TCP()
    print(packet.summary())

    forbiddenIP = 'www.twitter.com'

    dstIP = forbiddenIP
    #dstIP = '10.104.18.90'
    dstPort = 80
    packet = send_packet(packet, dstIP, dstPort)
    print(packet.show())
    print(packet.summary())

    #s = recv_packet(srcIP, 8989)
    #s.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
