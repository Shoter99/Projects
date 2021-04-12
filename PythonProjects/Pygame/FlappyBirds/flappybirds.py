import pygame
import sys
import os
import time
import random
import math
import json
# CONST VARIABLES
WIDTH = 1024
HEIGHT = 1024

GRAVITY = .25


def Join(name):
    return os.path.join('assets', name)


def DrawFloor():
    screen.blit(floorSurface, (floor_x_pos, HEIGHT*.9))
    screen.blit(floorSurface, (floor_x_pos+WIDTH, HEIGHT*.9))


def Jump():
    global birdMovment, birdRect
    birdMovment = 0
    birdMovment -= 8


def SpawnPipe():
    gapBetweenPipes = random.randint(100, 150)
    gapPos = random.randint(200, HEIGHT-300)
    downPipe = pipeSurface.get_rect(
        midtop=(WIDTH, math.floor(gapPos+gapBetweenPipes)))
    upPipe = pipeSurface.get_rect(midbottom=(
        WIDTH, math.floor(gapPos-gapBetweenPipes)))
    pipes = (upPipe, downPipe)
    return pipes


def MovePipes(pipeList):
    for pipe in pipeList:
        pipe.centerx -= 6
    return pipeList


def DrawPipes(pipes):
    for i, pipe in enumerate(pipes):
        if(i % 2 != 0):
            screen.blit(pipeSurface, pipe)
        else:
            screen.blit(UpPipeSurface, pipe)


def CheckCollisions(pipes):
    for pipe in pipes:
        if birdRect.colliderect(pipe):
            return False
    global HEIGHT, birdMovment
    if birdRect.centery >= HEIGHT*.9 or birdRect.centery < 0:
        return False
    return True


def RotateBird(bird):
    newBird = pygame.transform.rotate(bird, -birdMovment*3)
    return newBird


def DisplayFont():
    if gameActive:
        scoreSurface = gameFont.render(f'{int(score)}', True, (255, 255, 255))
        scoreRect = scoreSurface.get_rect(center=(WIDTH/2, 100))
        screen.blit(scoreSurface, scoreRect)
    else:
        scoreSurface = gameFont.render(
            f'Score: {int(score)}', True, (255, 255, 255))
        scoreRect = scoreSurface.get_rect(center=(WIDTH/2, 100))
        screen.blit(scoreSurface, scoreRect)

        highScoreSurface = gameFont.render(
            f'Highscore: {int(highscore)}', True, (255, 255, 255))
        highScoreRect = highScoreSurface.get_rect(center=(WIDTH/2, 800))
        screen.blit(highScoreSurface, highScoreRect)

        RestartSurface = gameFont.render(
            'Click space to restart', True, (255, 255, 255))
        RestartRect = RestartSurface.get_rect(center=(WIDTH/2, 350))
        screen.blit(RestartSurface, RestartRect)


def DrawBackground():
    if score < 20:
        screen.blit(bgSurface, (0, 0))
    else:
        screen.blit(bgNightSurface, (0, 0))


def SaveHighscore():
    with open('data.json', 'w') as f:
        hs = {'highscore': int(highscore)}
        json.dump(hs, f)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Game variables
gameActive = False
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
    open('data.json', 'a')


gameFont = pygame.font.Font('LondrinaSolid-Light.ttf', 62)
# loading background image and scaling it 2x
bgSurface = pygame.image.load(Join('background-day.png')).convert()
bgSurface = pygame.transform.scale(bgSurface, (WIDTH, HEIGHT))

bgNightSurface = pygame.image.load(Join('background-night.png')).convert()
bgNightSurface = pygame.transform.scale(bgNightSurface, (WIDTH, HEIGHT))
# loading floor image and scaling it 2x
floorSurface = pygame.image.load(Join('base.png')).convert()
floorSurface = pygame.transform.scale(floorSurface, (WIDTH, 300))

floor_x_pos = 0

# loading bird image and creating rect around it for collisions
birdSurface = pygame.image.load(Join('bluebird-midflap.png')).convert()
birdSurface = pygame.transform.scale2x(birdSurface)
birdRect = birdSurface.get_rect(center=(100, HEIGHT/2))
birdMovment = 0

# loading pipe image
pipeSurface = pygame.image.load(Join('pipe-green.png'))
pipeSurface = pygame.transform.scale(pipeSurface, (100, HEIGHT))
UpPipeSurface = pygame.transform.rotate(pipeSurface, 180)
pipeList = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SaveHighscore()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Jump()
            if event.key == pygame.K_SPACE and gameActive == False:
                gameActive = True
                pipeList.clear()
                birdRect.y = HEIGHT/2
                birdMovment = 0
                score = 0
        if event.type == SPAWNPIPE:
            upPipe, downPipe = SpawnPipe()
            pipeList.append(upPipe)
            pipeList.append(downPipe)

    # draw background
    DrawBackground()

    if gameActive:
        # Bird
        birdRotated = RotateBird(birdSurface)
        screen.blit(birdRotated, birdRect)
        birdMovment += GRAVITY
        birdRect.centery += birdMovment
        CheckCollisions(pipeList)

        # Pipes
        pipeList = MovePipes(pipeList)
        DrawPipes(pipeList)
        gameActive = CheckCollisions(pipeList)

        score += 0.01
        DisplayFont()
    else:
        if score > highscore:
            highscore = score
        DisplayFont()
    # Floor
    floor_x_pos -= 1
    DrawFloor()
    if(floor_x_pos == -WIDTH):
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(60)
