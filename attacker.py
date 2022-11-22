import util

class Attacker:

    def __init__(self, victim, forbidden):
        self.victim = victim
        self.forbidden = forbidden
  
    def attack(self):
        # send a single packet to the forbidden site to trigger the attack
        packet = util.send_packet(src=self.victim, dst=self.forbidden, 
                                  payload="ATTACKER: HERE'S THE MIDDLEBOX TRIGGER")

        print(packet.summary())


import config

if __name__ == '__main__':
    attacker = Attacker(victim=config.victim, forbidden=config.forbidden)
    attacker.attack()
