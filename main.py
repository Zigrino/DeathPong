import pygame
import global_vars
import sys
import inputs
import sprites.player, sprites.sword, sprites.gun, sprites.health_bar, sprites.gameOver, sprites.rocket_launcher
from sprites.ray_gun import Ray_Gun, Ray
import pygame.mixer as mixer
import random

pygame.init()
mixer.init()
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
    weapon_list = ["swords", "raygun", "gun", "machine_gun", "rocket"]
    sword_hit = mixer.Sound(r"assets/sounds/sword_hit.mp3")
    sword_hit.set_volume(3)
    sounds = {"rocket": mixer.Sound(r"assets/sounds/rocket_fire.wav"), "swords": mixer.Sound(r"assets/sounds/sword.wav"), "raygun": mixer.Sound(r"assets/sounds/raygun.wav"), "gun": mixer.Sound(r"assets/sounds/gun.mp3"), "machine_gun": mixer.Sound(r"assets/sounds/machine_gun.mp3"), "player_hit": mixer.Sound(r"assets/sounds/hit.wav"), "sword_hit": sword_hit}
    weapons_shot = {}
    weapons_shot["swords"] = pygame.sprite.Group()
    weapons_shot["raygun"] = pygame.sprite.Group()
    weapons_shot["gun"] = pygame.sprite.Group()
    weapons_shot["machine_gun"] = pygame.sprite.Group()
    weapons_shot["rocket"] = pygame.sprite.Group()
    weapons1_shot = {}
    weapons1_shot["swords"] = pygame.sprite.Group()
    weapons1_shot["raygun"] = pygame.sprite.Group()
    weapons1_shot["gun"] = pygame.sprite.Group()
    weapons1_shot["machine_gun"] = pygame.sprite.Group()
    weapons1_shot["rocket"] = pygame.sprite.Group()
    weapons_held = {}
    weapons_held["raygun"] = Ray_Gun(player, 0)
    weapons_held["swords"] = sprites.sword.Sword_Held(player, 0)
    weapons_held["gun"] = sprites.gun.Gun(player, 0)
    weapons_held["machine_gun"] = sprites.gun.Machine_Gun(player, 0)
    weapons_held["rocket"] = sprites.rocket_launcher.Launcher(player, 0)
    weapons1_held = {}
    weapons1_held["raygun"] = Ray_Gun(player1, 1)
    weapons1_held["swords"] = sprites.sword.Sword_Held(player1, 1)
    weapons1_held["gun"] = sprites.gun.Gun(player1, 1)
    weapons1_held["machine_gun"] = sprites.gun.Machine_Gun(player1, 1)
    weapons1_held["rocket"] = sprites.rocket_launcher.Launcher(player1, 1)
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
            elif w == "rocket":
                if time_since_shot < 90:
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
            elif w == "rocket":
                if time_since_shot1 < 90:
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
                    sounds[weapon].stop()
                    sounds["swords"].play()
                    weapons_shot["swords"].add(sprites.sword.Sword(player, 0))
                elif weapon == "raygun":
                    #sounds[weapon].stop()
                    sounds["raygun"].play()
                    weapons_shot["raygun"].add(Ray(player, 0))
                elif weapon == "gun":
                    sounds[weapon].stop()
                    sounds["gun"].play()
                    time_since_shot = 0
                    weapons_shot["gun"].add(sprites.gun.Bullet(player, 0))
                elif weapon == "machine_gun":
                    sounds[weapon].stop()
                    sounds["machine_gun"].play()
                    time_since_shot = 0
                    weapons_shot["machine_gun"].add(sprites.gun.Bullet(player, 0))
                elif weapon == "rocket":
                    sounds[weapon].stop()
                    sounds["rocket"].play()
                    time_since_shot = 0
                    weapons_shot["rocket"].add(sprites.rocket_launcher.Rocket(player, 0))
        if p == player1:
            if input_status1["is_shooting"] and p.can_shoot:
                if weapon1 == "swords":
                    sounds[weapon1].stop()
                    sounds["swords"].play()
                    time_since_shot1 = 0
                    weapons1_shot["swords"].add(sprites.sword.Sword(player1, 1))
                elif weapon1 == "raygun":
                    #sounds[weapon1].stop()
                    sounds["raygun"].play()
                    weapons1_shot["raygun"].add(Ray(player1, 1))
                elif weapon1 == "gun":
                    sounds[weapon1].stop()
                    sounds["gun"].play()
                    time_since_shot1 = 0
                    weapons1_shot["gun"].add(sprites.gun.Bullet(player1, 1))
                elif weapon1 == "machine_gun":
                    sounds[weapon1].stop()
                    sounds["machine_gun"].play()
                    time_since_shot1 = 0
                    weapons1_shot["machine_gun"].add(sprites.gun.Bullet(player1, 1))
                elif weapon1 == "rocket":
                    sounds[weapon1].stop()
                    sounds["rocket"].play()
                    time_since_shot1 = 0
                    weapons1_shot["rocket"].add(sprites.rocket_launcher.Rocket(player1, 1))

    def collisions():
        for wep in weapons_shot:
            for w in weapons_shot[wep]:
                if pygame.sprite.collide_mask(player1, w):
                    if wep == "swords" and w.can_kill:
                        sounds["sword_hit"].play()
                        w.image = w.image_list[1]
                        w.can_kill = False
                        player1.update_health(global_vars.sword_damage)
                        # print("Player 1 has been hit, health = ", player1.health)
                    elif wep == "raygun":
                        sounds["player_hit"].play()
                        w.kill()
                        player1.update_health(global_vars.raygun_damage)
                        # print("Player 1 has been hit, health = ", player1.health)
                    elif wep == "gun":
                        sounds["player_hit"].play()
                        player1.update_health(global_vars.gun_damage)
                        # print("Player 1 has been hit, health = ", player1.health)
                        w.kill()
                    elif wep == "machine_gun":
                        sounds["player_hit"].play()
                        player1.update_health(global_vars.machine_gun_damage) 
                        w.kill()
                    elif wep == "rocket":
                        if w.dealing_damage:
                            sounds["player_hit"].play()
                            player1.update_health(global_vars.explosion_damage) 
                            w.dealing_damage = False
        for wep in weapons1_shot:
            for w in weapons1_shot[wep]:
                if pygame.sprite.collide_mask(player, w):
                    if wep == "swords" and w.can_kill:
                        sounds["sword_hit"].play()
                        w.image = w.image_list[1]
                        w.can_kill = False
                        player.update_health(global_vars.sword_damage)
                        # print("Player 0 has been hit, health = ", player.health)
                    elif wep == "raygun":
                        sounds["player_hit"].play()
                        w.kill()
                        player.update_health(global_vars.raygun_damage)
                        # print("Player 0 has been hit, health = ", player.health)
                    elif wep == "gun":
                        sounds["player_hit"].play()
                        player.update_health(global_vars.gun_damage)
                        # print("Player 0 has been hit, health = ", player.health)
                        w.kill()
                    elif wep == "machine_gun":
                        sounds["player_hit"].play()
                        player.update_health(global_vars.machine_gun_damage) 
                        w.kill()
                    elif wep == "rocket":
                        if w.dealing_damage:
                            sounds["player_hit"].play()
                            player.update_health(global_vars.explosion_damage) 
                            w.dealing_damage = False

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
            time_since_shot = 100
            #weapon = weapon_list[(weapon_list.index(weapon)+1)%len(weapon_list)]
            new_list = weapon_list.copy()
            new_list.remove(weapon)
            weapon = random.choice(new_list)
            player.swap_weapon = False
        if player1.swap_weapon:
            player1.can_shoot = True;
            time_since_shot1 = 100 #sets can shoot to true to stop it from being stuck as false if sword is in the air dumbass
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
            if w == "rocket":
                weapons_shot[w].update(player1.rect.centery)
            else:
                weapons_shot[w].update()
        for w in weapons1_shot:
            if w == "rocket":
                weapons1_shot[w].update(player.rect.centery)
            else:
                weapons1_shot[w].update()
        
        #Launcher update
        if weapon == "rocket" and weapons_held["rocket"].is_full and time_since_shot < 90:
            weapons_held["rocket"].is_full = False
        elif weapon == "rocket" and (not weapons_held["rocket"].is_full) and time_since_shot >= 90:
            weapons_held["rocket"].is_full = True
        if weapon1 == "rocket" and weapons1_held["rocket"].is_full and time_since_shot1 < 90:
            weapons1_held["rocket"].is_full = False
        elif weapon1 == "rocket" and (not weapons1_held["rocket"].is_full) and time_since_shot1 >= 90:
            weapons1_held["rocket"].is_full = True





    #haha method within methon lol funniegklafdsjgkdlgj

if  __name__ == "__main__":
    main()
