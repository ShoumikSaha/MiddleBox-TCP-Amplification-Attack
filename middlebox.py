import scapy.all as scapy
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Middlebox():

  def __init__(self, forbidden):
    self.forbidden = forbidden

  def run(self):
    while True:
        # listen for packets being sent to the forbidden site
        p = scapy.sniff(filter=forbidden.sniff_filter(), count=0, timeout=5)

        if p != None:
            print("Middlebox sniffed packet. PAYLOAD: " + p[0]['RAW'].load)

            # the packet came from this actor
            pktSrc = util.Actor.from_packet_source (p)

            # send a packet back to the source, "WEBSITE BLOCKED"
            pkt = util.send_packet (src=forbidden, dst=pktSrc, 
                                    flags='SA',
                                    payload="MIDDLEBOX: WEBSITE BLOCKED")

import config

if __name__ == '__main__':
  middlebox = Middlebox(forbidden=config.forbidden)
  middlebox.run()
