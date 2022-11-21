import scapy.all as scapy
import warnings
warnings.filterwarnings("ignore", category=Warning)

class Actor:
  def __init__(self, ip, port):
      self.ip = ip
      self.port = port

  # get the Actor who is the source of this packet
  def from_packet_source (pkt):
      return Actor (pkt[0]['IP'].src, pkt[0]['TCP'].sport)

  # get the sniffing filter for this Actor
  def sniff_filter (self):
      return ("dst host " + self.ip + " and tcp port " + str(self.port))




# send a packet between two Actors, with given flags and payload
def send_packet(src, dst, flags="", payload=""):
    packet = None
    if flags == "":
        packet = scapy.IP(src=src.ip, dst=dst.ip) / scapy.TCP(sport=src.port, dport=dst.port) / scapy.Raw(load=payload)
    else:
        packet = scapy.IP(src=src.ip, dst=dst.ip) / scapy.TCP(flags=flags, sport=src.port, dport=dst.port) / scapy.Raw(load=payload)
    try:
        scapy.send(packet)
    except:
        print(Exception)
    return packet

