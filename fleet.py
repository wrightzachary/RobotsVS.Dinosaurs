from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot("Battle Droid", "Blaster", 15)
        robot_two = Robot("Huyang", "Blaster", 10)
        robot_three = Robot("Probe Droid", "Laser Beam", 10)
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)
