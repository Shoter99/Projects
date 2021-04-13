import pygame
import os
import sys
import random
import json


def Join(name):
    return os.path.join('Assets', name)


def SaveHighscore():
    with open('data.json', 'w') as f:
        hs = {'highscore': int(highscore)}
        json.dump(hs, f)


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


def DisplayFont():
    if gameActive:
        scoreSurface = gameFont.render(f'{int(score)}', True, BLACK)
        scoreRect = scoreSurface.get_rect(center=(WIDTH-100, 100))
        screen.blit(scoreSurface, scoreRect)
    if not gameActive:
        scoreSurface = gameFont.render(f'Score: {int(score)}', True, BLACK)
        scoreRect = scoreSurface.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(scoreSurface, scoreRect)

        highScoreSurface = gameFont.render(
            f'Highscore: {int(highscore)}', True, BLACK)
        highScoreRect = scoreSurface.get_rect(
            center=(WIDTH/2, HEIGHT/2+50))
        screen.blit(highScoreSurface, highScoreRect)


# cost variables
WIDTH = 1000
HEIGHT = 400


GRAVITY = .9

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ninja Run")
clock = pygame.time.Clock()


# Game variables
gameFont = pygame.font.Font('Karantina-Bold.ttf', 48)

gameSpeed = 8

score = 0
highscore = 0

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
    try:
        highscore = data['highscore']
    except Exception as e:
        highscore = 0
except Exception as e:
    open('data.json', 'x')

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
                score = 0
                pygame.time.set_timer(BUSHSPAWNER, 1200)
        if event.type == BUSHSPAWNER:
            bushList.append(SpawnBush())
            spawn = random.randint(0, 100)
            if(spawn > 65):
                pygame.time.set_timer(BUSHSPAWNER, 800)
            else:
                pygame.time.set_timer(BUSHSPAWNER, 1300)
    screen.fill(WHITE)
    DisplaySky(skySurface)
    DisplayGround()
    DisplayFont()
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
        score += 0.05
        gameActive = CheckForCollisions(bushList)
    else:
        pygame.time.set_timer(BUSHSPAWNER, 0)
        if score > highscore:
            highscore = score
        SaveHighscore()

    OutOfScreen()
    pygame.display.update()
    clock.tick(60)
