import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/Temperary_Dude.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = (0, globals.window_dimensions[1]/2)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        pass
