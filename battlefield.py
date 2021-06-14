from fleet import Fleet
from herd import Herd

team = "Robos"


class Battlefield:
    def __init__(self, run_game):
        self.run_game = run_game
        print("Welcome to Robos vs. Dinos")
        self.team_selection = input("What team would you like to join?")
        print(input)
        if input == team:
            print("Hope you enjoy extinction like the dinosaurs!")
        else:
            print("Welcome to the Robos!")

    def battle(self):
        pass

    def dinos_turn(self):
        pass

    def robos_turn(self):
        pass

    def dinos_opps_options(self):
        herd = Herd()
        herd.dinosaur[0].dino_attributes()
        herd.dinosaur[1].dino_attributes()
        herd.dinosaur[2].dino_attributes()

    def robos_opps_options(self):
        fleet = Fleet()
        fleet.robot[0].robot_attributes()
        fleet.robot[1].robot_attributes()
        fleet.robot[2].robot_attributes()


def winner_winner():
    print("Winner Winner Chicken Dinner, Congratulations: {}")
