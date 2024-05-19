import pygame

class Player():



    def __init__(self, device_index):
        self.player = pygame.rect.Rect(0, 0, 100, 100)
        self.color = "pink"
        self.device_index = device_index
        self.moovex = round(pygame.joystick.Joystick(0).get_axis(0))
        self.moovey = round(pygame.joystick.Joystick(0).get_axis(1))
        self.speedx = 10
        self.speedy = 10

    def moovement(self):
        self.player.move_ip(self.moovex, self.moovey)

    def displayer(self, screen):
        pygame.draw.rect(screen, self.color, self.player)

    def colorer(self, color):
        self.color = color






