import pygame
import random


# créer une classe qui représente le monstre
class Monster(pygame.sprite.Sprite):

    # créer le constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # Infliger les dégats
        self.health -= amount

        # vérifier si nouveau nombre de points de vie est inférieur à 0
        if self.health <= 0:
            # Réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # dessiner notre background de vie (gris)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10 , self.rect.y - 20, self.max_health, 5])
        # dessiner notre barre de vie (vert clair)
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10 , self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que s'il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision
        else:
            # Infliger des dégats (au joueur)
            self.game.player.damage(self.attack)
