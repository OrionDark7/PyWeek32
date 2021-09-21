import pygame, pytmx, random
from game import objects

lastchunk = None

def GenerateChunk(walls, obstacles, indicators):
    global lastchunk
    i = objects.Indicator([380, -40], "nc")
    indicators.add(i)
    if lastchunk == None:
        lastchunk = random.randint(0,0)
    else:
        lastchunk = random.randint(0,0)
    chunk = pytmx.TiledMap("./r/chunks/"+str(lastchunk)+".tmx")
    print(lastchunk)
    for x in range(7):
        for y in range(8):
            prop = chunk.get_tile_properties(x, y, 0)
            if not prop == None:
                if prop['t'] == "obstacle":
                    obstacle = objects.Obstacles([260+(x*40), -240+(y*40)], prop["type"])
                    obstacles.add(obstacle)
                elif prop['t'] == "wall":
                    wall = objects.Wall([260+(x*40), -240+(y*40)], prop["type"])
                    walls.add(wall)

def GenerateWalls(walls, indicators):
    w1 = objects.Wall([220, -40], "wall")
    w2 = objects.Wall([540, -40], "wall")
    i = objects.Indicator([380, -40], "nw")
    walls.add(w1, w2)
    indicators.add(i)

def StartWalls(walls, indicators):
    for i in range(-16,16):
        w1 = objects.Wall([220, 40 * (i+1)], "wall")
        w2 = objects.Wall([540, 40 * (i+1)], "wall")
        i = objects.Indicator([380, -40 * (i+1)], "nw")
        walls.add(w1, w2)
        indicators.add(i)
    i = objects.Indicator([380, -40 * 8], "nc")
    indicators.add(i)
    i = objects.Indicator([380, -40 * 16], "nc")
    indicators.add(i)