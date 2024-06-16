import pygame
import sys

def death_screen(screen):

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    bg = pygame.image.load("Attachments/menu/bg.png").convert_alpha()
    player1 = pygame.image.load("Attachments/menu/player1.png").convert_alpha()
    player2 = pygame.image.load("Attachments/menu/player2.png").convert_alpha()

    scale_factor = 5

    bg = pygame.transform.scale(bg, (bg.get_width() * scale_factor * 5, bg.get_height() * scale_factor * 5))
    player1 = pygame.transform.scale(player1, (player1.get_width() * scale_factor * 5, player1.get_height() * scale_factor ))
    player2 = pygame.transform.scale(player2, (player2.get_width() * scale_factor * 5, player2.get_height() * scale_factor ))

    bg_pos = [screen_width / 2 - bg.get_width() / 2, screen_height / 2 - bg.get_height() / 2]
    player1_rect = player1.get_rect(center=(screen_width / 2, screen_height / 2 - 200))
    player2_rect = player2.get_rect(center=(screen_width / 2, screen_height / 2 - 200))

    screen.blit(bg, bg_pos)
    screen.blit(player1, player1_rect)
    screen.blit(player2, player2_rect)

def draw_main_screen(screen):

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    a_button = pygame.image.load("Attachments/menu/a_button.png").convert_alpha()
    b_button = pygame.image.load("Attachments/menu/b_button.png").convert_alpha()
    y_button = pygame.image.load("Attachments/menu/y_button.png").convert_alpha()

    play = pygame.image.load("Attachments/menu/play.png").convert_alpha()
    options = pygame.image.load("Attachments/menu/options.png").convert_alpha()
    quit = pygame.image.load("Attachments/menu/quit.png").convert_alpha()

    start_with = pygame.image.load("Attachments/menu/start with.png").convert_alpha()
    keyboard = pygame.image.load("Attachments/menu/keyboard.png").convert_alpha()
    controller = pygame.image.load("Attachments/menu/controller.png").convert_alpha()

    scale_factor = 5

    play = pygame.transform.scale(play, (play.get_width() * scale_factor, play.get_height() * scale_factor))
    options = pygame.transform.scale(options, (options.get_width() * scale_factor, options.get_height() * scale_factor))
    quit = pygame.transform.scale(quit, (quit.get_width() * scale_factor, quit.get_height() * scale_factor))

    play_rect = play.get_rect(center=(screen_width / 2, screen_height / 2 - 200))
    options_rect = options.get_rect(center=(screen_width / 2, screen_height / 2 - 100))
    quit_rect = quit.get_rect(center=(screen_width / 2, screen_height / 2))

    start_with_rect = start_with.get_rect(center=(screen_width / 2, screen_height / 2 + screen_height / 4))
    keyboard_rect = keyboard.get_rect(center=(screen_width / 2 - screen_height/4, screen_height - screen_height / 6))
    controller_rect = controller.get_rect(center=(screen_width / 2 + screen_height / 4, screen_height - screen_height / 6))


    screen.blit(play, play_rect)
    screen.blit(options, options_rect)
    screen.blit(quit, quit_rect)

    screen.blit(start_with, start_with_rect)
    screen.blit(keyboard, keyboard_rect)
    screen.blit(controller, controller_rect)

    button_spacing = 20

    screen.blit(a_button, (play_rect.right + button_spacing, play_rect.centery - a_button.get_height() / 2))
    screen.blit(y_button, (options_rect.right + button_spacing, options_rect.centery - y_button.get_height() / 4))
    screen.blit(b_button, (quit_rect.right + button_spacing, quit_rect.centery - b_button.get_height() / 4))

    pygame.display.flip()

    return play_rect, options_rect, quit_rect, start_with_rect, keyboard_rect, controller_rect

def clear_screen(screen, color):
    screen.fill(color)
    pygame.display.flip()

def options_menu(screen):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    clear_screen(screen, (0, 0, 0))

    wasd = pygame.image.load("Attachments/menu/wasd.png").convert_alpha()
    ijkl = pygame.image.load("Attachments/menu/ijkl.png").convert_alpha()
    moovement = pygame.image.load("Attachments/menu/movement.png").convert_alpha()
    llll = pygame.image.load("Attachments/menu/llll.png").convert_alpha()
    abxy = pygame.image.load("Attachments/menu/abxy.png").convert_alpha()
    bg = pygame.image.load("Attachments/menu/bg.png").convert_alpha()

    scale_factor = 5

    wasd = pygame.transform.scale(wasd, (wasd.get_width() * scale_factor, wasd.get_height() * scale_factor))
    ijkl = pygame.transform.scale(ijkl, (ijkl.get_width() * scale_factor, ijkl.get_height() * scale_factor))
    moovement = pygame.transform.scale(moovement, (moovement.get_width() * scale_factor, moovement.get_height() * scale_factor))
    llll = pygame.transform.scale(llll, (llll.get_width() * scale_factor, llll.get_height() * scale_factor))
    abxy = pygame.transform.scale(abxy, (abxy.get_width() * scale_factor, abxy.get_height() * scale_factor))

    bg = pygame.transform.scale(bg, (bg.get_width() * scale_factor * 5, bg.get_height() * scale_factor * 5))

    moovement_pos = [screen_width / 2 - moovement.get_width() / 2, 0 + moovement.get_height()]
    wasd_pos = [0 + 1.5 * wasd.get_width(), screen_height / 2 - wasd.get_height()]
    ijkl_pos = [0 + 1.5 * ijkl.get_width(), screen_height / 2 - ijkl.get_height() + ijkl.get_height()]
    llll_pos = [screen_width - 2.5 * wasd.get_width(), screen_height / 2 - wasd.get_height()]
    abxy_pos = [screen_width - 2.5 * wasd.get_width(), screen_height / 2 - ijkl.get_height() + ijkl.get_height() + ijkl.get_height() / 2]
    bg_pos = [screen_width / 2 - bg.get_width() / 2, screen_height / 2 - bg.get_height() / 2]

    screen.blit(bg, bg_pos)
    screen.blit(wasd, wasd_pos)
    screen.blit(ijkl, ijkl_pos)
    screen.blit(abxy, abxy_pos)
    screen.blit(moovement, moovement_pos)
    screen.blit(llll, llll_pos)

    pygame.display.flip()



def main_menu():

    screen = pygame.display.set_mode((0, 0))

    current_menu = "main"

    play_rect, options_rect, quit_rect, start_with_rect, keyboard_rect, controller_rect = draw_main_screen(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if current_menu == "main":
                    if play_rect.collidepoint(mouse_pos):
                        running = False

                    elif options_rect.collidepoint(mouse_pos):
                        options_menu(screen)
                        current_menu = "options"

                    elif quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

                    elif keyboard_rect.collidepoint(mouse_pos):
                        keyboard = True

                    elif controller_rect.collidepoint(mouse_pos):
                        keyboard = False

                elif current_menu == "options":
                    clear_screen(screen, (0, 0, 0))
                    play_rect, options_rect, quit_rect, start_with_rect, keyboard_rect, controller_rect = draw_main_screen(screen)
                    current_menu = "main"

        pygame.display.update()


