import pygame
from pygame.math import Vector2

window = pygame.surface.Surface([800, 600])

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, type="wall"):
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
        if self.passed:
            self.kill()
        if action == "scroll":
            self.pos.y += 0.25
            self.rect.topleft = round(self.pos.x), round(self.pos.y)
            if self.rect.top >= 600 and not self.passed:
                self.passed = True
                self.kill()

class Indicator(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([40, 40])
        self.rect = self.image.get_rect()
        self.rect.topleft = list(pos)
        self.pos = Vector2(pos[0], pos[1])
        self.passed = False
        self.type = str(type)
    def message(self, m):
        msg = [self, "wall", str(m)]
        return msg
    def update(self, msgs, action="scroll"):
        if self.passed:
            self.kill()
        if action == "scroll":
            self.pos.y += 0.25
            self.rect.topleft = round(self.pos.x), round(self.pos.y)
            if self.rect.top >= 600 and not self.passed:
                self.passed = True
                if self.type == "nw":
                    msgs.msgs.append(self.message("newwall"))
                elif self.type == "nc":
                    msgs.msgs.append(self.message("newchunk"))
                self.kill()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./r/images/obstacles/"+str(type)+".png")
        self.rect = self.image.get_rect()
        self.rect.topleft = list(pos)
        self.passed = False
        self.pos = Vector2(pos[0], pos[1])
    def message(self, m):
        msg = [self, "obstacle", str(m)]
    def update(self, msgs, action="scroll"):
        if self.passed:
            self.kill()
        if action == "scroll":
            self.pos.y += 0.25
            self.rect.topleft = round(self.pos.x), round(self.pos.y)
            if self.rect.top >= 600 and not self.passed:
                self.passed = True
                self.kill()

class Powerups(pygame.sprite.Sprite):
    def __init__(self, pos, type, amount):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./r/images/powerups/"+str(type)+".png")
        self.rect = self.image.get_rect()
        self.rect.topleft = list(pos)
        self.pos = Vector2(self.rect.left, self.rect.top)
        self.type = str(type)
        self.amount = float(amount)
        self.passed = False
    def message(self, m):
        msg = [self, "powerup", str(m)]
    def update(self, msgs, player, action="scroll"):
        if self.passed:
            self.kill()
        if action == "scroll":
            self.pos.y += 0.25
            self.rect.topleft = round(self.pos.x), round(self.pos.y)
            if self.rect.top >= 600 and not self.passed:
                self.passed = True
                self.kill()


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
