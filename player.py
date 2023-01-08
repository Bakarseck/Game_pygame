import pygame
from projectile import Projectile
import animation


#creer une classe Joueur qui va heriter de Sprite
#Un sprite est un element graphique dans notre jeu
#Player hérite de sprite
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        #recuperer sa position
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

     def update_health_bar(self, surface):
        #definir une couleur pour notre jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        #definir une couleur pour l'arrière plan de la jauge
        background_bar_color = (60, 63, 60)

        #definir la position de notre jauge vie, sa largeur et son épaisseur
        bar_position = [self.rect.x + 50 , self.rect.y + 20, self.health, 7]

        #definir la position de l'arrière plan de notre jauge de vie
        background_bar_position = [self.rect.x + 50 , self.rect.y + 20, self.max_health, 7]

        #dessiner le background de notr jauge de vie
        pygame.draw.rect(surface, background_bar_color, background_bar_position)

        #dessiner notre barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        #créer une nouvelle instance de la classe projectile
        self.all_projetctiles.add(Projectile(self))
        # demarrer l'animation 
        self.start_animation()

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.y -= self.velocity