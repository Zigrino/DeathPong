import pygame

class Launcher(pygame.sprite.Sprite):
    def __init__(self, player, pn):
        super().__init__()
        self.pn = pn
        self.player = player;
        self.full = pygame.transform.scale(pygame.image.load(r"assets/images/Rocket_Launcher.png"), (1328*0.07, 527*0.07))
        self.empty = pygame.transform.scale(pygame.image.load(r"assets/images/Rocket_Launcher_Empty.png"), (1060*0.07, 527*0.07))
        self.image = self.full
        self.is_full = True
        self.rect = self.image.get_rect()
        if self.pn == 0:
            self.rect.center = (self.player.rect.midright[0] + 20, self.player.rect.midright[1])
        else:
            self.rect.center = (self.player.rect.midleft[0] - 20, self.player.rect.midleft[1])
            self.image = pygame.transform.flip(self.image, True, False)
        self.surface = pygame.display.get_surface()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        if self.is_full:
            self.image = self.full
        else:
            self.image = self.empty
        if self.pn == 0:
            self.rect.center = (self.player.rect.midright[0] + 20, self.player.rect.midright[1])
        else:
            self.rect.center = (self.player.rect.midleft[0] - 20, self.player.rect.midleft[1])
            self.image = pygame.transform.flip(self.image, True, False)

class Rocket(pygame.sprite.Sprite):
   def __init__(self, player, pn):
       super().__init__()
       self.pn = pn
       self.player = player;
       self.image = pygame.image.load(r"assets/images/Rocket.png")
       self.scale = 0.05
       self.image = pygame.transform.scale(self.image, (1172*self.scale, 384*self.scale))
       self.rect = self.image.get_rect()
       if self.pn == 0:
           self.rect.center = (player.rect.midright[0]+10, player.rect.midright[1])
       else:
           self.rect.center = (player.rect.midleft[0] - 10, player.rect.midleft[1])
           self.image = pygame.transform.flip(self.image, True, False)
       self.surface = pygame.display.get_surface()
       self.speed = 10
       self.chase = 3
       self.flying = True
   def draw(self, surface):
       surface.blit(self.image, self.rect)
   def update(self, player_y):
       if self.rect.center[0] <= 800 and self.rect.center[0] >= 0:
           if self.pn == 0:
               self.rect.center =  (self.rect.center[0] + self.speed, self.rect.center[1])
           else:
               self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
       else:
           self.flying = False
           self.kill()
       if player_y > self.rect.center[1]:
           self.rect.center = (self.rect.center[0], self.rect.center[1]+self.chase)
       elif player_y < self.rect.center[1]:
           self.rect.center = (self.rect.center[0], self.rect.center[1]-self.chase)
