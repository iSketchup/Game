import pygame
from pygame.locals import *
import sys

pygame.joystick.init()

joysticks = []
for x in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(x)
    joysticks.append(joystick)
print(joysticks)

def joysticker():

    speedx = round(pygame.joystick.Joystick(0).get_axis(0))
    speedy = round(pygame.joystick.Joystick(0).get_axis(1))
    player.moovement(speedx, speedy)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        if event.type == pygame.JOYBUTTONDOWN:

            # Jostick(0) nur weil ich gerade nur eine controller habe
            # sonst der gwünschte von de 2 conrtollern
            # get_button(0) -> in der Klammer der gwünschte button
            if pygame.joystick.Joystick(0).get_button(0):
                player.colorer("pink1")

            elif pygame.joystick.Joystick(0).get_button(1):
                player.colorer("pink2")

            elif pygame.joystick.Joystick(0).get_button(2):
                player.colorer("pink3")

            elif pygame.joystick.Joystick(0).get_button(3):
                player.colorer("pink4")
            print(event)

        if event.type == pygame.JOYAXISMOTION:
            print(event)


class Player():
    def __init__(self):
        self.player = pygame.rect.Rect(0,0,100,100)
        self.color = "pink"

    def moovement(self, speedx, speedy):
        self.player.move_ip(speedx,speedy)

    def displayer(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

    def colorer(self, color):
        self.color = color


player = Player()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300,400))

running = True
while running:

    events()

    screen.fill((255,255,255))
    player.displayer(screen)
    pygame.display.update()
    clock.tick(30)

    joysticker()


