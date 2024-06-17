import sys, pygame
from player import Player

import map
import menu



def main():

    pygame.init()

    screen = pygame.display.set_mode((0, 0))

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    map_list, map_data = map.map_lister('assets/map/tilesets_and_maps/new tilemap/mapabc.tmx')
    measurew = map_data.tilewidth
    measureh = map_data.tileheight
    upsizefaktorw, upsizefaktorh = screen_width / (45 * measurew), screen_height / (25 * measureh)

    pygame.display.set_caption("1 vs 1")
    clock = pygame.time.Clock()
    running = True

    floor = map.collider(map_data, upsizefaktorw, upsizefaktorh)

    #cotroler zeug

    controllers = []

    
    tilesize = 16

    keyboard = menu.main_menu()

    if keyboard:
        for i in range(2):

            stick = Player(i, floor, tilesize, controllers, screen, upsizefaktorw, keyboard)
            controllers.append(stick)

    while running:

        map.map_drawer(screen, map_list, map_data, upsizefaktorw, upsizefaktorh)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.main_menu()

            if event.type == pygame.JOYDEVICEADDED and not keyboard:
                stick = Player(event.device_index, floor, tilesize, controllers, screen, upsizefaktorw,
                               keyboard)
                controllers.append(stick)

        for controller in controllers:
            controller.update(controllers)


        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()


