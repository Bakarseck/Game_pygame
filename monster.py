import pygame
import random #faire de l'aléatoire en python
import animation

#self permet de cibler l'objet courant
#Creer une classe qui va gérer la notion de monstre dans notre jeu
class Monster(animation.AnimateSprite):

    #definir le constructeur initiale qui permet de charger les caractériqtiques de base d'une classe
    def __init__(self, game):
        super().__init__("mummy")
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 2 == random.randint(1, 3)
        self.start_animation()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

        #si son nouveau nombre de point de vie est inférieur ou égale à 0
        if self.health <= 0:
            #Réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

            #si la barre d'evenement est chargé à son maximum
            if self.game.commet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)

                #appel de la méthode pour déclencher la pluie de comètes
                self.game.commet_event.attempt_fall()

                #s'il n'y a plus de boule de feu
                if len(self.commet_event.all_comets) == 0:
                    print("L'évenement est fini")
                    #remettre au départ
                    self.commet_event.reset_percent()
                    self.commet_event.fall_mode = False

    def update_health_bar(self, surface):
        #definir une couleur pour notre jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        #definir une couleur pour l'arrière plan de la jauge
        background_bar_color = (60, 63, 60)

        #definir la position de notre jauge vie, sa largeur et son épaisseur
        bar_position = [self.rect.x + 10 , self.rect.y - 20, self.health, 5]

        #definir la position de l'arrière plan de notre jauge de vie
        background_bar_position = [self.rect.x + 10 , self.rect.y - 20, self.max_health, 5]

        #dessiner le background de notr jauge de vie
        pygame.draw.rect(surface, background_bar_color, background_bar_position)

        #dessiner notre barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        #s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players)
            self.rect.x -= self.velocity

        #si le monstre est en collision avec le joueur
        else:
            #infliger des dégats(au joueur)
            self.game.player.damage(self.attack)

    def update_animation(self):
        self.animate(loop=True)