import pygame 
from player import Player
from monster import Monster
from commet_event import CometFallEvent

#creer une classe game
class Game:

    def __init__(self):
        #definir si notre jeu a commencé 
        self.is_playing = True
        #generer notre Joueur
        self.all_players = pygame.sprite.Group()
        self.player  = Player(self)
        seff.all_players.add(self.player)
        #generer l'evenement
        self.commet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettr le joueur à 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.commet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.commet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        #appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualiser la barre d'event du jeu
        self.commet_event.update_bar(screen)

        self.player.update_animation()

        #recuperer les projectiles du joueur
        for projectile in self.player.all_projetctiles:
            projectile.move()

        #recuperer les monstres de notre jeu
        for monster in self.player.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.animation()

        #recuperer les comètes du jeu
        for comet in self.player.all_comets:
            self.fall()

        #appliquer les images de mon groupe de projectile
        self.player.all_projetctiles.draw(screen)

        #appliquer l'ensemble des images de notre groupe de monstre
        self.all_monsters.draw(screen)

        #appliquer l'ensemble des images de mon groupe de comètes
        self.commet_event.all_comets.draw(screen)


        #verifier si le joueur veut aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0 :
            self.player.move_left()

    def check_collision(self, sprite, group):
            return pygame.sprite.spritecollider(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
            monster = Monster()
            self.all_monsters.add(monster)