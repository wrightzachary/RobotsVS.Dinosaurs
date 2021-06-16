from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        # Intro/Setup
        self.display_welcome()

        # Game Rounds
        self.battle()

        # End Game
        self.display_winners()


    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs! Only one side can win!")

    def battle(self):
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0: # while both sides are still alive
            self.dino_turn()
            if len(self.fleet.robots) > 0:
                self.robo_turn()

    def dino_turn(self):
        print("Choose the dinosaur who will attack:")
        self.show_dino_opponent_options()
        chosen_dino = int(input())
        print("Choose the robot who will defend:")
        self.show_robo_opponent_options()
        chosen_robot = int(input())
        self.herd.dinosaurs[chosen_dino].attack(self.fleet.robots[chosen_robot])
        if self.fleet.robots[chosen_robot].health <= 0:
            print(f"{self.fleet.robots[chosen_robot]} has died")
            self.fleet.robots.remove(self.fleet.robots[chosen_robot])
            # self.fleet.robots.pop(chosen_robot)


    def robo_turn(self):
        print("Choose the robot who will attack:")
        self.show_robo_opponent_options()
        chosen_robot = int(input())
        print("Choose the dinosaur who will defend:")
        self.show_dino_opponent_options()
        chosen_dino = int(input())
        self.fleet.robots[chosen_robot].attack(self.herd.dinosaurs[chosen_dino])
        if self.herd.dinosaurs[chosen_dino].health <= 0:
            print(f"{self.herd.dinosaurs[chosen_dino]} has died")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[chosen_dino])


    def show_dino_opponent_options(self):
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f"Press {dino_index} for {dino.type}")
            dino_index += 1

    def show_robo_opponent_options(self):
        robot_index = 0
        for robot in self.fleet.robots:
            print(f"Press {robot_index} for {robot.name}")
            robot_index += 1

    def display_winners(self):
        print("We have a winner!")
        if len(self.fleet.robots) > 0:
            print("Robots win!")
        else:
            print("Dinosaurs win!")
