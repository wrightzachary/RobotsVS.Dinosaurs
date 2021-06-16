from weapon import Weapon


class Robot:
    def __init__(self, name, weapon_type, weapon_attack_power):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon(weapon_type, weapon_attack_power)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacks {dinosaur.type} with {self.weapon.type} for {self.weapon.attack_power} damage. New health is {dinosaur.health}.")


    def __str__(self):
        return self.name
