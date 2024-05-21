import pygame

class Player():



    def __init__(self, device_index, color):

        self.player_rect = pygame.rect.Rect(0, 0, 100, 100)
        self.color = color

        self.joystick = pygame.joystick.Joystick(device_index)

        self.device_index = device_index

        self.name = self.joystick.get_name()

        # bewegungen Controller
    def moovement_controller(self):

        self.x_moovement = round(self.joystick.get_axis(0)) * 10
        self.y_moovement = round(self.joystick.get_axis(1)) * 10
        self.player_rect.move_ip(self.x_moovement, self.y_moovement)
    def displayer(self, screen):

        pygame.draw.rect(screen, self.color, self.player_rect)






