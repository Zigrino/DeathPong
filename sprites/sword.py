import pygame

class Sword(pygame.sprite.Sprite):
    def __init__(self, player, pn):
        super().__init__()
        self.pn = pn
        self.player = player;
        self.image_list = [pygame.image.load(r"assets/images/Sword.png"), pygame.image.load(r"assets/images/Bloody_Sword.png")]
        self.scale = 0.1
        #Original image dimensions = 448x448
        self.image = self.image_list[0]
        self.image = pygame.transform.scale(self.image, (448*self.scale, 448*self.scale))
        if pn == 1:
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.midright = self.player.rect.midleft
        else:
            self.rect = self.image.get_rect()
            self.rect.midleft = self.player.rect.midright
        self.surface = pygame.display.get_surface()
        self.speed = 5
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
        
class Sword_Held(pygame.sprite.Sprite):
    def __init__(self, player, pn):
        super().__init__()
        self.player = player
        self.pn = pn
        self.image = pygame.image.load(r"assets/images/Sword.png")
        self.scale = 0.1
        self.image = pygame.transform.scale(self.image, (448*self.scale, 448*self.scale))

        if pn == 1:
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.midright = self.player.rect.midleft
        else:
            self.rect = self.image.get_rect()
            self.rect.midleft = self.player.rect.midright

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        if self.pn == 1:
            self.rect.midright = self.player.rect.midleft
        else:
            self.rect.midleft = self.player.rect.midright
