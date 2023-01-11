import pygame
from player import Player
# from comet_event import CometFallEvent
from monster import Monster

# créer une seconde classe qui va représenter notre jeu
class Game:

    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = True
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        # self.comet_event = CometFallEvent()
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie et mettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False


    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie de mon joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'event
        # self.comet_event.update_bar(screen)

        # récupérer les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # recuperer ls cometes
        # for comet in self.comet_event.all_comets:
        #     comet.fall()

        # appliquer l'ensemble des projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer les images des monstres
        self.all_monsters.draw(screen)

        # appliquer les images de mon groupe de comètes
        # self.comet_event.all_comets.draw(screen)

        # si le joueur veut aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)