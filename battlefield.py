from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        pass

fleet = Fleet()
print(fleet.robot[0].robot_attributes())
print(fleet.robot[1].robot_attributes())
print(fleet.robot[2].robot_attributes())


herd = Herd()
print(herd.dinosaur[0].dino_attributes())
print(herd.dinosaur[1].dino_attributes())
print(herd.dinosaur[2].dino_attributes())
