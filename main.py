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

    player = sprites.player.Player((0, HEIGHT/2), 0)
    player1 = sprites.player.Player((WIDTH, HEIGHT/2), 1)
    input_status = {}
    weapons_shot = {}
    weapons_shot["swords"] = pygame.sprite.Group()
    weapons_shot["raygun"] = pygame.sprite.Group()
    weapons1_shot = {}
    weapons1_shot["swords"] = pygame.sprite.Group()
    weapons1_shot["raygun"] = pygame.sprite.Group()
    weapons_held = {}
    weapons_held["raygun"] = Ray_Gun(player, 0)
    weapons_held["swords"] = sprites.sword.Sword_Held(player, 0)
    weapons1_held = {}
    weapons1_held["raygun"] = Ray_Gun(player1, 1)
    weapons1_held["swords"] = sprites.sword.Sword_Held(player1, 1)
    running = True
    weapon = "swords"
    weapon1 = "swords"
    def weaponHandler(w, p): #decides if player can shoot
        pass

    def shootWeapons(p): #shoots the player
        pass
    def update_weapons(w, p):
        pass
    while running:
        clock.tick(global_vars.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #inputs and shit
        input_status = inputs.process_inputs()
        input_status1 = inputs.process_inputs1()
        
        if input_status["ray_gun"] == True and weapon != "raygun":
            player.can_shoot = True; #sets can shoot to true to stop it from being stuck as false if sword is in the air dumbass
            weapon = "raygun"
        if input_status1["ray_gun"] == True and weapon1 != "raygun":
            player1.can_shoot = True; #sets can shoot to true to stop it from being stuck as false if sword is in the air dumbass
            weapon1 = "raygun"
        #HELL YES SHOOTING THINGS IS COOL GUNS GO BOOM AMERICA WOOOOOOOOOO
        weaponHandler(weapon, player)
        weaponHandler(weapon1, player1)
        shootWeapons(player)
        shootWeapons(player1)


        #drawing shit
        screen.fill(global_vars.SCREEN_COLOR)
        player.draw(screen)
        player1.draw(screen)
        weapons_shot[weapon].draw(screen)
        weapons1_shot[weapon1].draw(screen)
        weapons_held[weapon].draw(screen)
        weapons1_held[weapon1].draw(screen)


        #Updates shit 
        pygame.display.update()
        player.update()
        player1.update()
        weapons_shot[weapon].update()
        weapons1_shot[weapon].update()
        weapons_held[weapon].update()
        weapons1_held[weapon1].update()




    #haha method within methon lol funniegklafdsjgkdlgj

if  __name__ == "__main__":
    main()
