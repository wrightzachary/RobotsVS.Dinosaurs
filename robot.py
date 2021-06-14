from weapon import Weapon

weapon = Weapon()


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 81
        self.health = 100
        self.weapon = "blaster"
        self.weapon_power = 86

    def robot_attributes(self):
        print(f"My name is {self.name}, my power level is {self.power_level}, my health is at {self.health}"
              f" my weapon is a {self.weapon} and the weapon power is {self.weapon_power}.")
