import pygame, pytmx
from game import objects

def GenerateWalls(walls):
    w1 = objects.Wall([220, -40], "")
    w2 = objects.Wall([540, -40], "")
    walls.add(w1, w2)

def StartWalls(walls):
    for i in range(15):
        w1 = objects.Wall([220, -40 * (i+1)], "")
        w2 = objects.Wall([540, -40 * (i+1)], "")
        walls.add(w1, w2)
