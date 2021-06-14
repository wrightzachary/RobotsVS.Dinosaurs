from fleet import Fleet
from herd import Herd


fleet = Fleet()
fleet.robot[0].robot_attributes()
fleet.robot[1].robot_attributes()
fleet.robot[2].robot_attributes()


herd = Herd()
herd.dinosaur[0].dino_attributes()
herd.dinosaur[1].dino_attributes()
herd.dinosaur[2].dino_attributes()


class Battlefield:
    def __init__(self, run_game):
        self.run_game = run_game
        # self.player = input("Which team would you like to use")
        print("Welcome to Robos vs. Dinos")

#     def battle(self):
#         pass
#
#     def dinos_turn(self):
#         pass
#
#     def robos_turn(self):
#         pass
#
#     def dinos_opps_options(self):
#         pass
#
#     def robos_opps_options(self):
#         pass
#
#
# def winner_winner():
#     print("Winner Winner Chicken Dinner, Congratulations: {}")
