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


def map_drawer(surface, map_list, map_data, measure):
    global upsizefaktorw, upsizefaktorh
    upsizefaktorw, upsizefaktorh = surface.get_width() / (45 * measure), surface.get_height() / (25 * measure)

    if False:
        pass
    else:
        for layer in map_list:
            for x, y, gid in layer:
                tile = map_data.get_tile_image_by_gid(gid)
                if tile:
                    tile = pygame.transform.scale(tile, (measure * upsizefaktorw + 1, measure * upsizefaktorh + 1))
                    surface.blit(tile, (x * upsizefaktorw * map_data.tilewidth, y * upsizefaktorh * map_data.tileheight))

    return upsizefaktorh, upsizefaktorw



def collider(map_data):
    floor = []

    for layer in map_data.visible_layers:
        if layer.name == 'floor' and isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_img = map_data.get_tile_image_by_gid(gid)
                if tile_img:
                    tile = pygame.Rect(x * map_data.tilewidth * upsizefaktorw,
                                        y * map_data.tileheight * upsizefaktorh,
                                        map_data.tilewidth * upsizefaktorw+1,
                                        map_data.tileheight * upsizefaktorh+1)


                    floor.append(tile)
    return floor










