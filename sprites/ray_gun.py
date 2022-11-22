import pygame

class Ray_Gun(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player;
        self.image = pygame.image.load(r"assets/images/Ray_Gun.png")
        self.scale = 0.1
        self.image = pygame.transform.scale(self.image, (584*self.scale, 320*self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.midright
        self.surface = pygame.display.get_surface()
    def draw(self, surface, player):
        self.rect.center = player.rect.midright
        surface.blit(self.image, self.rect)