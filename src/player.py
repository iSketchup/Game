import time
import pygame

import menu
from spritesheet import Spritesheet

class Player():
    def __init__(self, device_index, colidables, tilesize, controllers, screen, upsizefaktorw, keyboard):

        self.idle = Spritesheet('assets/knight/Idle.png', (48, 64))
        self.run_right = Spritesheet('assets/knight/Run_right.png',(48, 64))
        self.run_left = Spritesheet('assets/knight/Run.png',(48, 64))
        self.attack = Spritesheet('assets/knight/Attack1.png',(64, 80))
        self.jumping = Spritesheet('assets/knight/Jump.png',(48, 64))
        self.hit = Spritesheet('assets/knight/Take Hit.png',(64, 64))

        self.current_state = self.idle
        self.player_rect = self.idle.frame_list[0].get_rect()


        self.last_update = pygame.time.get_ticks()
        self.update_rate = 140
        self.cur_frame = 0

        self.device_index = device_index

        try:
            self.joystick = pygame.joystick.Joystick(device_index)
            self.name = self.joystick.get_name()
        except pygame.error:
            self.joystick = None

        self.tilesize = tilesize
        self.controller_num = (len(controllers) % 2) + 1

        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.controllers = controllers

        self.move = pygame.math.Vector2(0,0)
        self.speed = 10

        self.collidables = colidables

        self.ground = False
        self.jumpheight = 100

        self.hp = self.tilesize * 15 / 100
        self.dead = False
        self.keyboard = keyboard

        self.done = False
        self.rekord = None
        self.currenttime = None
        self.starting_time = time.perf_counter()

        if self.controller_num == 2:
            self.player_rect.x = self.screen_width - tilesize * upsizefaktorw



    def x_movement(self):

        if not self.keyboard:
            self.move.x = self.joystick.get_axis(0) * self.speed

            if abs(self.move.x) < 0.05:
                self.move.x = 0

            if self.move.x < 0 :
                self.current_state = self.run_left

            elif self.move.x > 0 :
                self.current_state = self.run_right

            if self.player_rect.x + self.player_rect.width > self.screen_width:
                self.move.x = 0
                self.player_rect.x = self.screen_width - self.player_rect.width

            elif self.player_rect.x < 0:
                self.move.x = 0
                self.player_rect.x = 0
        else:

            self.pressed_keys = pygame.key.get_pressed()

            if self.controller_num == 1:

                if self.pressed_keys[pygame.K_d] == True:
                    self.move.x = self.speed

                elif self.pressed_keys[pygame.K_a] == True:
                    self.move.x = - self.speed

            else:
                if self.pressed_keys[pygame.K_l] == True:
                    self.move.x = self.speed

                elif self.pressed_keys[pygame.K_j] == True:
                    self.move.x = - self.speed

            if self.move.x < 0:
                self.current_state = self.run_left

            elif self.move.x > 0:
                self.current_state = self.run_right


            if self.player_rect.x + self.player_rect.width > self.screen_width:
                self.move.x = 0
                self.player_rect.x = self.screen_width - self.player_rect.width

            elif self.player_rect.x < 0:
                self.move.x = 0
                self.player_rect.x = 0

    def jump(self):
        if not self.keyboard:
            #if A is pressed this returns True
            if self.joystick.get_button(2):
                if self.ground:
                    self.move.y = - self.jumpheight
                    self.ground = False
                else:
                    self.current_state = self.jumping
        else:
            if self.controller_num == 1:
                if self.pressed_keys[pygame.K_w]:
                    if self.ground:
                        self.move.y = - self.jumpheight
                        self.ground = False
                    else:
                        self.current_state = self.jumping
            elif self.controller_num == 2:
                if self.pressed_keys[pygame.K_i]:
                    if self.ground:
                        self.move.y = - self.jumpheight
                        self.ground = False
                    else:
                        self.current_state = self.jumping

    def gravity(self):

        for rect in self.collidables:
            if self.player_rect.colliderect(rect):
                self.player_rect.y = self.screen_height - (self.player_rect.height + (self.screen_height - rect.y))
                self.ground = True

        if not self.ground:
            self.move.y += 10


    def hitting(self):
        self.hitbox = None

        if not self.keyboard:
            hit_direction = pygame.math.Vector2(round(self.joystick.get_axis(0)), round(self.joystick.get_axis(1)))

        elif self.controller_num == 1:
            x_value = 0
            y_value = 0

            if self.pressed_keys[pygame.K_w]:
                x_value += 1
            if self.pressed_keys[pygame.K_s]:
                x_value -= 1

            if self.pressed_keys[pygame.K_d]:
                y_value += 1
            if self.pressed_keys[pygame.K_a]:
                y_value -= 1
            hit_direction = pygame.math.Vector2(x_value, y_value)
        else:
            x_value = 0
            y_value = 0

            if self.pressed_keys[pygame.K_i]:
                x_value += 1
            if self.pressed_keys[pygame.K_k]:
                x_value -= 1

            if self.pressed_keys[pygame.K_l]:
                y_value += 1
            if self.pressed_keys[pygame.K_j]:
                y_value -= 1
            hit_direction = pygame.math.Vector2(x_value, y_value)

        hit_direction.x = self.player_rect.width * hit_direction.x
        hit_direction.y = self.player_rect.height * hit_direction.y

        if not self.keyboard:
            if self.joystick.get_button(3):
                self.hitbox = pygame.Rect(self.player_rect.x + hit_direction.x, self.player_rect.y + hit_direction.y,
                                          self.player_rect.height, self.player_rect.width)
                self.current_state = self.attack

        elif self.controller_num == 1:
            if self.pressed_keys[pygame.K_c]:
                self.hitbox = pygame.Rect(self.player_rect.x + hit_direction.x, self.player_rect.y + hit_direction.y,
                                          self.player_rect.height, self.player_rect.width)
                self.current_state = self.attack
        else:
            if self.pressed_keys[pygame.K_n]:
                self.hitbox = pygame.Rect(self.player_rect.x + hit_direction.x, self.player_rect.y + hit_direction.y,
                                          self.player_rect.height, self.player_rect.width)
                self.current_state = self.attack

    def being_hit(self):

        if self.controller_num == 1:
            try:
                hit = self.controllers[1]
            except IndexError:
                pass
        elif self.controller_num == 2:
            try:
                hit = self.controllers[0]
            except IndexError:
                pass

        try:
            hit = hit.hitbox

            if self.player_rect.colliderect(hit):
                self.hp += 5
                self.current_state = self.hit

        except:
            pass



    def hp_bar(self):
        height_hp = self.tilesize * 2
        width_hp = self.tilesize * 15

        print(self.hp)
        print(width_hp)

        self.hp_bars = []
        self.damage_bars = []

        if self.controller_num == 1:
            x_c = 0
            y_c = 0

            if self.hp >= width_hp:
                self.dead = True


            else:
                hp_rect = pygame.Rect(x_c, y_c, width_hp - self.hp, height_hp)
                self.hp_bars.append(hp_rect)

            damage = pygame.Rect(x_c, y_c, width_hp, height_hp)
            damage.left = x_c

            self.damage_bars.append(damage)



        #0 means 2 here bc 2 % 2 = 0
        elif self.controller_num == 2:
            x_c = self.screen_width - width_hp
            y_c = 0

            if self.hp >= width_hp:
                self.dead = True
            else:
                hp_rect = pygame.Rect(x_c, y_c, width_hp - self.hp, height_hp)
                self.hp_bars.append(hp_rect)

            damage = pygame.Rect(x_c, y_c, width_hp, height_hp)


            self.damage_bars.append(damage)


    def animat(self, counter):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.update_rate:

            counter += 1
            self.last_update = now
        return counter


    def displayer(self):

        self.cur_frame = self.animat(self.cur_frame)

        print(self.current_state.col_count)


        self.screen.blit(self.current_state.frame_list[(self.cur_frame) % self.current_state.col_count], self.player_rect)

        if (self.cur_frame) % self.current_state.col_count == 0:
            self.current_state = self.idle

        for rect in self.damage_bars:
            pygame.draw.rect(self.screen, "red", rect)

        for rect in self.hp_bars:
            pygame.draw.rect(self.screen, "green", rect)

    def update(self, controllers):
        self.controllers = controllers
        self.hp_bar()
        self.move.x = 0
        self.move.y = 0
        self.x_movement()
        self.jump()
        self.gravity()
        self.hitting()

        self.player_rect.move_ip(self.move)
        self.being_hit()

        self.displayer()

        if self.dead == True:
            self.done, self.rekord, self.currenttime = menu.death_screen(self.screen, self.controller_num, self.done, self.rekord, self.currenttime, self.starting_time)



