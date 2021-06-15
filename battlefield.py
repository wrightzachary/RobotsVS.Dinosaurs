from fleet import Fleet
from herd import Herd


herd = Herd()
fleet = Fleet()
response = "play"


class Battlefield:
    def __init__(self, run_game):
        self.run_game = run_game
        print("Welcome to Robos vs. Dinos")
        print('')
        input("Type play to start!")
        if response == "play":
            print("Please see below for the teams")
            print('')
            print("Team Dinos")
            self.dino_team = herd.dinosaur[0].dino_attributes()
            self.dino_team = herd.dinosaur[1].dino_attributes()
            self.dino_team = herd.dinosaur[2].dino_attributes()
            print('')
            print("Team Robos")
            self.robo_team = fleet.robot[0].robot_attributes()
            self.robo_team = fleet.robot[1].robot_attributes()
            self.robo_team = fleet.robot[2].robot_attributes()

    def battle(self):
        pass

    def dinos_turn(self):
        pass

    def robos_turn(self):
        pass

    def dinos_opps_options(self):
        pass

    def robos_opps_options(self):
        pass


def winner_winner():
    print("Winner Winner Chicken Dinner, Congratulations: {}")
