import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

asteroid = pygame.image.load('asteroid.png').convert()
# Player
shipImag = pygame.image.load('battleship.png')
shipX = 360
shipY = 420
shipX_movement = 0


def ship(x, y):
    screen.blit(shipImag, (x, y))


while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, K_ESCAPE):
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shipX_movement = -0.3
            if event.key == pygame.K_RIGHT:
                shipX_movement = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shipX_movement = 0

    shipX += shipX_movement

    if shipX <= 0:
        shipX = 0
    elif shipX >= 736:
        shipX = 736

    ship(shipX, shipY)
    pygame.display.update()
