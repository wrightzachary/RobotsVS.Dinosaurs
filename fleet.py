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
