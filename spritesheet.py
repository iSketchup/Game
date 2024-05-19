import pygame


class Spritesheet():
	def __init__(self, image_root, measurments):
		self.image = pygame.image.load(image_root)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()

	def draw(self, screen):
		pygame.draw.rect(screen, 'pink', self.rect)
		screen.blit(self.image, (0, 0))

