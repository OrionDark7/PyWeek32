import pygame
from pygame.math import Vector2

window = pygame.surface.Surface([800, 600])

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([40, 40])
        self.type = str(type)
        self.rect = self.image.get_rect()
        self.rect.topleft = list(pos)
        self.pos = Vector2(pos[0], pos[1])
        self.passed = False
    def message(self, m):
        msg = [self, "wall", str(m)]
        return msg
    def update(self, msgs, action="scroll"):
        if action == "scroll":
            self.pos.y += 0.5
            self.rect.topleft = round(self.pos.x), round(self.pos.y)
            if self.rect.top >= 600 and not self.passed:
                self.passed = True
                msgs.msgs.append(self.message("newwall"))
                self.kill()
                print(self.alive())

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
    def message(self, m):
        msg = [self, "obstacle", str(m)]

class Powerups(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
    def message(self, m):
        msg = [self, "powerup", str(m)]

class Player(pygame.sprite.Sprite):
    def __init__(self, pos=400):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([35, 35])
        self.image.fill([255, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.center = [int(pos), 580]
    def draw(self):
        global window
        window.blit(self.image, self.rect.topleft)
    def message(self, m):
        msg = [self, "player", str(m)]
    def update(self, msgs, action="move"):
        if action == "move":
            if msgs.pos[0] >= 280 and msgs.pos[0] <= 520:
                self.rect.centerx = msgs.pos[0]
            elif msgs.pos[0] > 520:
                self.rect.centerx = 520
            elif msgs.pos[0] < 280:
                self.rect.centerx = 280
