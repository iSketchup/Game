import pygame
import sys

pygame.joystick.init()

joysticks = []
for x in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(x)
    joysticks.append(joystick)

if len(joysticks)<1:
    print("No controllers Connected")
    sys.exit()
else:
    print(f"Controllers Connected: {joysticks}")



print(joysticks)


def joysticker():

    speedx = round(pygame.joystick.Joystick(0).get_axis(0))
    speedy = round(pygame.joystick.Joystick(0).get_axis(1))
    player.moovement(speedx, speedy)



class Player():

    ,
    def __init__(self):
        self.player = pygame.rect.Rect(0, 0, 100, 100)
        self.color = "pink"

    def moovement(self, speedx, speedy):
        self.player.move_ip(speedx, speedy)

    def displayer(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

    def colorer(self, color):
        self.color = color

player = Player()




