import pygame
import sys
import map

def draw_main_screen(screen):

    screen_width = screen.get_width()
    screen_height = screen.get_height()


    a_button = pygame.image.load("Attachments/menu/a_button.png").convert_alpha()
    b_button = pygame.image.load("Attachments/menu/b_button.png").convert_alpha()
    x_button = pygame.image.load("Attachments/menu/x_button.png").convert_alpha()
    y_button = pygame.image.load("Attachments/menu/y_button.png").convert_alpha()
    l_joy = pygame.image.load("Attachments/menu/l_button.png").convert_alpha()

    play = pygame.image.load("Attachments/menu/play.png").convert_alpha()
    options = pygame.image.load("Attachments/menu/options.png").convert_alpha()
    quit = pygame.image.load("Attachments/menu/quit.png").convert_alpha()

    scale_factor = 5

    play = pygame.transform.scale(play, (play.get_width() * scale_factor, play.get_height() * scale_factor))
    options = pygame.transform.scale(options, (options.get_width() * scale_factor, options.get_height() * scale_factor))
    quit = pygame.transform.scale(quit, (quit.get_width() * scale_factor, quit.get_height() * scale_factor))

    play_pos = [screen_width / 2 - play.get_width() / 2, screen_height / 2 - 200]
    options_pos = [screen_width / 2 - options.get_width() / 2, screen_height / 2 - 100]
    quit_pos = [screen_width / 2 - quit.get_width() / 2, screen_height / 2]

    screen.blit(play, play_pos)
    screen.blit(options, options_pos)
    screen.blit(quit, quit_pos)


    button_spacing = 20  

    screen.blit(a_button, (play_pos[0] + play.get_width() + button_spacing, play_pos[1] + a_button.get_width() / 4))
    screen.blit(y_button, (options_pos[0] + options.get_width() + button_spacing, options_pos[1] + y_button.get_width() / 4))
    screen.blit(b_button, (quit_pos[0] + quit.get_width() + button_spacing, quit_pos[1] + b_button.get_width() / 4))

    pygame.display.flip()

def clear_screen(screen, color):
    screen.fill(color)
    pygame.display.flip()

def options_menu(screen):

    clear_screen(screen, (0, 0, 0))

    a_button = pygame.image.load("Attachments/menu/a_button.png").convert_alpha()
    b_button = pygame.image.load("Attachments/menu/b_button.png").convert_alpha()
    x_button = pygame.image.load("Attachments/menu/x_button.png").convert_alpha()
    y_button = pygame.image.load("Attachments/menu/y_button.png").convert_alpha()
    l_joy = pygame.image.load("Attachments/menu/l_button.png").convert_alpha()





def main_menu():
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    screen = pygame.display.set_mode((0,0))
    pygame.display.set_caption("Joystick Test")

    draw_main_screen(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(0):

                    options_menu(screen)


                elif joystick.get_button(1):
                    pygame.quit()
                    sys.exit()

                #player knopf

                elif joystick.get_button(2):
                    running = False

                elif joystick.get_button(3):
                    clear_screen(screen, (0, 255, 0))  # Grün

        pygame.display.update()

    pygame.quit()
    sys.exit()

def displayer():
    if __name__ == '__main__':
        main_menu()
displayer()





















