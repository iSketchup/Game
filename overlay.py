import pygame



def calculations(tilesize):
    height = tilesize * 2
    width = tilesize * 15
    return width, height



def rect(width, height, screen):
    damage = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(screen, "red", damage)

    health = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(screen, "green", health)

def displayrer(screen, tilesize):
    width, height = calculations(tilesize)
    rect(width, height, screen)




