import pandas as pd
import pygame
import random
import math
from openpyxl import Workbook

pygame.init()


screen = pygame.display.set_mode((800, 600))

# Asteroid
asteroidImag = pygame.image.load('meteor.png')
asteroidX = random.randint(0, 800)
asteroidY = random.randint(50, 150)
asteroid_movement = 1

# Player
shipImag = pygame.image.load('battleship.png')
shipX = 360
shipY = 420
shipX_movement = 0

# Bomb
bombImag = pygame.image.load('bomb.png')
bombX = 360
bombY = 484


def collision(bombX, bombY, asteroidX, asteroidY):
    distance = math.sqrt((math.pow(bombX - asteroidX, 2)) + (math.pow(bombY - asteroidY, 2)))
    if distance < 20:
        return True
    else:
        return False


def shipDistance(shipX, asteroidX):
    distance = math.fabs(asteroidX - shipX)
    if distance < 20:
        return True
    else:
        return False


wb = Workbook()
workSheet = wb.active
workSheet.title = "Data"
workSheet['A1'] = "BombX"
workSheet['B1'] = "ShipX"
workSheet['C1'] = "AsteroidX"
workSheet['D1'] = "AsteroidY"
workSheet['E1'] = "Movement Input"


def record_data(position):
    workSheet.append([bombX, shipX, asteroidX, asteroidY, position])
    return position


def ship(x, y):
    screen.blit(shipImag, (round(x), round(y)))


def asteroid(x, y):
    screen.blit(asteroidImag, (round(x), round(y)))


def bomb(x, y):
    screen.blit(bombImag, (x, y))


bombIsPlanted = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Distance = shipDistance(shipX, asteroidX)
    if Distance:
        bombX = asteroidX

    if bombX == asteroidX:
        if asteroidX > 400:
            shipX_movement = -1
            record_data(1)

        elif asteroidX <= 400:
            record_data(0)
            shipX_movement = 1
        shipX += shipX_movement
    elif bombX != asteroidX:
        if shipX > asteroidX:
            shipX_movement = -1
            record_data(1)
        else:
            shipX_movement = 1
            record_data(0)
        shipX += shipX_movement

    Collided = collision(bombX, bombY, asteroidX, asteroidY)
    if Collided:
        asteroidX = random.randint(10, 736)
        asteroidY = -5
        print("Collided")

    asteroidY += asteroid_movement
    if asteroidY >= 800:
        asteroidX = random.randint(64, 736)
        asteroidY = -5

    # shipX += shipX_movement

    if shipX <= 0:
        shipX = 0
    elif shipX >= 736:
        shipX = 736

    screen.fill((0, 0, 0))
    bomb(bombX, bombY)
    asteroid(asteroidX, asteroidY)
    ship(shipX, shipY)
    wb.save("Data2.xlsx")
    pygame.display.update()
