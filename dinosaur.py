class Dinosaur:
    def __init__(self, dinosaur_type, health, energy_level, attack_power):
        self.dinosaur_type = dinosaur_type
        self.health = health
        self.energy_level = energy_level
        self.attack_power = attack_power
        print(f"The dinosaur is a {dinosaur_type}!")
        print(f"Dinosaur health is {health}")
        print(f"Dinosaur energy level is {energy_level}")
        print(f"Dinosaur attack power is {attack_power}")
