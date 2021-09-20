import pygame
from game import objects, map

pygame.init()
pygame.display.init()
window = pygame.display.set_mode([800, 600])
objects.window = window

walls = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
map.walls = walls
map.obstacles = obstacles
map.StartWalls()
msgs = []

pygame.time.set_timer(pygame.USEREVENT, 1000)
screen = "game"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if screen == "game":
        window.fill([255, 255, 255])
        walls.update()
        walls.draw(window)
        obstacles.draw(window)
        print(objects.msgs)
        for i in objects.msgs:
            hitwall = False
            if i[2] == "newwall" and not hitwall:
                map.GenerateWalls()
                i[0].remove(walls)
                hiwtall = True
            objects.msgs.remove(i)

    pygame.display.flip()

pygame.quit()