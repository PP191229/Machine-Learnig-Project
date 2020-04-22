import keyboard
import pygame
import random
import math
import joblib
from sklearn.svm import SVC

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
    # print(distance)
    if distance < 20:
        return True
    else:
        return False


def ship(x, y):
    screen.blit(shipImag, (round(x), round(y)))


def asteroid(x, y):
    screen.blit(asteroidImag, (round(x), round(y)))


def bomb(x, y):
    screen.blit(bombImag, (x, y))


# predict_data = range(0, 1)

predictor = joblib.load('trained_model.pkl')

bombIsPlanted = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False

    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_LEFT:
    #         shipX_movement = -0.3
    #    if event.key == pygame.K_RIGHT:
    #         shipX_movement = 0.3
    #     if event.key == pygame.K_SPACE:
    #         bombX = shipX
    elements = [shipX, asteroidX, asteroidY, bombX]
    predicted_value = predictor.predict([elements])
    Distance = shipDistance(shipX, asteroidX)
    if Distance:
        bombX = asteroidX
    # key code left = 27, right = 26
    if bombX == asteroidX:
        if predicted_value == 1:
            keyboard.press(27)
            print('Left')
            shipX_movement = -0.3

        elif predicted_value == 0:
            keyboard.press(26)
            print('Right')
            shipX_movement = 0.3
        shipX += shipX_movement
    elif bombX != asteroidX:
        if predicted_value == 0:
            shipX_movement = -0.3
        elif predicted_value == 1:
            shipX_movement = 0.3
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
    pygame.display.update()
