from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur("Tyrannosaurus rex", 15)
        dino_two = Dinosaur("Allosaurus", 10)
        dino_three = Dinosaur("Archaeopteryx", 15)
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
