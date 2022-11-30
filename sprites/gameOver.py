import pygame

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.winner = 0
        self.gameover = False
        self.font = pygame.font.Font(r"assets/fonts/gamefont.ttf", 20)
        self.message = f"Player {self.winner} wins!"
        self.image = self.font.render(self.message, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
    def updateWinner(self, w):
        self.winner = w
        self.message = f"Player {w} wins!"
        self.image = self.font.render(self.message, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
        self.gameover = True
    def draw(self, surface):
        if self.gameover:
            surface.blit(self.image, self.rect)
