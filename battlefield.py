from turtle import Terminator
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot("Robot")
        self.dinosaur = Dinosaur("Dinosaur", 35)


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    

    def display_welcome(self):
        print('\nWelcome to Robots vs Dinosaurs!\nA fight between flesh and machine!\nOnly one will survive!')
        

    
    def battle_phase(self):
        while(self.robot.health >0 and self.dinosaur.health >0):
            self.robot.attack(self.dinosaur)
            print(self.robot.health, "Terminator's health")
            if(self.dinosaur.healh >0):
                self.dinosaur.attack_power(self.robot)
                print(self.dinosaur.health, "Blue's health")
            else:
                print("The battle has come to an end")
                return True


    
    def display_winner(self):
        if(self.dinosaur.health >0):
            print("Blue is the winner, the Terminator has been terminated!")
        else:
            print("Terminator has made sure the dinosaurs stayed extinct!")
