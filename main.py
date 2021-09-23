import pygame, random
from game import objects, map, ui

pygame.init()
pygame.display.init()
window = pygame.display.set_mode([800, 600])
objects.window = window
ui.window = window

walls = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
indicators = pygame.sprite.Group()
map.StartWalls(walls, indicators)
player = objects.Player()

class Messages():
    def __init__(self):
        self.msgs = []
        self.pos = [-1, -1]
        self.speed = 0.25
m = Messages()

pygame.time.set_timer(pygame.USEREVENT, 50)
screen = "game"
running = True
settings = {"fullscreen":False, "audio":True}
hitobstacle = False
obstacledifficulty = {"obstacle":0}
obstacle = {}
words = [["gonna", "school", "safe", "today"]]

def StartGame():
    global walls, obstacles, player, hitobstacle
    map.StartWalls(walls)
    player = objects.Player()
    hitobstacle = False

def CreateObstacle(d, o):
    global words
    if d == 0:
        obstacle["type"] = "typing"
        obstacle["puzzle"] = random.choice(words[d])
        obstacle["tile"] = o

def DrawGroups():
    global player, walls, obstacles, window
    player.draw()
    walls.draw(window)
    obstacles.draw(window)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            m.pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen == "game":
                obstacles.update(m, "click")
                if len(m.msgs) > 0:
                    for i in m.msgs:
                        if i[2] == "click":
                            hitobstacle = True
                            CreateObstacle(obstacledifficulty[i[0].type], i[0])
                            pygame.time.set_timer(pygame.USEREVENT, 50)
                            break
        elif event.type == pygame.KEYDOWN:
            if screen == "game":
                if event.key == pygame.KEYDOWN:
                    screen = "paused"
                if hitobstacle == True:
                    if obstacle["type"] == "typing":
                        key = pygame.key.name(event.key)
                        if obstacle["puzzle"][0] == key:
                            obstacle["puzzle"] = obstacle["puzzle"][1:len(obstacle["puzzle"])]
                            if len(obstacle["puzzle"]) == 0:
                                hitobstacle = None
                                obstacle["tile"].kill()
                                obstacle = {}
        elif event.type == pygame.USEREVENT:
            if hitobstacle and m.speed > 0:
                m.speed -= 0.012
            elif hitobstacle == None and m.speed < 0.25:
                m.speed += 0.012
            if m.speed <= 0:
                m.speed = 0
            if m.speed >= 0.25:
                m.speed = m.speed
                if hitobstacle == None:
                    hitobstacle = False

    if screen == "game":
        window.fill([255, 255, 255])
        DrawGroups()
        indicators.update(m)
        walls.update(m)
        obstacles.update(m)
        player.update(m)
        for i in m.msgs:
            if i[2] == "newwall":
                map.GenerateWalls(walls, indicators)
            elif i[2] == "newchunk":
                map.GenerateChunk(walls, obstacles, indicators)
            m.msgs.remove(i)
        if hitobstacle:
            ui.color = [0, 0, 0]
            ui.Box([400, 300], [300, 500], c=True)
            ui.color = [255, 255, 255]
            ui.Text("obstacle", [400, 80], True)
            if obstacle["type"] == "typing":
                ui.Text(obstacle["puzzle"], [400, 300], True)
    elif screen == "paused":
        window.fill([255, 255, 255])
        DrawGroups()
    pygame.display.flip()

pygame.quit()