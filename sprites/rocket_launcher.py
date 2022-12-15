import pygame, math

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
       self.base_image = pygame.image.load(r"assets/images/Rocket.png")
       self.explosions = [pygame.image.load(r"assets/images/exp1_.png"), pygame.image.load(r"assets/images/exp2_.png"), pygame.image.load(r"assets/images/exp3_.png"), pygame.image.load(r"assets/images/exp4_.png"), pygame.image.load(r"assets/images/exp5_.png")]
       self.scale = 0.05
       self.image = pygame.transform.scale(self.image, (1172*self.scale, 384*self.scale))
       self.base_image = pygame.transform.scale(self.base_image, (1172*self.scale, 384*self.scale))
       self.rect = self.image.get_rect()
       if self.pn == 0:
           self.rect.center = (player.rect.midright[0]+10, player.rect.midright[1])
       else:
           self.rect.center = (player.rect.midleft[0] - 10, player.rect.midleft[1])
           self.image = pygame.transform.flip(self.image, True, False)
           self.base_image = pygame.transform.flip(self.image, True, False)
       self.surface = pygame.display.get_surface()
       self.speed = 10
       self.chase = 3
       self.flying = True
       self.exploding = False
       self.dealing_damage = False
       self.velocity = [0,0]
   def draw(self, surface):
       surface.blit(self.image, self.rect)


   def update(self, player_y):
       
       if self.rect.right <= 800 and self.rect.left >= 0 and not self.dealing_damage:
           if self.pn == 0:
               self.rect.center =  (self.rect.center[0] + self.speed, self.rect.center[1])
               self.velocity[0] = self.speed #for rotation
           else:
               self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
               self.velocity[0] = -self.speed # for rotation
       else:
           self.exploding = True
           self.dealing_damage = True

       if player_y > self.rect.center[1] + 3 and not self.exploding:
           self.rect.center = (self.rect.center[0], self.rect.center[1]+self.chase)
           self.velocity[1] = self.chase # for rotation
       elif player_y < self.rect.center[1] - 3 and not self.exploding:
           self.rect.center = (self.rect.center[0], self.rect.center[1]-self.chase)
           self.velocity[1] = -self.chase # for rotation
       else:
           self.velocity[1] = 0

        
        #rotation
       if not self.exploding:
            angle = (math.atan2(self.velocity[0], self.velocity[1]) * 180.0 / math.pi) + 270
            self.image = pygame.transform.rotate(self.base_image, angle)
            self.rect = self.image.get_rect(center = self.rect.center)