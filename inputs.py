import pygame

def process_inputs():
    key_status = {"is_shooting": False}
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        key_status["is_shooting"] = True
    else:
        key_status["is_shooting"] = False
    return key_status

