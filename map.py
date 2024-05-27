import pygame
import pytmx
def map_lister(tmxfile):
#   this takes every tile that is a instance(that means it will have to be drawn) and puts it in a list
#   every row has its own list inside of the map list

    map_data = pytmx.load_pygame(tmxfile)
    map_list = []
    for row in map_data.visible_layers:
        if isinstance(row, pytmx.TiledTileLayer):
            map_list.append(row)

    return map_list, map_data


def map_drawer(surface, map_list, map_data):
    upsizefaktorw, upsizefaktorh = surface.get_width() / (50*24), surface.get_height() / (25*24)

    for layer in map_list:
        for x, y, gid in layer:
            tile = map_data.get_tile_image_by_gid(gid)
            if tile:
                tile = pygame.transform.scale(tile, (24 * upsizefaktorw + 1, 24 * upsizefaktorh + 1))
                surface.blit(tile, (x * upsizefaktorw * map_data.tilewidth, y * upsizefaktorh * map_data.tileheight))








