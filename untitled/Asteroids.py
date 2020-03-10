import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Asteroid
asteroidImag = pygame.image.load('meteor.png')
asteroidX = random.randint(0, 800)
asteroidY = random.randint(50, 150)
asteroid_movement = 0.05

# Player
shipImag = pygame.image.load('battleship.png')
shipX = 360
shipY = 420
shipX_movement = 0


def ship(x, y):
    screen.blit(shipImag, (x, y))


def asteroid(x, y):
    screen.blit(asteroidImag, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shipX_movement = -0.3
            if event.key == pygame.K_RIGHT:
                shipX_movement = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shipX_movement = 0

    asteroidY += asteroid_movement
    if asteroidY >= 800:
        asteroidX = random.randint(10, 790)
        asteroidY = -5

    shipX += shipX_movement

    if shipX <= 0:
        shipX = 0
    elif shipX >= 736:
        shipX = 736

    asteroid(asteroidX, asteroidY)
    ship(shipX, shipY)
    pygame.display.update()
