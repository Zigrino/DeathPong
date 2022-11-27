import pygame
import time, random
class Player(pygame.sprite.Sprite):
    def __init__(self, startpos, playnum):
        super().__init__()
        if playnum == 0:
            self.image = pygame.image.load(r"assets/images/player.png")
        else:
            self.image = pygame.image.load(r"assets/images/player.png")
        # 32 × 32
        self.scale = 3
        self.image = pygame.transform.scale(self.image, (32*self.scale, 32*self.scale))
        self.rect = self.image.get_rect()
        self.pn = playnum
        if playnum == 1:
            self.rect.midright = startpos
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.rect.midleft = startpos
        self.speed = 5
        self.is_shooting = False
        self.swap_weapon = False
        self.time_to_swap = random.randint(3, 12)
        self.time_since_swapped = 0
        self.last_time_swapped = time.time()
        self.can_shoot = False
        self.health = 20
        self.alive = True
    def update_health(self, num):
        self.health -= num
        if self.health <= 0:
            self.alive = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        keys = pygame.key.get_pressed()
        self.time_since_swapped = time.time()-self.last_time_swapped
        if self.time_since_swapped >= self.time_to_swap:
            self.swap_weapon = True
            self.time_to_swap = random.randint(3, 8)
            self.last_time_swapped = time.time()
            self.time_since_swapped = 0
        
        
        if self.pn == 0:
            movement = [keys[pygame.K_w], keys[pygame.K_s]]
        else:
            movement = [keys[pygame.K_UP], keys[pygame.K_DOWN]]
        if movement[0] and self.rect.topleft[1] - self.speed > 0:
            self.rect.center = (self.rect.center[0], self.rect.center[1] - self.speed)
        elif movement[1] and self.rect.bottomleft[1] - self.speed < 600:
            self.rect.center = (self.rect.center[0], self.rect.center[1] + self.speed)


            
