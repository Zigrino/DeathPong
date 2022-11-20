import pygame

def get_inputs():
    return pygame.key.get_pressed()

def shoot(keys):
    if keys[pygame.K_SPACE]:
        return True
    

def process_inputs():
    keys = get_inputs()
    return {"is_shooting": shoot(keys)}
