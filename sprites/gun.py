import pygame

class Gun(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player;
        self.image = pygame.image.load(r"assets/images/Gun.png")
        self.scale = 0.08
        self.image = pygame.transform.scale(self.image, (1299*self.scale, 752*self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.midright
        self.surface = pygame.display.get_surface()
    def draw(self, surface, player):
        self.rect.center = player.rect.midright
        surface.blit(self.image, self.rect)

class Bullet(pygame.sprite.Sprite):
   def __init__(self, player):
       super().__init__()
       self.player = player;
       self.image = pygame.image.load(r"assets/images/Bullet.png")
       self.scale = 0.1
       #dimensions = 438x329
       self.image = pygame.transform.scale(self.image, (438*self.scale, 329*self.scale))
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
           self.kill()
