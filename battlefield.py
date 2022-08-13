from turtle import Terminator
from dinosaur import Dinosaur
from robot import Robot

robot = Robot("Terminator")
dinosaur = Dinosaur("Blue", 35)



class Battlefield:
    def __init__(self):
        self.robot = Robot("Robot", 30)
        self.dinosaur = Dinosaur("Dinosaur", 35)


    def run_game(self):
        self.display_welcome(self)
        self.battle_phase(self)
        self.display_winner(self)
    

    def display_welcome(self):
        print('\nWelcome to Robots vs Dinosaurs!\nA fight between flesh and machine!\nOnly one will survive!')
        

    
    def battle_phase(self):
        while(robot.health or dinosaur.health >0):
            robot.attack(dinosaur)
            print(robot.health, "Terminator's health")
            if(dinosaur.healh >0):
                dinosaur.attack(robot)
                print(dinosaur.health, "Blue's health")
            else:
                print("The battle has come to an end")
                return True


    
    def display_winner(self):
        if(dinosaur.health >0):
            print("Blue is the winner, the Terminator has been terminated!")
        else:
            print("Terminator has made sure the dinosaurs stayed extinct!")

