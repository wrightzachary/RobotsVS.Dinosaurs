class Dinosaur:
    def __init__(self, dino_type):
        self.dino_type = dino_type
        self.health_level = 85
        self.energy_level = 100
        self.attack_power = 80

    def dino_attributes(self):
        print(f"I am a {self.dino_type}, my health is {self.health_level}, my energy is at {self.energy_level},"
              f" and my attack power is {self.attack_power}.")
