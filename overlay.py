import pygame



def calculations(tilesize):
    height = tilesize * 2
    width = tilesize * 15
    height_hp = tilesize * 15
    widht_hp = tilesize * 2
    return width, height, height_hp, widht_hp



def rect(screen, width, height, width_hp, height_hp ):
    damage = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(screen, "red", damage)

    hp_rect = pygame.Rect(0, 0, width_hp, height_hp)
    pygame.draw.rect(screen, "green", hp_rect)





def displayrer(screen, tilesize):
    width, height, widht_hp, height_hp = calculations(tilesize)
    rect(screen, width, height, widht_hp, height_hp)




