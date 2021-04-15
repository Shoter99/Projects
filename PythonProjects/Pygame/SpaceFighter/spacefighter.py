import pygame
import sys
from join import Join
import random
# CONST VARIABLES
WIDTH = 500
HEIGHT = 900

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Background():

    def __init__(self):
        self.bgSurface = pygame.image.load(Join('background.png'))
        self.bgSurface = pygame.transform.scale(
            self.bgSurface, (WIDTH, HEIGHT))
        self.backgroundMovment = 1
        self.backgroundPos = 0

    def DisplayBackground(self):
        screen.blit(self.bgSurface, (0, self.backgroundPos))


class Meteor():

    def __init__(self):
        self.meteorSurface = pygame.image.load(Join('met.png'))
        self.meteorSurface = pygame.transform.scale(
            self.meteorSurface, (int(WIDTH*.1), int(HEIGHT*.1)))
        self.meteorMovment = 1
        self.meteorYPos = 0

    def __del__(self):
        print("Deleted "+str(self))

    def SpawnMeteor(self):
        self.meteorPos = random.randint(20, WIDTH-20)
        self.meteorRect = self.meteorSurface.get_rect(
            center=(self.meteorPos, self.meteorYPos))

    def Display(self):
        screen.blit(self.meteorSurface, self.meteorRect)

    def MoveMeteor(self):
        self.meteorRect.centery += 2.5

    def __str__():
        return "Meteor"


class Fighter():

    def __init__(self):
        self.fighterSurface = pygame.transform.scale(
            pygame.image.load(Join('spacecraft.png')), (int(.2*WIDTH), int(.1*HEIGHT)))
        self.fighterRect = self.fighterSurface.get_rect(
            center=(WIDTH/2, .8*HEIGHT))

    def DisplayFighter(self):
        screen.blit(self.fighterSurface, self.fighterRect)

    def MoveHorizontal(self, direction):
        self.fighterRect.centerx += 4*direction

    def FighterOutOfScreen(self):
        if self.fighterRect.left <= 0:
            self.fighterRect.left = 0
        if self.fighterRect.right >= WIDTH:
            self.fighterRect.right = WIDTH


def DisplayAllMeteors(meteors):
    for meteor in meteors:
        meteor.Display()


def MoveAllMeteors(meteors):
    for meteor in meteors:
        meteor.MoveMeteor()


def OutOfBoundries(meteors):
    for meteor in meteors:
        if(meteor.meteorRect.centery > HEIGHT+15):
            print("Out Of Boundries")
            meteors.remove(meteor)


def CheckForCollisions(meteors, player):
    for meteor in meteors:
        if player.fighterRect.colliderect(meteor.meteorRect):
            return False
    return True
# variables


meteorList = []

SPAWNMETEOR = pygame.USEREVENT
pygame.time.set_timer(SPAWNMETEOR, 1500)


def main():
    bg = Background()
    p1 = Fighter()
    spawnTime = 1500
    gameActive = True
    while True:
        p1.FighterOutOfScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SPAWNMETEOR and gameActive:
                meteor = Meteor()
                meteor.SpawnMeteor()
                meteorList.append(meteor)
                spawnTime -= 0.01
                if spawnTime <= 1200:
                    spawnTime = 1200
                pygame.time.set_timer(SPAWNMETEOR, int(spawnTime))
            if event.type == pygame.KEYDOWN and not gameActive:
                if event.key == pygame.K_SPACE:
                    meteorList.clear()
                    p1.fighterRect.centerx = WIDTH/2
                    gameActive = True
                    pygame.time.set_timer(SPAWNMETEOR, 1500)

        bg.DisplayBackground()
        DisplayAllMeteors(meteorList)
        p1.DisplayFighter()
        if gameActive:
            MoveAllMeteors(meteorList)
            OutOfBoundries(meteorList)
            CheckForCollisions(meteorList, p1)
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                p1.MoveHorizontal(-1)
            if key[pygame.K_d]:
                p1.MoveHorizontal(1)
            gameActive = CheckForCollisions(meteorList, p1)
        else:
            pygame.time.set_timer(SPAWNMETEOR, 0)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
