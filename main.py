import pygame
from game import objects, map

pygame.init()
pygame.display.init()
window = pygame.display.set_mode([800, 600])
objects.window = window

walls = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
indicators = pygame.sprite.Group()
map.StartWalls(walls, indicators)
player = objects.Player()

class Messages():
    def __init__(self):
        self.msgs = []
        self.pos = [-1, -1]
m = Messages()

pygame.time.set_timer(pygame.USEREVENT, 1000)
screen = "game"
running = True
settings = {"fullscreen":False, "audio":True}
hitobstacle = False

def StartGame():
    global walls, obstacles, player, hitobstacle
    map.StartWalls(walls)
    player = objects.Player()
    hitobstacle = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            m.pos = pygame.mouse.get_pos()

    if screen == "game":
        window.fill([255, 255, 255])
        indicators.update(m)
        walls.update(m)
        walls.draw(window)
        obstacles.update(m)
        obstacles.draw(window)
        player.update(m)
        player.draw()
        for i in m.msgs:
            if i[2] == "newwall":
                map.GenerateWalls(walls, indicators)
            elif i[2] == "newchunk":
                map.GenerateChunk(walls, obstacles, indicators)
            m.msgs.remove(i)

    pygame.display.flip()

pygame.quit()