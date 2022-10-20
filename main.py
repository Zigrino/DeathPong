from operator import truediv
import pygame
import globals
import sys
pygame.init()
WIDTH = globals.window_dimensions[0]
HEIGHT = globals.window_dimensions[1]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if  __name__ == "__main__":
    main()