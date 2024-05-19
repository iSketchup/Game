import pygame

class Player():



    def __init__(self, device_index):

        self.player = pygame.rect.Rect(0, 0, 100, 100)
        self.color = "pink"
        self.device_index = device_index


        self.joystick = pygame.joystick.Joystick(device_index)


    def moovement(self):

        self.x_moovement = round(pygame.joystick.Joystick(0).get_axis(0)) * 10
        self.y_moovement = round(pygame.joystick.Joystick(0).get_axis(1)) * 10
        self.player.move_ip(self.x_moovement, self.y_moovement)


    def displayer(self, screen):

        pygame.draw.rect(screen, self.color, self.player)

    def colorer(self, color):
        self.color = color






