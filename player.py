import pygame

class Player():



    def __init__(self, device_index):
        self.player = pygame.rect.Rect(0, 0, 100, 100)
        self.color = "pink"
        self.device_index = device_index
        #self.moovex = round(pygame.joystick.Joystick(0).get_axis(0))
        #self.moovey = round(pygame.joystick.Joystick(0).get_axis(1))
        
        self.speedx = 10
        self.speedy = 10

        self.joystick = pygame.joystick.Joystick(device_index)


    def moovement(self):

        if self.joystick:
            self.moovex = round(self.joystick.get_axis(0) * self.speedx)
            self.moovey = round(self.joystick.get_axis(1) * self.speedy)

            self.player.move_ip(self.moovex, self.moovey)


    def displayer(self, screen):

        pygame.draw.rect(screen, self.color, self.player)

    def colorer(self, color):
        self.color = color






