class Weapon:
    def __init__(self, type, attack_power):
        self.type = type
        self.attack_power = attack_power

    def __str__(self):
        return self.type
