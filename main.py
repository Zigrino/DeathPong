import pygame
import global_vars
import sys
import inputs
import sprites.player, sprites.sword
from sprites.ray_gun import Ray_Gun

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
    ray_gun = Ray_Gun(player)
    running = True
    ray_on = False
    while running:
        clock.tick(global_vars.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #inputs and shit
        input_status = inputs.process_inputs()
        if(input_status["is_shooting"] and player.can_shoot and not ray_on):
            swords.add(sprites.sword.Sword(player))
            player.can_shoot = False
            player.is_shooting = True
        swordcount = 0
        for sword in swords:
            if sword.flying:
                swordcount += 1
        if swordcount > 0:
            player.can_shoot = False
        else:
            player.can_shoot = True
        if input_status["ray_gun"]:
            ray_on = True

        #drawing shit
        screen.fill(global_vars.SCREEN_COLOR)
        player.draw(screen)
        swords.draw(screen)
        if ray_on:
            ray_gun.draw(screen, player)


        #Updates shit 
        pygame.display.update()
        player.update()
        swords.update()
if  __name__ == "__main__":
    main()
