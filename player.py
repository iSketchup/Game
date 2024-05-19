import pygame

class Player():



    def __init__(self, device_index):

        self.player = pygame.rect.Rect(0, 0, 100, 100)
        self.color = "pink"
        self.device_index = device_index


        self.joystick = pygame.joystick.Joystick(device_index)

    # bewegungen Controller
    def moovement_controller(self):

        self.x_moovement = round(pygame.joystick.Joystick(0).get_axis(0)) * 10
        self.y_moovement = round(pygame.joystick.Joystick(0).get_axis(1)) * 10
        self.player.move_ip(self.x_moovement, self.y_moovement)

    # bewegung Tastatur
    def moovement_keys(self):

        pressed_keys = pygame.key.get_pressed()
        speed = 10
        x = 0
        y = 0

        if pressed_keys[pygame.K_w or pygame.K_UP]:
            y = -speed
        if pressed_keys[pygame.K_s or pygame.K_DOWN]:
            y = speed
        if pressed_keys[pygame.K_a or pygame.K_RIGHT]:
            x = -speed
        if pressed_keys[pygame.K_d or pygame.K_LEFT]:
            x = speed

        self.player.move_ip(x, y)


    def displayer(self, screen):

        pygame.draw.rect(screen, self.color, self.player)

    def colorer(self, color):
        self.color = color






