import pygame
from pytmx.util_pygame import load_pygame
pygame.init()

def seba():
    tmx_data = load_pygame("Attachments/map/tilesets_and_maps/darcos_feuer_freudenhaus.tmx")

    print(tmx_data)