from battlefield import Battlefield


battlefield = Battlefield()
battlefield.run_game()

print("Game Over")
_________________

from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def display_welcome(self):
        print("Welcome to Robos vs. Dinos")

    def run_game(self):
        self.dinos_turn()
        self.robos_turn()
        self.battle()

    def battle(self):
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaur) > 0:
            self.show.dinos_opps_options()
            self.show.robos_opps_options()

    def dinos_turn(self):
        pass

    def robos_turn(self):
        print("choose the Robot who will attack")
        self.show.robos_opps_options()
        chosen_robot = int(input())
        print ("Choose the dinosaur to defend")
        chosen_dinosaur = int(input())
        self.fleet.robot[chosen_robot].attack(self.herd.dinosaur[chosen_dinosaur])
        if self.herd.dinosaur[chosen_dinosaur].health <= 0:
            print(f"{self.fleet.robot[chosen_robot]} has died")
            self.fleet.robots.remove(self.herd.dinosaur[chosen_dinosaur])

    def dinos_opps_options(self):
        pass

    def robos_opps_options(self):
    dino_index = 0
    for dinos in self.herd.dinosaur:
        print(f"Press {dino_index} for {dino_type}")
        dino_index +=1

def display_winner():
    print("Winner Winner Chicken Dinner, Congratulations: {}")
    if len(self.fleet.robots)>0:
        print("Robots Win")
    else:
        print("DinoS Win")

_________________________________________

class Weapon:
    def __init__(self):
        self.weapon = "blaster"
        self.weapon_power = 86


___________________________________________


from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaur = []
        self.create_herd()

    def create_herd(self):
        pterodactyl = Dinosaur("Pterodactyl")
        tyrannosaurus = Dinosaur("Tyrannosaurus")
        baryonyx = Dinosaur("Baryonyx")
        self.dinosaur.append(pterodactyl)
        self.dinosaur.append(tyrannosaurus)
        self.dinosaur.append(baryonyx)


______________________________________________

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

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.dino_type} attacks {robot} for {self.attack_power} damage. new health is {robot.health}")

    def __int__(self):
        return self.dino_type
_______________________________________________

from weapon import Weapon

weapon = Weapon()


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 81
        self.health = 100
        self.weapon = "blaster"
        self.weapon_power = 86
        self.attack = "galactic blast"

    def robot_attributes(self):
        print(f"My name is {self.name}, my power level is {self.power_level}, my health is at {self.health}"
              f" my weapon is a {self.weapon} and the weapon power is {self.weapon_power}.")

    def attack(self, robot):
        robot.health -= self.weapon_power
        print(f"{self.name} attacks {dino_type} for {self.weapon_power} damage. new health is {dinosaur.health}")

______________________________________________________

from robot import Robot


class Fleet:
    def __init__(self):
        self.robot = []
        self.create_fleet()

    def create_fleet(self):
        battle_droid = Robot("Battle_Droid")
        droideka = Robot("Droideka")
        huyang = Robot("Huyang")
        self.robot.append(battle_droid)
        self.robot.append(droideka)
        self.robot.append(huyang)
