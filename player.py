import pygame

class Player():

    def __init__(self):
        self.player = pygame.rect.Rect(0, 0, 100, 100)
        self.color = "pink"

    def moovement(self, speedx, speedy):
        self.player.move_ip(speedx, speedy)

    def displayer(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

    def colorer(self, color):
        self.color = color

player = Player()




