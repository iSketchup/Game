import pygame
import sys
import map

def draw_main_screen(screen):

    a_button = pygame.image.load("Attachments/menu/a_button.png")
    b_button = pygame.image.load("Attachments/menu/b_button.png")
    x_button = pygame.image.load("Attachments/menu/x_button.png")
    y_button = pygame.image.load("Attachments/menu/y_button.png")
    l_joy = pygame.image.load("Attachments/menu/l_button.png")

    screen.blit(a_button, (0, 16))
    screen.blit(b_button, (0, 32))
    screen.blit(x_button, (0, 50))
    screen.blit(y_button, (0, 66))

    pygame.display.flip()

def clear_screen(screen, color):
    screen.fill(color)
    pygame.display.flip()

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
                    clear_screen(screen, (255, 182, 193)) # Pink

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





















