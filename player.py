import pygame
class Player():
    def __init__(self, device_index, rect, colidables, tilesize, controllers, screen_width):

        self.device_index = device_index
        self.player_rect = rect
        self.color = 'blue'

        self.joystick = pygame.joystick.Joystick(device_index)
        self.name = self.joystick.get_name()

        self.tilesize = tilesize
        self.controller_num = (len(controllers) % 2) + 1
        self.screen_width = screen_width

        self.controllers = controllers

        self.move = pygame.math.Vector2(0,0)
        self.speed = 10

        self.collidables = colidables

        self.ground = True
        self.jumpheight = 100

        self.hp = self.tilesize * 15

        self.dead = False




    def x_movement(self):

        self.move.x = self.joystick.get_axis(0) * self.speed

        if abs(self.move.x) < 0.01:
            self.move.x = 0

        if self.player_rect.x + self.player_rect.width > self.screen_width:
            self.move.x = 0
            self.player_rect.x = self.screen_width - self.player_rect.width

        elif self.player_rect.x < 0:
            self.move.x = 0
            self.player_rect.x = 0

    def jump(self):

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


    def hitting(self):
        self.hitbox = None

        hit_direction = pygame.math.Vector2(round(self.joystick.get_axis(0)), round(self.joystick.get_axis(1)))
        hit_direction.x = self.player_rect.width * hit_direction.x

        hit_direction.y = self.player_rect.height * hit_direction.y

        if self.joystick.get_button(3):
            self.hitbox = pygame.Rect(self.player_rect.x + hit_direction.x, self.player_rect.y + hit_direction.y,
                                      self.player_rect.height, self.player_rect.width)

    def being_hit(self):
        hit = self.controllers[(self.controller_num-1)]

        for controller in self.controllers:

            if controller.controller_num == 1:
                try:
                    hit = self.controllers[0]
                except IndexError:
                    pass
            else:
                try:
                    hit = self.controllers[1]
                except IndexError:
                    pass

        hit = hit.player_rect

        if self.player_rect.colliderect(hit):
            self.hp -= 1


    def hp_bar(self):

        height_hp = self.tilesize * 2
        width_hp = self.tilesize * 15

        self.hp_bars = []
        self.damage_bars = []

        if self.controller_num == 1:
            x_c = 0
            y_c = 0

            if self.hp == 0:
                self.dead = True
            else:
                hp_rect = pygame.Rect(x_c, y_c, width_hp / self.hp, height_hp)
                self.hp_bars.append(hp_rect)

            damage = pygame.Rect(x_c, y_c, width_hp, height_hp)
            damage.left = x_c

            self.damage_bars.append(damage)



        #0 means 2 here bc 2 % 2 = 0
        elif self.controller_num == 2:
            x_c = self.screen_width - width_hp
            y_c = 0

            if self.hp == 0:
                self.dead = True
            else:
                hp_rect = pygame.Rect(x_c, y_c, width_hp / self.hp, height_hp)
                self.hp_bars.append(hp_rect)

            damage = pygame.Rect(x_c, y_c, width_hp, height_hp)


            self.damage_bars.append(damage)


    def displayer(self, screen, controllers):

        self.controllers = controllers

        pygame.draw.rect(screen, self.color, self.player_rect)
        self.hp_bar()

        for rect in self.damage_bars:
            pygame.draw.rect(screen, "red", rect)

        for rect in self.hp_bars:
            pygame.draw.rect(screen, "green", rect)



        self.move.x = 0
        self.move.y = 0
        self.x_movement()
        self.jump()
        self.gravity()
        self.hitting()

        self.player_rect.move_ip(self.move)
        self.being_hit()
        try:

            pygame.draw.rect(screen, 'pink', self.hitbox)
        except TypeError:
           pass




