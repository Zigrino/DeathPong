import pygame

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, pn):
        super().__init__()
        self.pn = pn
        self.player = player;
        self.image = pygame.image.load(r"assets/images/Gun.png")
        self.scale = 0.04
        self.image = pygame.transform.scale(self.image, (1299*self.scale, 752*self.scale))
        if self.pn == 1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        if self.pn == 0:
            self.rect.center = (self.player.rect.midright[0] + 5, self.player.rect.midright[1])
        else:
            self.rect.center = (self.player.rect.midleft[0] - 5, self.player.rect.midleft[1])
        self.surface = pygame.display.get_surface()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        if self.pn == 0:
            self.rect.center = (self.player.rect.midright[0] + 5, self.player.rect.midright[1])
        else:
            self.rect.center = (self.player.rect.midleft[0] - 5, self.player.rect.midleft[1])

class Bullet(pygame.sprite.Sprite):
   def __init__(self, player, pn):
       super().__init__()
       self.pn = pn
       self.player = player;
       self.image = pygame.image.load(r"assets/images/Bullet.png")
       self.scale = 0.04
       #dimensions = 438x329
       self.image = pygame.transform.scale(self.image, (438*self.scale, 329*self.scale))
       self.rect = self.image.get_rect()
       if self.pn == 0:
           self.rect.center = (player.rect.midright[0]+10, player.rect.midright[1])
       else:
           self.rect.center = (player.rect.midleft[0] - 10, player.rect.midleft[1])
           self.image = pygame.transform.flip(self.image, True, False)
       self.surface = pygame.display.get_surface()
       self.speed = 40
       self.flying = True
   def draw(self, surface):
       surface.blit(self.image, self.rect)
   def update(self):
       if self.rect.center[0] <= 800 and self.rect.center[0] >= 0:
           if self.pn == 0:
               self.rect.center =  (self.rect.center[0] + self.speed, self.rect.center[1])
           else:
               self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])

       else:
           self.flying = False
           self.kill()
