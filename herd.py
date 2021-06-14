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
