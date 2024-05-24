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

    print(screen_height)
    print(screen_width)

    tmx_data, tilewidth, tileheight = map.loader()

    pygame.display.set_caption("1 vs 1")
    clock = pygame.time.Clock()
    running = True



    #cotroler zeug
    controllers = []

    colors = ['pink', 'red', 'blue', 'yellow']
    col_num = 0

    while running:

        map.drawer(tmx_data, tilewidth, tileheight, screen, screen_width, screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.JOYDEVICEADDED:
                controller = Player(event.device_index, colors[col_num % 4])
                controllers.append(controller)
                col_num += 1


        try:
            for controller in controllers:

                controller.displayer(screen)

        except:
            print('no controller connected')

        heart(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
