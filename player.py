import pygame

class Player():
    def __init__(self, device_index, color, rect):

        self.device_index = device_index
        self.player_rect = rect
        self.color = color

        self.joystick = pygame.joystick.Joystick(device_index)
        self.name = self.joystick.get_name()


        self.move = pygame.math.Vector2(0,0)
        self.speed = 10




    def x_movement(self):

        self.move.x = self.joystick.get_axis(0) * self.speed

        if abs(self.move.x) < 0.01:
            self.move.x = 0

    def jump(self):
        pass



    def displayer(self, screen):

        self.x_movement()
        self.jump()
        self.player_rect.move_ip(self.move)
        pygame.draw.rect(screen, self.color, self.player_rect)








