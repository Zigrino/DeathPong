import pygame

def process_inputs():
    key_status = {"is_shooting": False, "weapon_swap":False}
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        key_status["is_shooting"] = True
    else:
        key_status["is_shooting"] = False
   # if keys[pygame.K_a]:
   #     key_status["weapon_swap"] = True
    return key_status
def process_inputs1():
    key_status = {"is_shooting": False, "weapon_swap":False}
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        key_status["is_shooting"] = True
    else:
        key_status["is_shooting"] = False
   # if keys[pygame.K_RIGHT]:
   #     key_status["weapon_swap"] = True

    return key_status

