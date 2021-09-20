import pygame

window = pygame.display.set_mode([800, 600])
screen = "game"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if screen == "game":
        window.fill([255, 255, 255])

    pygame.display.flip()

pygame.quit()