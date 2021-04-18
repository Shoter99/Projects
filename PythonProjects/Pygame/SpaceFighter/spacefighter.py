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
pygame.display.set_caption('Space Fighter')


class Background:

    def __init__(self):
        self.bgSurface = pygame.image.load(Join('background.png'))
        self.bgSurface = pygame.transform.scale(
            self.bgSurface, (WIDTH, HEIGHT))
        self.backgroundMovment = 1
        self.backgroundPos = 0

    def DisplayBackground(self):
        screen.blit(self.bgSurface, (0, self.backgroundPos))


class Meteor:

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

    def MoveMeteor(self, speed):
        self.meteorRect.centery += speed

    def __str__(self):
        return "Meteor"


class Fighter:

    def __init__(self):
        self.fighterSurface = pygame.transform.scale(
            pygame.image.load(Join('spacecraft.png')), (int(.2*WIDTH), int(.1*HEIGHT)))
        self.fighterRect = self.fighterSurface.get_rect(
            center=(WIDTH/2, .8*HEIGHT))
        self.speed = 7
        self.fighterColliderRect = pygame.rect.Rect((5, 0), (5, 5))

    def DisplayFighter(self):
        screen.blit(self.fighterSurface, self.fighterRect)

    def MoveHorizontal(self, direction):
        self.fighterRect.centerx += self.speed*direction
        self.fighterColliderRect.topleft = self.fighterRect.center

    def FighterOutOfScreen(self):
        if self.fighterRect.left <= 0:
            self.fighterRect.left = 0
        if self.fighterRect.right >= WIDTH:
            self.fighterRect.right = WIDTH


def DisplayAllMeteors(meteors):
    for meteor in meteors:
        meteor.Display()


def MoveAllMeteors(meteors, meteorSpeed):
    for meteor in meteors:
        meteor.MoveMeteor(meteorSpeed)


def OutOfBoundaries(meteors):
    global meteorSpeed
    for meteor in meteors:
        if meteor.meteorRect.centery > HEIGHT+15:
            print("Out Of Boundaries")
            meteors.remove(meteor)
            meteorSpeed += .05


def CheckForCollisions(meteors, player):
    for meteor in meteors:
        if player.fighterColliderRect.colliderect(meteor.meteorRect):
            return False
    return True


def DisplayFont(gameActive):
    if gameActive:
        scoreSurface = gameFont.render(f'{int(score)}', True, (255, 255, 255))
        scoreRect = scoreSurface.get_rect(center=(WIDTH/2, 100))
        screen.blit(scoreSurface, scoreRect)
    else:
        scoreSurface = title_gameFont.render(
            f'Score: {int(score)}', True, (255, 255, 255))
        scoreRect = scoreSurface.get_rect(center=(WIDTH/2, (HEIGHT/2-100)))
        screen.blit(scoreSurface, scoreRect)

        high_scoreSurface = title_gameFont.render(
            f'Highscore: {int(highscore)}', True, (255, 255, 255))
        high_scoreRect = high_scoreSurface.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(high_scoreSurface, high_scoreRect)


# variables
# Font
gameFont = pygame.font.Font('ZenDots-Regular.ttf', 62)
title_gameFont = pygame.font.Font('ZenDots-Regular.ttf', 42)
score = 0
highscore = 0

meteorList = []
meteorSpeed = 2.5

SPAWNMETEOR = pygame.USEREVENT
pygame.time.set_timer(SPAWNMETEOR, 1500)


def main():
    global score
    bg = Background()
    p1 = Fighter()
    spawnTime = 1500
    gameActive = False
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
                spawnTime -= 0.03
                if spawnTime <= 100:
                    spawnTime = 100
                pygame.time.set_timer(SPAWNMETEOR, int(spawnTime))
            if event.type == pygame.KEYDOWN and not gameActive:
                if event.key == pygame.K_SPACE:
                    meteorList.clear()
                    score = 0
                    p1.fighterRect.centerx = WIDTH/2
                    gameActive = True
                    pygame.time.set_timer(SPAWNMETEOR, 1500)

        bg.DisplayBackground()
        DisplayAllMeteors(meteorList)
        p1.DisplayFighter()
        DisplayFont(gameActive)
        if gameActive:
            MoveAllMeteors(meteorList, meteorSpeed)
            OutOfBoundaries(meteorList)
            CheckForCollisions(meteorList, p1)
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                p1.MoveHorizontal(-1)
            if key[pygame.K_d]:
                p1.MoveHorizontal(1)
            gameActive = CheckForCollisions(meteorList, p1)
            score += .0167
        else:
            DisplayFont(gameActive)
            pygame.time.set_timer(SPAWNMETEOR, 0)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
