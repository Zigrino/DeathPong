import pygame
import global_vars
import sys
import inputs
import sprites.player, sprites.sword
from sprites.ray_gun import Ray_Gun, Ray

pygame.init()
WIDTH = global_vars.window_dimensions[0]
HEIGHT = global_vars.window_dimensions[1]
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Sprites and stuff


def main():
    def weaponHandler(weapon):
        if weapon=="sword":
            #Managing swords
            swordcount = 0
            for sword in swords:
                if sword.flying:
                    swordcount += 1
            if swordcount > 0:
                player.can_shoot = False
            else:
                player.can_shoot = True
        elif weapon=="raygun":
            raycount = 0
            for ray in rays:
                if ray.flying:
                    raycount += 1
            if raycount < 7:
                player.can_shoot = True
            else:
                player.can_shoot = False

    input_status = {}
    swords = pygame.sprite.Group()
    rays = pygame.sprite.Group()
    player = sprites.player.Player()
    ray_gun = Ray_Gun(player)
    running = True
    weapon = "sword"
    while running:
        clock.tick(global_vars.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #inputs and shit
        input_status = inputs.process_inputs()
        if input_status["ray_gun"] and weapon != "raygun":
            player.can_shoot = True; #sets can shoot to true to stop it from being stuck as false if sword is in the air dumbass
            weapon = "raygun"
        #HELL YES SHOOTING THINGS IS COOL GUNS GO BOOM AMERICA WOOOOOOOOOO
        weaponHandler(weapon)
        if(input_status["is_shooting"] and player.can_shoot and weapon == "sword"):
            swords.add(sprites.sword.Sword(player))
            player.can_shoot = False
        elif(input_status["is_shooting"] and player.can_shoot and weapon == "raygun"):
            rays.add(Ray(player))

        #drawing shit
        screen.fill(global_vars.SCREEN_COLOR)
        player.draw(screen)
        swords.draw(screen)
        rays.draw(screen)
        if weapon == "raygun":
            ray_gun.draw(screen, player)


        #Updates shit 
        pygame.display.update()
        player.update()
        swords.update()
        rays.update()




    #haha method within methon lol funniegklafdsjgkdlgj

if  __name__ == "__main__":
    main()
