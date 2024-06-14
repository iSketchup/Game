import sys, pygame
from player import Player
from spritesheet import Spritesheet
import map
import menu


def heart(screen):
    heart = Spritesheet('Attachments/UI/heart.png', (320, 320))
    heart.draw(screen)



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

    col_num = 0
    
    tilesize = 16

    player1_rect = pygame.Rect(0, 320 * upsizefaktorh, tilesize * upsizefaktorh, tilesize * upsizefaktorw)

    player2_rect = pygame.Rect(screen_width - tilesize * upsizefaktorw, 320 * upsizefaktorh, tilesize * upsizefaktorh, tilesize * upsizefaktorw)
    rect = player1_rect

    while running:

        map.map_drawer(screen, map_list, map_data, upsizefaktorw, upsizefaktorh)


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

                stick = Player(event.device_index, rect, floor, tilesize, controllers, screen_width)
                controllers.append(stick)
                col_num += 1

        for controller in controllers:
            if controller.dead:
                print(controller.controller_num, ' wins')
                sys.exit()

        if False:
            for rect in floor:
                pygame.draw.rect(screen, 'pink', rect)


#        try:
        hits_list = []
        for controller in controllers:
            controller.displayer(screen, controllers)
            print(controller.controller_num)

            hits = hits_list
#        except:
#            print('no controller connected')

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    menu.main_menu(main)

