import sys, pygame
from player import Player
from spritesheet import Spritesheet



def heart(screen):
        heart = Spritesheet('Attachments/UI/heart.png', (320, 320))

        heart.draw(screen)


def main():

    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("1 vs 1")
    clock = pygame.time.Clock()
    running = True

    #cotroler zeug
    controllers = []

    # Player init
    while running:

        screen.fill('white')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.JOYDEVICEADDED:
                controller = Player(event.device_index, 'pink')
                controllers.append(controller)


        try:
            i = 0
            for controller in controllers:
                print(i)
                print(controller.name)
                controller.displayer(screen)
                controller.moovement_controller()
                i+=1
        except FileExistsError:
            print('e')


        print(controllers)


        heart(screen)




        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()