from turtle import *
import sys
import random
import math
import time


'''
try:
    WIDTH, HEIGHT = sys.argv[1], sys.argv[2]
except Exception as e:
    print('Wrong input. Screen size not specified. Correct input "turtleRace <width> <height>"')
    input("Press Enter to exit")
    quit()
'''
WIDTH, HEIGHT = 400, 700
screen = Screen()
screen.setup(WIDTH, HEIGHT)


class Racer():
    def __init__(self, color, name):
        self.racer = Turtle()

        self.color = color
        self.name = name

    def MoveToStartingPos(self, posX, posY):
        self.racer.penup()
        self.racer.color(self.color)
        self.racer.goto(posX, posY)
        self.racer.setheading(90)
        self.racer.pendown()

    def Move(self):
        distance = random.randint(1, 20)
        self.racer.forward(distance)

    def Color(self):
        return self.color

    def __str__(self):
        return self.name


def SpawnRacers(numberOfRacers):
    output = []
    for x in range(numberOfRacers):
        color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        name = f'Racer Nr {x+1}'
        racer = Racer(color, name)
        output.append(racer)
    return output


def SetStartingPoint(racers):
    spaceBetween = WIDTH/(len(racers)+1)
    startingX = -WIDTH/2
    startingY = -HEIGHT/2 + .1*HEIGHT
    for i, racer in enumerate(racers):
        racer.MoveToStartingPos(startingX + spaceBetween*(i+1), startingY)


def Race(racers):
    while True:
        for racer in racers:
            racer.Move()
            x, y = racer.racer.pos()
            if y >= HEIGHT/2 - 10:
                return racer.__str__()


def main():
    screen.colormode(255)
    nRacers = 0
    while nRacers < 2 or nRacers > 10:
        nRacers = int(input("Input the number of racers (2-10)"))

    racers = SpawnRacers(nRacers)
    SetStartingPoint(racers)
    input('Press Enter to start the race')
    winner = Race(racers)
    print(f'The winner is {winner}')


if __name__ == '__main__':
    while True:
        main()
        raceAgain = input("Do you want to race again? (yes/no)")
        if(raceAgain.lower() != 'yes'):
            break
        screen.clear()
