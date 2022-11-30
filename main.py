import pygame
import global_vars
import sys
import inputs
import sprites.player, sprites.sword, sprites.gun, sprites.health_bar, sprites.gameOver
from sprites.ray_gun import Ray_Gun, Ray
import random

pygame.init()
WIDTH = global_vars.window_dimensions[0]
HEIGHT = global_vars.window_dimensions[1]
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    global time_since_shot, time_since_shot1
    #Sprites and stuff
    player = sprites.player.Player((0, HEIGHT/2), 0)
    player1 = sprites.player.Player((WIDTH, HEIGHT/2), 1)
    input_status = {}
    weapon_list = ["swords", "raygun", "gun", "machine_gun"]
    weapons_shot = {}
    weapons_shot["swords"] = pygame.sprite.Group()
    weapons_shot["raygun"] = pygame.sprite.Group()
    weapons_shot["gun"] = pygame.sprite.Group()
    weapons_shot["machine_gun"] = pygame.sprite.Group()
    weapons1_shot = {}
    weapons1_shot["swords"] = pygame.sprite.Group()
    weapons1_shot["raygun"] = pygame.sprite.Group()
    weapons1_shot["gun"] = pygame.sprite.Group()
    weapons1_shot["machine_gun"] = pygame.sprite.Group()
    weapons_held = {}
    weapons_held["raygun"] = Ray_Gun(player, 0)
    weapons_held["swords"] = sprites.sword.Sword_Held(player, 0)
    weapons_held["gun"] = sprites.gun.Gun(player, 0)
    weapons_held["machine_gun"] = sprites.gun.Machine_Gun(player, 0)
    weapons1_held = {}
    weapons1_held["raygun"] = Ray_Gun(player1, 1)
    weapons1_held["swords"] = sprites.sword.Sword_Held(player1, 1)
    weapons1_held["gun"] = sprites.gun.Gun(player1, 1)
    weapons1_held["machine_gun"] = sprites.gun.Machine_Gun(player1, 1)
    running = True
    weapon = random.choice(weapon_list)
    weapon1 = random.choice(weapon_list)
    time_since_shot = 10000
    time_since_shot1 = 10000
    health_bar = sprites.health_bar.Health_Bar(player, 0)
    health_bar1 = sprites.health_bar.Health_Bar(player1, 1)
    gameover = sprites.gameOver.GameOver()
    def weaponHandler(w, p): #decides if player can shoot
        if p == player:
            if w == "swords":
                # sword_count = 0
                # for sword in weapons_shot["swords"]:
                #     if sword.flying:
                #         sword_count += 1
                if time_since_shot < 35:
                    p.can_shoot = False
                else:
                    p.can_shoot = True
            elif w == "raygun":
                raycount = 0
                for ray in weapons_shot["raygun"]:
                    if ray.flying:
                        raycount += 1
                if raycount < 7:
                    p.can_shoot = True
                else:
                    p.can_shoot = False
            elif w == "gun":
                if time_since_shot < 60:
                    p.can_shoot = False
                else:
                    p.can_shoot = True
            elif w == "machine_gun":
                bullet_count = 0
                for bul in weapons_shot["machine_gun"]:
                    if bul.flying:
                        bullet_count += 1
                if time_since_shot < 10 or bullet_count > 15:
                    p.can_shoot = False
                else:
                    p.can_shoot = True
        if not player.alive:
            player.can_shoot = False

        if p == player1:
            if w == "swords":
                # sword_count = 0
                # for sword in weapons_shot["swords"]:
                #     if sword.flying:
                #         sword_count += 1
                if time_since_shot1 < 35:
                    p.can_shoot = False
                else:
                    p.can_shoot = True
            elif w == "raygun":
                raycount = 0
                for ray in weapons1_shot["raygun"]:
                    if ray.flying:
                        raycount += 1
                if raycount < 7:
                    p.can_shoot = True
                else:
                    p.can_shoot = False
            elif w == "gun":
                if time_since_shot1 < 60:
                    p.can_shoot = False
                else:
                    p.can_shoot = True
            elif w == "machine_gun":
                bullet_count = 0
                for bul in weapons1_shot["machine_gun"]:
                    if bul.flying:
                        bullet_count += 1
                if time_since_shot1 < 10 or bullet_count > 7:
                    p.can_shoot = False
                else:
                    p.can_shoot = True
        if not player1.alive:
            player1.can_shoot = False


    def shootWeapons(p): #shoots the player
        global time_since_shot, time_since_shot1
        if p == player:
            if input_status["is_shooting"] and p.can_shoot:
                if weapon == "swords":
                    time_since_shot = 0
                    weapons_shot["swords"].add(sprites.sword.Sword(player, 0))
                elif weapon == "raygun":
                    weapons_shot["raygun"].add(Ray(player, 0))
                elif weapon == "gun":
                    time_since_shot = 0
                    weapons_shot["gun"].add(sprites.gun.Bullet(player, 0))
                elif weapon == "machine_gun":
                    time_since_shot = 0
                    weapons_shot["machine_gun"].add(sprites.gun.Bullet(player, 0))
        if p == player1:
            if input_status1["is_shooting"] and p.can_shoot:
                if weapon1 == "swords":
                    time_since_shot1 = 0
                    weapons1_shot["swords"].add(sprites.sword.Sword(player1, 1))
                elif weapon1 == "raygun":
                    weapons1_shot["raygun"].add(Ray(player1, 1))
                elif weapon1 == "gun":
                    time_since_shot1 = 0
                    weapons1_shot["gun"].add(sprites.gun.Bullet(player1, 1))
                elif weapon1 == "machine_gun":
                    time_since_shot1 = 0
                    weapons1_shot["machine_gun"].add(sprites.gun.Bullet(player1, 1))

    def collisions():
        for wep in weapons_shot:
            for w in weapons_shot[wep]:
                if pygame.sprite.collide_mask(player1, w):
                    if wep == "swords" and w.can_kill:
                        w.image = w.image_list[1]
                        w.can_kill = False
                        player1.update_health(global_vars.sword_damage)
                        # print("Player 1 has been hit, health = ", player1.health)
                    elif wep == "raygun":
                        w.kill()
                        player1.update_health(global_vars.raygun_damage)
                        # print("Player 1 has been hit, health = ", player1.health)
                    elif wep == "gun":
                        player1.update_health(global_vars.gun_damage)
                        # print("Player 1 has been hit, health = ", player1.health)
                        w.kill()
                    elif wep == "machine_gun":
                        player1.update_health(global_vars.machine_gun_damage) 
                        w.kill()
        for wep in weapons1_shot:
            for w in weapons1_shot[wep]:
                if pygame.sprite.collide_mask(player, w):
                    if wep == "swords" and w.can_kill:
                        w.image = w.image_list[1]
                        w.can_kill = False
                        player.update_health(global_vars.sword_damage)
                        # print("Player 0 has been hit, health = ", player.health)
                    elif wep == "raygun":
                        w.kill()
                        player.update_health(global_vars.raygun_damage)
                        # print("Player 0 has been hit, health = ", player.health)
                    elif wep == "gun":
                        player.update_health(global_vars.gun_damage)
                        # print("Player 0 has been hit, health = ", player.health)
                        w.kill()
                    elif wep == "machine_gun":
                        player.update_health(global_vars.machine_gun_damage) 
                        w.kill()

    while running:
        clock.tick(global_vars.FPS)
        time_since_shot1 += 1
        time_since_shot += 1
        input_status = inputs.process_inputs()
        input_status1 = inputs.process_inputs1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_r:
                    main()
        #inputs and shit
        if player.swap_weapon:
            player.can_shoot = True; #sets can shoot to true to stop it from being stuck as false if sword is in the air dumbass
            #weapon = weapon_list[(weapon_list.index(weapon)+1)%len(weapon_list)]
            new_list = weapon_list.copy()
            new_list.remove(weapon)
            weapon = random.choice(new_list)
            player.swap_weapon = False
        if player1.swap_weapon:
            player1.can_shoot = True; #sets can shoot to true to stop it from being stuck as false if sword is in the air dumbass
            new_list = weapon_list.copy()
            new_list.remove(weapon1)
            weapon1 = random.choice(new_list)
            player1.swap_weapon = False


        #HELL YES SHOOTING THINGS IS COOL GUNS GO BOOM AMERICA WOOOOOOOOOO
        weaponHandler(weapon, player)
        weaponHandler(weapon1, player1)
        shootWeapons(player)
        shootWeapons(player1)

        collisions()


        #Gameover shit
        if not player.alive:
            gameover.updateWinner(2)
        if not player1.alive:
            gameover.updateWinner(1)

        #drawing shit
        screen.fill(global_vars.SCREEN_COLOR)
        if player.alive:
            player.draw(screen)
            weapons_held[weapon].draw(screen)
        if player1.alive:
            player1.draw(screen)
            weapons1_held[weapon1].draw(screen)
        for w in weapons_shot:
            weapons_shot[w].draw(screen)
        for w in weapons_shot:
            weapons1_shot[w].draw(screen)
        health_bar.draw(screen)
        health_bar1.draw(screen)
        gameover.draw(screen)


        #Updates shit 
        pygame.display.update()
        if player.alive:
            player.update()
            weapons_held[weapon].update()
        if player1.alive:
            player1.update()
            weapons1_held[weapon1].update()
        for w in weapons_shot:
            weapons_shot[w].update()
        for w in weapons_shot:
            weapons1_shot[w].update()




    #haha method within methon lol funniegklafdsjgkdlgj

if  __name__ == "__main__":
    main()
