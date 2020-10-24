import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640,480))
screen.fill(255)
pygame.draw.rect(screen, 0,(0.33*width,0,1,height),2)