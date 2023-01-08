import pygame
import math
from game import Game
pygame.init()

#generer la fenetre de notre jeu
pygame.diplay.set_caption("Commet fall Game")
screen = pygame.diplay.set_mode((1080, 720))

#importer et charger l'image
background = pygame.image.load('assets/bg.jpg')

#importer et charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer et charger notre bouton
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


#charger notre Game
game = Game()

running = True

#boucle tant que running vraie
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        #déclencher les instructions de la partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencé
    else:
        #ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # coordonnées x du joueur game.player.rect.x 

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fênêtre
    for event in pygame.event.get():
        #verifier que l'evenement est fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du Jeu") 
        #Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est appuyé

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif envent.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le button play
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                game.start()