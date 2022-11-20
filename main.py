import pygame
import global_vars
import sys
import inputs
import sprites.player, sprites.sword
pygame.init()
WIDTH = global_vars.window_dimensions[0]
HEIGHT = global_vars.window_dimensions[1]
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Sprites and stuff


def main():
    input_status = {}
    swords = pygame.sprite.Group()
    player = sprites.player.Player()
    running = True
    while running:
        clock.tick(global_vars.FPS)
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
        screen.fill(global_vars.SCREEN_COLOR)
        player.draw(screen)
        swords.draw(screen)


        #Updates shit 
        pygame.display.update()
        player.update()
        swords.update()
if  __name__ == "__main__":
    main()
