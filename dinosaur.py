class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = 35


    def attack_robot(self, robot):
        robot.health = robot.health - (self.attack_power)
        print(f"\n{self.name} attacked {robot.name} for {self.attack_power} damage!\n{robot.name}'s health is now {robot.health}")
        if (robot.health <= 0):
            print(f"\n{robot.name} has been terminated!")