import pygame

def process_inputs():
    key_status = {"is_shooting": False, "ray_gun":False}
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        key_status["is_shooting"] = True
    else:
        key_status["is_shooting"] = False
    if keys[pygame.K_LEFT]:
        key_status["ray_gun"] = True
    return key_status
def process_inputs1():
    key_status = {"is_shooting": False, "ray_gun":False}
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        key_status["is_shooting"] = True
    else:
        key_status["is_shooting"] = False
    if keys[pygame.K_RIGHT]:
        key_status["ray_gun"] = True
    return key_status

