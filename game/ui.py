import pygame

pygame.font.init()

font = pygame.font.Font(None, 24)
color = [0, 0, 0]
window = pygame.surface.Surface([800, 600])

def Font(size, c=None):
    font = pygame.font.Font(None, size)
    if not c == None:
        color = list(c)

def Box(pos, dim, c=False):
    global color, window
    surface = pygame.surface.Surface(list(dim))
    surface.set_alpha(128)
    if c:
        window.blit(surface, [pos[0]-(dim[0]/2), pos[1]-(dim[1]/2)])
    else:
        window.blit(surface, pos)

def Text(t, pos, c=False):
    global color, window
    text = font.render(str(t), 1, color)
    if c:
        rect = text.get_rect()
        window.blit(text, [pos[0]-rect.width/2, pos[1]-rect.height/2])
    else:
        window.blit(text, pos)

class Button(pygame.sprite.Sprite):
    def __init__(self, text, pos, c=False, ncolor=None):
        global font, color
        if ncolor == None:
            self.image = font.render(str(text), 1, color)
        else:
            self.image = font.render(str(text), 1, ncolor)
        self.rect = self.image.get_rect()
        if c:
            self.rect.center = list(pos)
        else:
            self.rect.topleft = list(pos)
        self.text = str(text)
        self.newimage = pygame.surface.Surface([self.rect.width+4, self.rect.height+4])
        self.newimage.fill([0, 0, 0])
        self.newimage.blit(self.image, [2,2])
        self.image = self.newimage
        self.image.set_alpha(255)
    def update(self, m):
        pass