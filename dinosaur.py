class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power


    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"\n{self.name} attacked {robot.name} for {self.attack_power} damage!\n{robot.name}'s health is now {robot.health}")
        if (robot.health <= 0):
            print(f"\n{robot.name} has been terminated!")