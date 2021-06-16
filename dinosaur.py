class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.attack_power = attack_power
        self.energy = 100
        self.health = 100

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.type} attacks {robot.name} for {self.attack_power} damage. New health is {robot.health}.")

    def __str__(self):
        return self.type
