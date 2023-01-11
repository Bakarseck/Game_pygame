import pygame
pygame.init()

# créer la fenêtre de jeu
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygamon - Aventure")

# boucle du jeu
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
