import pygame

pygame.font.init()

font = pygame.font.Font(None, 24)
color = [0, 0, 0]
window = pygame.surface.Surface([800, 600])

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