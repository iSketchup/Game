import pygame
import pytmx
def map_lister(tmxfile):
#   this takes every tile that is a instance(that means it will have to be drawn) and puts it in a list
#   every row has its own list inside of the map list

    map_data = pytmx.load_pygame(tmxfile)
    map_list = []
    floor_tiles = []
    for row in map_data.visible_layers:
        if isinstance(row, pytmx.TiledTileLayer):
            map_list.append(row)
#            if row.name == 'floor':
    return map_list, map_data, floor_tiles


def map_drawer(surface, map_list, map_data, measure):
    upsizefaktorw, upsizefaktorh = surface.get_width() / (45*measure), surface.get_height() / (25 * measure)

    for layer in map_list:
        for x, y, gid in layer:
            tile = map_data.get_tile_image_by_gid(gid)
            if tile:
                tile = pygame.transform.scale(tile, (measure * upsizefaktorw + 1, measure * upsizefaktorh + 1))
                surface.blit(tile, (x * upsizefaktorw * map_data.tilewidth, y * upsizefaktorh * map_data.tileheight))



def collider(mapdata):
    collisions_layer = []
    for x, y, gid in mapdata.get_layer_by_name("floor"):
        if gid:
            tile_rect = pygame.Rect(x * mapdata.tilewidth,y * mapdata.tileheight,mapdata.tilewidth,mapdata.tileheight)
            collisions_layer.append(tile_rect)

    return collisions_layer








