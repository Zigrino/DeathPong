import pygame
import globals
import sys
import inputs
import sprites.player, sprites.sword
pygame.init()
WIDTH = globals.window_dimensions[0]
HEIGHT = globals.window_dimensions[1]
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Sprites and stuff


def main():
    input_status = {}
    swords = pygame.sprite.Group()
    player = sprites.player.Player()
    running = True
    while running:
        clock.tick(globals.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #inputs and shit
        input_status = inputs.process_inputs()

        if(input_status["is_shooting"]):
            print("shooting a sword")
            swords.add(sprites.sword.Sword(player))

        #drawing shit
        screen.fill(globals.SCREEN_COLOR)
        player.draw(screen)
        swords.draw(screen)


        #Updates shit 
        pygame.display.update()
if  __name__ == "__main__":
    main()
