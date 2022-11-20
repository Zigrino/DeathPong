import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/player.png")
        self.rect = self.image.get_rect()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        pass
