import sys, pygame
from player import Player

import map
import menu



def main():

    pygame.init()

    screen = pygame.display.set_mode((0, 0))

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    map_list, map_data = map.map_lister('Attachments/map/tilesets_and_maps/new tilemap/mapabc.tmx')
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

    player1_rect = pygame.Rect(0, 320 * upsizefaktorh, tilesize * upsizefaktorh, tilesize * upsizefaktorw)

    player2_rect = pygame.Rect(screen_width - tilesize * upsizefaktorw, 320 * upsizefaktorh, tilesize * upsizefaktorh, tilesize * upsizefaktorw)
    rect = player1_rect


    keyboard = menu.main_menu()

    if keyboard:
        for i in range(2):
            for controller in controllers:

                if len(controllers) % 2 == 0:
                    rect = player1_rect
                else:
                    rect = player2_rect

            stick = Player(i, floor, tilesize, controllers, screen, keyboard, upsizefaktorw)
            controllers.append(stick)

    while running:

        map.map_drawer(screen, map_list, map_data, upsizefaktorw, upsizefaktorh)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("esc gedrückt")
                    menu.main_menu()

            if event.type == pygame.JOYDEVICEADDED and not keyboard:
                for controller in controllers:

                    if len(controllers) % 2 == 0:
                        rect = player1_rect
                    else:
                        rect = player2_rect
                stick = Player(event.device_index, floor, tilesize, controllers, screen,
                               keyboard, upsizefaktorw)
                controllers.append(stick)

        for controller in controllers:
            controller.update(controllers)


        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()


