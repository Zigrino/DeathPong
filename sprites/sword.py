import pygame

class Sword(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player;
        self.image_list = [pygame.image.load(r"assets/images/Sword.png"), pygame.image.load(r"assets/images/Bloody_Sword.png")]
        self.scale = 0.5
        #Original image dimensions = 448x448
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.midleft = player.rect.midright
        self.surface = pygame.display.get_surface()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        pass
        

