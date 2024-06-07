import pygame

class Player():
    def __init__(self, device_index, rect, colidables):

        self.device_index = device_index
        self.player_rect = rect
        self.color = 'blue'

        self.joystick = pygame.joystick.Joystick(device_index)
        self.name = self.joystick.get_name()


        self.move = pygame.math.Vector2(0,0)
        self.speed = 10

        self.collidables = colidables

        self.ground = True
        self.jumpheight = 10




    def x_movement(self):

        self.move.x = self.joystick.get_axis(0) * self.speed

        if abs(self.move.x) < 0.01:
            self.move.x = 0

    def jump(self):
        print(self.jumpheight, self.ground, self.move)

        #if A is pressed this returns True
        if self.joystick.get_button(2):
            if self.ground:
                self.move.y = - self.jumpheight
                self.ground = False


    def gravity(self):

        for rect in self.collidables:
            if self.player_rect.colliderect(rect):
                self.ground = True

        if not self.ground:
            self.move.y += 1





    def displayer(self, screen):
        pygame.draw.rect(screen, self.color, self.player_rect)
        self.move.x = 0
        self.move.y = 0
        self.x_movement()
        self.jump()
        self.gravity()
        self.player_rect.move_ip(self.move)








