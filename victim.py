import scapy.all as scapy
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import util

class Victim()

  def __init__(self, victim):
    self.victim = victim

  def run(self):
    received_packet_count = 0
    while True:
        # listen for packets coming to the victim
        p = scapy.sniff(filter=victim.sniff_filter(), count=0, timeout=3)
    
        if p != None:
            print("Victim received packet. PAYLOAD: " + p[0]['RAW'].load)

            # the packet came from this actor
            pktSrc = util.Actor.from_packet_source (p)

            # respond to these packets with RST packet
            received_packet_count += 1
            pkt = util.send_packet (src=self.victim, dst=pktSrc, 
                                    flags='R',
                                    payload="VICTIM: I'VE RECEIVED " + str(received_packet_count) + " PACKETS. STOP SENDING!")



import config

if __name__ == '__main__':
  victim = Victim(victim=config.victim)
  victim.run()
