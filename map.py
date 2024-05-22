import pygame
import pytmx
from pytmx.util_pygame import load_pygame
pygame.init()

def loader():
    tmx_data = load_pygame("Attachments/map/tilesets_and_maps/darcos_feuer_freudenhaus.tmx")
    tilewidth = tmx_data.tilewidth
    tileheight = tmx_data.tileheight

    return tmx_data, tilewidth, tileheight


def drawer(tmx_data, tilewidth, tileheight, screen):

    for layer in tmx_data.layers:
        #is instace returned entweder True oder False
        if isinstance(layer, pytmx.TiledTileLayer):
            # x und y für die positionen
            for x, y, tile in layer.tiles():
                if(tile):
                    screen.blit(tile, [x*tilewidth, y*tileheight])

        else:
            continue






