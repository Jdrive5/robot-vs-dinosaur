from weapon import Weapon

weapon = Weapon

class Robot:
    def __init__(self, name,):
        self.name = name 
        self.health = 100
        self.weapon = Weapon("Needle", 30)


    def attack_dinosaur(self, dinosaur):
        dinosaur.healh = dinosaur.health - self.weapon.attack_power
        print(f"\n{self.name} attacked {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage!\n{dinosaur.name}'s health is now {dinosaur.health}")
        if (dinosaur.health <= 0):
            print(f"\n{dinosaur.name} has been slayed!")
