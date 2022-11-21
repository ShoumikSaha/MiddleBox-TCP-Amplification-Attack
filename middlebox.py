import scapy.all as scapy
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

middleBoxIP = '10.104.18.90'
middleBoxPort = 7000
forbiddenIP = 'www.twitter.com'

p = scapy.sniff(filter="dst host " + forbiddenIP + " and tcp port 80", count=1)
print(p.summary())
print(p[0]['IP'].src)
srcIP = p[0]['IP'].src
srcPort = p[0]['TCP'].sport

pkt = scapy.IP(src=middleBoxIP, dst=srcIP)/scapy.TCP(flags="SA", sport=middleBoxPort, dport=srcPort)
scapy.send(pkt)
print(pkt.summary())

while True:
    p = scapy.sniff(filter="dst host " + middleBoxIP + " and tcp port " + str(middleBoxPort), count=0, timeout=5)
    print(p.summary())
    try:
        srcIP = p[0]['IP'].src
        srcPort = p[0]['TCP'].sport

        pkt = scapy.IP(src=middleBoxIP, dst=srcIP) / scapy.TCP(flags="SA", dport=srcPort, sport=middleBoxPort)
        scapy.send(pkt)
    except:
        print(Exception)
        continue