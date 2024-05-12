import pygame
from main import *

class Player:
    def __init__(self, x, y, rect):
        self.rect = pygame.Rect(x, y, 200, 200)
        self.x = x
        self.y = y

    def moovement(self):
        joysticks = []
        if event.type == pygame.JOYDEVICEADDED:
            print(event)





