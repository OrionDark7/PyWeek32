import pygame, pytmx
from game import objects

def GenerateWalls(walls, indicators):
    w1 = objects.Wall([220, -40], "")
    w2 = objects.Wall([540, -40], "")
    i = objects.Indicator([380, -40])
    walls.add(w1, w2)
    indicators.add(i)

def StartWalls(walls, indicators):
    for i in range(16):
        w1 = objects.Wall([220, -40 * (i+1)], "")
        w2 = objects.Wall([540, -40 * (i+1)], "")
        i = objects.Indicator([380, -40 * (i+1)])
        walls.add(w1, w2)
        indicators.add(i)
