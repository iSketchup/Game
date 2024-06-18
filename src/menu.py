import csv
import time

import pygame
import sys


def file_reader(name, start):
    with open(name, 'r') as file:

        line = file.readline()
        line = float(line)
        print(line)

    now = time.perf_counter()

    now = now - start


    with open(name, 'w') as file:
        if line > now:
            print('sdafsdafs')
            file.write(str(now))
        else:
            file.write(str(line))

    return line, now


def text_objects(text):
    font = pygame.font.SysFont('Courier New', 30)
    textSurface = font.render(text, True, 'black')
    textSurface = textSurface.convert_alpha()
    return textSurface, textSurface.get_rect()

def death_screen(screen, looser_num, done, rekord, currenttime, start):

    if not done:
        rekord, currenttime = file_reader('assets/highscore.csv', start)
        currenttime = float(currenttime)



    if float(rekord) > currenttime:
        txtsurf, txt_rect = text_objects(f'{round(currenttime,2)} beats the Highscore!')
        done = True

    else:
        txtsurf, txt_rect = text_objects(f'{round(currenttime,2)} does not beat the Highscore!')
        done = True

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    x = (screen_width / 2)
    y = (screen_height / 3 * 2)



    bg = pygame.image.load("assets/menu/bg.png").convert_alpha()
    player1 = pygame.image.load("assets/menu/player1.png").convert_alpha()
    player2 = pygame.image.load("assets/menu/player2.png").convert_alpha()

    scale_factor = 5

    bg = pygame.transform.scale(bg, (bg.get_width() * scale_factor * 5, bg.get_height() * scale_factor * 5))
    player1 = pygame.transform.scale(player1, (scale_factor * player1.get_width(), scale_factor * player1.get_height()))
    player2 = pygame.transform.scale(player2, (scale_factor * player2.get_width(), scale_factor * player2.get_height()))

    bg_pos = [screen_width / 2 - bg.get_width() / 2, screen_height / 2 - bg.get_height() / 2]
    player1_rect = player1.get_rect(center=(screen_width / 2, screen_height / 2))
    player2_rect = player2.get_rect(center=(screen_width / 2, screen_height / 2))

    txt_rect.centerx = x
    txt_rect.centery = player2_rect.bottom + 20

    screen.blit(bg, bg_pos)

    if looser_num == 2:
        screen.blit(player1, player1_rect)
    else:
        screen.blit(player2, player2_rect)

    screen.blit(txtsurf, txt_rect)
    return done, rekord, currenttime


def draw_main_screen(screen):

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    play = pygame.image.load("assets/menu/play.png").convert_alpha()
    options = pygame.image.load("assets/menu/options.png").convert_alpha()
    quit = pygame.image.load("assets/menu/quit.png").convert_alpha()

    start_with = pygame.image.load("assets/menu/start with.png").convert_alpha()
    keyboard = pygame.image.load("assets/menu/keyboard.png").convert_alpha()
    controller = pygame.image.load("assets/menu/controller.png").convert_alpha()

    bg = pygame.image.load("assets/menu/bg.png").convert_alpha()
    bgbg = pygame.image.load("assets/menu/bgbg.png").convert_alpha()
    logo = pygame.image.load("assets/menu/logo.png").convert_alpha()

    scale_factor = 5

    bgbg = pygame.transform.scale(bgbg, (screen_width, screen_height))
    logo = pygame.transform.scale(logo, (logo.get_width() * scale_factor, logo.get_height() * scale_factor))
    bg = pygame.transform.scale(bg, (bg.get_width() * scale_factor*2, bg.get_height() * scale_factor*2))

    play = pygame.transform.scale(play, (play.get_width() * scale_factor, play.get_height() * scale_factor))
    options = pygame.transform.scale(options, (options.get_width() * scale_factor, options.get_height() * scale_factor))
    quit = pygame.transform.scale(quit, (quit.get_width() * scale_factor, quit.get_height() * scale_factor))

    play_rect = play.get_rect(center=(screen_width / 2, screen_height / 2 - 100))
    options_rect = options.get_rect(center=(screen_width / 2, screen_height / 2))
    quit_rect = quit.get_rect(center=(screen_width / 2, screen_height / 2 + 100))

    start_with_rect = start_with.get_rect(center=(screen_width - screen_width + bg.get_width() / 2 + start_with.get_width()/2, screen_height / 2 - 100))
    keyboard_rect = keyboard.get_rect(center=(screen_width - screen_width + bg.get_width() /2, screen_height/2))
    controller_rect = controller.get_rect(center=(screen_width - screen_width + bg.get_width(), screen_height /2))

    bg_pos = [screen_width - screen_width + bg.get_width() / 4.5, screen_height / 2 - 150]
    bgbg_pos = [screen_width / 2 - bgbg.get_width() / 2, screen_height / 2 - bgbg.get_height() / 2]
    logo_pos = [screen_width / 2 - logo.get_width() / 2, screen_height / 2 - 2.6 * logo.get_height()]

    screen.blit(bgbg, bgbg_pos)
    screen.blit(logo, logo_pos)
    screen.blit(bg, bg_pos)

    screen.blit(play, play_rect)
    screen.blit(options, options_rect)
    screen.blit(quit, quit_rect)

    screen.blit(start_with, start_with_rect)
    screen.blit(keyboard, keyboard_rect)
    screen.blit(controller, controller_rect)


    pygame.display.flip()

    return play_rect, options_rect, quit_rect, start_with_rect, keyboard_rect, controller_rect

def clear_screen(screen, color):
    screen.fill(color)
    pygame.display.flip()

def options_menu(screen):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    bgbg = pygame.image.load("assets/menu/bgbg.png").convert_alpha()
    bgbg = pygame.transform.scale(bgbg, (screen_width, screen_height))
    bgbg_pos = [screen_width / 2 - bgbg.get_width() / 2, screen_height / 2 - bgbg.get_height() / 2]
    screen.blit(bgbg, bgbg_pos)

    wasd = pygame.image.load("assets/menu/wasd.png").convert_alpha()
    ijkl = pygame.image.load("assets/menu/ijkl.png").convert_alpha()
    moovement = pygame.image.load("assets/menu/movement.png").convert_alpha()
    llll = pygame.image.load("assets/menu/llll.png").convert_alpha()
    abxy = pygame.image.load("assets/menu/abxy.png").convert_alpha()
    bg = pygame.image.load("assets/menu/bg.png").convert_alpha()

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

    keyboard = True

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
                    play_rect, options_rect, quit_rect, start_with_rect, keyboard_rect, controller_rect = draw_main_screen(screen)
                    current_menu = "main"

                elif current_menu == "death":

                    play_rect, options_rect, quit_rect, start_with_rect, keyboard_rect, controller_rect = draw_main_screen(
                        screen)
                    current_menu = "main"


        pygame.display.update()
    return keyboard


