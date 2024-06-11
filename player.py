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
        self.jumpheight = 100

        self.lifebarw = 500
        self.lifebarh = 8
        self.lifebarx = 0
        self.lifebary = 16




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
            self.move.y += 10


    def hit(self):
        if self.joystick.get_button(3):
            self.hitbox = pygame.Rect(self.player_rect.x * round(self.joystick.get_axis(0)), self.player_rect.y * round(self.joystick.get_axis(1)), self.player_rect.height, self.player_rect.width)

    def displayer(self, screen):
        pygame.draw.rect(screen, self.color, self.player_rect)
        try:
            pygame.draw.rect(screen, 'blue', self.hitbox)
        except:
            pass
        self.move.x = 0
        self.move.y = 0
        self.x_movement()
        self.jump()
        self.gravity()
        self.hit()
        self.player_rect.move_ip(self.move)






