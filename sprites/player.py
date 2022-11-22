import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/player.png")
        # 32 × 32
        self.scale = 3
        self.image = pygame.transform.scale(self.image, (32*self.scale, 32*self.scale))
        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 300)
        self.speed = 5
        self.is_shooting = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        keys = pygame.key.get_pressed()
        movement = [keys[pygame.K_w], keys[pygame.K_s]]
        if movement[0] and self.rect.topleft[1] - self.speed > 0:
            self.rect.center = (self.rect.center[0], self.rect.center[1] - self.speed)
        elif movement[1] and self.rect.bottomleft[1] - self.speed < 600:
            self.rect.center = (self.rect.center[0], self.rect.center[1] + self.speed)


            
