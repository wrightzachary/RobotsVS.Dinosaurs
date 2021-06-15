class Dinosaur:
    def __init__(self, dino_type):
        self.dino_type = dino_type
        self.health = 100
        self.energy_level = 100
        self.attack_power = 80
        self.attack = "sonic_roar"

    def dino_attributes(self):
        print(f"I am a {self.dino_type}, my health is {self.health}, my energy is at {self.energy_level},"
              f" and my attack power is {self.attack_power}.")
