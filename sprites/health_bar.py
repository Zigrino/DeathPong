import pygame

class Health_Bar(pygame.sprite.Sprite):
    def __init__(self, player, pn):
        super().__init__()
        self.pn = pn
        self.player = player
        self.total_health = self.player.health
        self.scale = 0.04
    def draw(self, window):
        if self.pn == 0:
            pygame.draw.rect(window, (255,0,0), (0, 0, 200, 25))
            pygame.draw.rect(window, (5,255,10), (0, 0, (200-(200/self.total_health)*(self.total_health-self.player.health)), 25))
        else:
            pygame.draw.rect(window, (255,0,0), (600, 0, 800, 25))
            pygame.draw.rect(window, (5,255,10), (600+(200/self.total_health)*(self.total_health-self.player.health), 0, 800, 25))