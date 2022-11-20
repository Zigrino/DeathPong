import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/Temporary_Dude.png")
        # 11000 × 11000
        self.scale = 0.1
        self.image = pygame.transform.scale(self.image, (11000*self.scale, 11000*self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 300)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        pass
