import pygame

class Sword(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player;
        self.image_list = [pygame.image.load(r"assets/images/Sword.png"), pygame.image.load(r"assets/images/Bloody_Sword.png")]
        self.scale = 0.1
        #Original image dimensions = 448x448
        self.image = self.image_list[0]
        self.image = pygame.transform.scale(self.image, (448*self.scale, 448*self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        self.surface = pygame.display.get_surface()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        pass
        

