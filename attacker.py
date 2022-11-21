import scapy.all as scapy


def build_packet(srcIP, srcPort):
    return scapy.IP(src=srcIP) / scapy.TCP(sport=srcPort)



def send_packet(pkt, dstIP, dstPort):
    pkt.dst = dstIP
    pkt.dport = dstPort
    try:
        scapy.send(pkt)
    except:
        print(Exception)
    return pkt