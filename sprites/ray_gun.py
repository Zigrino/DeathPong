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

class Ray(pygame.sprite.Sprite):
   def __init__(self, player):
       super().__init__()
       self.player = player;
       self.image = pygame.image.load(r"assets/images/Ray_segment.png")
       self.scale = 0.1
       #dimensions = 148x64
       self.image = pygame.transform.scale(self.image, (148*self.scale, 32*self.scale))
       self.rect = self.image.get_rect()
       self.rect.center = (player.rect.midright[0]+10, player.rect.midright[1])
       self.surface = pygame.display.get_surface()
       self.speed = 15
       self.flying = True
   def draw(self, surface):
       surface.blit(self.image, self.rect)
   def update(self):
       if self.rect.center[0] <= 800:
           self.rect.center =  (self.rect.center[0] + self.speed, self.rect.center[1])
       else:
           self.flying = False