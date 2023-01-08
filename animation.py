import pygame 

# définir une classe qui va s'occuper des animations
class Animation(pygame.sprite.Sprite):

    #définir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # définir une méthode pour animer le sprite
    def animate(self, loop=False):

        # si l'animation est active
        if self.animation:
            # passer à la suivante
            self.current_image += 1

            # vérifier si on atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0
                
                if loop is False
                    # désactication de l'animation
                    self.animation = False

            # modifier l'image precédente par la suivante
            self.image = self.images[self.current_image]
    

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans dossier correspondant
    images = []
    # récupérer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    for num in range(1, 24):
        image_path = path + str(num) +'.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images

# definir un dictionnaire qui va contenir les images chargées de chaque sprite

# mummy -> [...mummy1.png, ...mummy2.png..., ...]

animations = {
    'mummy' : load_animation_images('mummy'),
    'player' : load_animation_images('player')
}