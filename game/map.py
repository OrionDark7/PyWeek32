import pygame, pytmx
from game import objects

walls = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

def GenerateWalls():
    global walls, obstacles
    w1 = objects.Wall([220, -40], "")
    w2 = objects.Wall([540, -40], "")
    walls.add(w1, w2)

def StartWalls():
    global walls, obstacles
    for i in range(15):
        w1 = objects.Wall([220, -40 * (i+1)], "")
        w2 = objects.Wall([540, -40 * (i+1)], "")
        walls.add(w1, w2)
