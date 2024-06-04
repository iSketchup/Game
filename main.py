import sys, pygame
from player import Player
from spritesheet import Spritesheet
import map




def heart(screen):
    heart = Spritesheet('Attachments/UI/heart.png', (320, 320))
    heart.draw(screen)


def main():

    pygame.init()

    screen = pygame.display.set_mode((0, 0))

    screen_width = screen.get_width()
    screen_height = screen.get_height()



    map_list, map_data, floor_tiles = map.map_lister('Attachments/map/tilesets_and_maps/new tilemap/mapabc.tmx')
    upsizefaktorh, upsizefaktorw = map.map_drawer(screen, map_list, map_data, measure=16)


    pygame.display.set_caption("1 vs 1")
    clock = pygame.time.Clock()
    running = True



    #cotroler zeug

    controllers = []

    colors = ['pink', 'red', 'blue', 'yellow']
    col_num = 0

    player1_rect = pygame.Rect(0, 320 * upsizefaktorh, 16 * upsizefaktorh, 16 * upsizefaktorw)

    player2_rect = pygame.Rect(screen_width - 16 * upsizefaktorw, 320 * upsizefaktorh, 16 * upsizefaktorh, 16 * upsizefaktorw)
    rect = player1_rect

    while running:

        map.map_drawer(screen, map_list, map_data, 16)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.JOYDEVICEADDED:
                for controller in controllers:
                    if len(controllers) % 2 == 0:
                        rect = player1_rect
                    else:
                        rect = player2_rect

                print('here')
                stick = Player(event.device_index, colors[col_num % 4], rect)
                controllers.append(stick)
                col_num += 1




        for controller in controllers:
            print('sad')
            print(controller.device_index)

        try:
            for controller in controllers:
                controller.displayer(screen)

        except:
            print('no controller connected')

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
