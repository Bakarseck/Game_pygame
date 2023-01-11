import pygame
from projectile import Projectile

# Un sprite, un élement graphique qui peut se déplacer
# créer une classe pour représenter le joueur
class Player(pygame.sprite.Sprite):

    # Un constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
    
    def damage(self, amount):
        # si le joueur peut perdre
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()
            

    def update_health_bar(self, surface):
        # dessiner notre background de vie (gris)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50 , self.rect.y + 20, self.max_health, 5])
        # dessiner notre barre de vie (vert clair)
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50 , self.rect.y + 20, self.health, 7])
    
    def launch_projectile(self):
        # creer une nouvelle instance de projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity