import pygame
import os
import sys
import random


def Join(name):
    return os.path.join('Assets', name)


def DisplaySky(surface):
    screen.blit(surface, (sky_x_pos, 0))
    screen.blit(surface, (sky_x_pos+WIDTH/2, 0))
    screen.blit(surface, (sky_x_pos+WIDTH, 0))


def DisplayGround():
    screen.blit(groundSurface, (sky_x_pos, 320))
    screen.blit(groundSurface, (sky_x_pos+WIDTH/2, 320))
    screen.blit(groundSurface, (sky_x_pos+WIDTH, 320))


def SpawnBush():

    newBush = bushSurface.get_rect(center=(WIDTH, 335))
    collideBush = pygame.rect.Rect((0, 0), (15, 40))
    collideBush.midbottom = newBush.midbottom
    return collideBush, newBush


def DisplayBushes(bushes):
    for bush in bushes:
        colBush, bushPos = bush
        screen.blit(bushSurface, bushPos)


def MoveBushes(bushes):
    for bush in bushes:
        colBush, bushPos = bush
        colBush.x -= gameSpeed
        bushPos.x -= gameSpeed


def CheckForCollisions(bushes):
    for bush in bushes:
        colBush, bushPos = bush
        if playerRect.colliderect(colBush):
            return False
    return True


def OutOfScreen():
    global bushList
    for bush in bushList:
        colBush, bushPos = bush
        if colBush.x < -15:
            bushList.remove(bush)


# cost variables
WIDTH = 1000
HEIGHT = 400


GRAVITY = .9

WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ninja Run")
clock = pygame.time.Clock()

# Game variables
gameSpeed = 8

# importing skysurface
skySurface = pygame.image.load(Join('sky.png'))
skySurface = pygame.transform.scale(skySurface, (int(WIDTH/2), 80))
sky_x_pos = 0

# importing ground surface
groundSurface = pygame.image.load(Join('ground.png'))
groundSurface = pygame.transform.scale(groundSurface, ((int(WIDTH/2)), 80))

#import obstacles
bushSurface = pygame.image.load(Join('bush.png'))
bushSurface = pygame.transform.scale(bushSurface, (60, 60))
bushList = []

# importing Player image and setting Player's variables
playerSurface = pygame.image.load(Join('player.png'))
playerSurface = pygame.transform.scale(playerSurface, (45, 135))
playerMovment = 0
playerRect = playerSurface.get_rect(center=(150, 310))
canJump = True

gameActive = False

BUSHSPAWNER = pygame.USEREVENT
pygame.time.set_timer(BUSHSPAWNER, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and canJump:
                playerMovment = -15
                canJump = False
            if event.key == pygame.K_SPACE and not gameActive:
                bushList.clear()
                sky_x_pos = 0
                gameSpeed = 5
                gameActive = True
                pygame.time.set_timer(BUSHSPAWNER, 1200)
        if event.type == BUSHSPAWNER:
            bushList.append(SpawnBush())
            bushSpawnTime = random.randint(800, 1200)
            pygame.time.set_timer(BUSHSPAWNER, bushSpawnTime)
    screen.fill(WHITE)
    DisplaySky(skySurface)
    DisplayGround()
    screen.blit(playerSurface, playerRect)
    DisplayBushes(bushList)
    if gameActive:
        MoveBushes(bushList)
        playerMovment += GRAVITY
        playerRect.centery += playerMovment
        if(playerRect.y >= 245):
            playerMovment = 0
            canJump = True
        sky_x_pos -= gameSpeed
        if sky_x_pos <= -WIDTH/2:
            sky_x_pos = 0
        gameSpeed += 0.002
        gameActive = CheckForCollisions(bushList)
    else:
        pygame.time.set_timer(BUSHSPAWNER, 0)
    OutOfScreen()
    pygame.display.update()
    clock.tick(60)
