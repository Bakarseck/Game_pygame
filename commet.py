import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, commet_event):
        super().__init__()
        #définir l'image associée à cette comette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.commet_event = commet_event

    def remove(self):
        self.commet_event.all_comets.remove(self)


        #si le nombre de comètes est de 0 ;
        if len(self.commet_event.all_comets) == 0:
            print("L'évenement est fini")
            #remettre la barre à 0
            self.commet_event.reset_percent()
            # apparaitre les 2 premiers monstres
            self.commet_event.game.spawn_monster()
            self.commet_event.game.spawn_monster()
            self.commet_event.game.spawn_monster()


    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol 
        if self.rect.y >= 500:
            #retirer la boule de feu
            self.remove()

        #si la boule touche le joueur
        if self.commet_event.game.check_collision(
            self, self.commet_event.game.all_players()
        ):
            print("Joueur Touché !")
            #retirer la boule de feu
            self.commet_event.game.player.damage(20)
        