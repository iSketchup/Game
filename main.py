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



    map_list, map_data = map.map_lister('Attachments/map/tilesets_and_maps/darcos_feuer_freudenhaus.tmx')

    pygame.display.set_caption("1 vs 1")
    clock = pygame.time.Clock()
    running = True



    #cotroler zeug
    controllers = []

    colors = ['pink', 'red', 'blue', 'yellow']
    col_num = 0

    while running:

        map.map_drawer(screen, map_list, map_data, screen_width, screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.JOYDEVICEADDED:
                controller = Player(event.device_index, colors[col_num % 4], controllers)
                controllers.append(controller)
                col_num += 1

        for controller in controllers:
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
