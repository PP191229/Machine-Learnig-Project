import sys
import pygame
from pygame.locals import *


class Asteroid:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.image.get_rect().move(0, self.speed)
        if self.pos.right > 500:
            self.pos.left = 100


class Ship(pygame.sprite.Sprite):
    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image, self.rect = pygame.image.load('spaceship.png').convert()
        selfScreen = pygame.display.get_surface()
        self.area = selfScreen.get_rect()


screen = pygame.display.set_mode((900, 900))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

asteroid = pygame.image.load('asteroid.png').convert()
ship = pygame.image.load('spaceship.png').convert()

screen.blit(background, (0, 0))
objects = []

for x in range(10):
    o = Asteroid(asteroid, x * 400, x)
    objects.append(o)

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(100)
