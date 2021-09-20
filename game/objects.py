import pygame
from pygame.math import Vector2

window = pygame.surface.Surface([800, 600])
msgs = []

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([40, 40])
        self.type = str(type)
        self.rect = self.image.get_rect()
        self.rect.topleft = list(pos)
        self.pos = Vector2(pos[0], pos[1])
    def message(self, m):
        msg = [self, "wall", str(m)]
        return msg
    def update(self, action="scroll"):
        global msgs
        if action == "scroll":
            self.pos.y += 0.5
            self.rect.topleft = round(self.pos.x), round(self.pos.y)
            if self.rect.top >= 600:

                msgs.append(self.message("newwall"))
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
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
    def message(self, m):
        msg = [self, "player", str(m)]