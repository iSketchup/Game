import pygame


class Spritesheet(pygame.sprite.Sprite):
	def __init__(self, image_root, measurements):
		super().__init__()
		self.image = pygame.image.load(image_root)
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.width = measurements[0]
		self.height = measurements[1]
		self.frame_list = []

		self.frames()


	def frames(self):
		for row in range(self.image.get_height() // self.height):
			for col in range(self.image.get_width() // self.width):
				image = self.image.subsurface(pygame.Rect(col * self.width, row * self.height, self.width, self.height))
				self.frame_list.append(image)



	def draw(self, screen):
		screen.blit( self.frame_list[0], (0,0))

	def update(self, screen):

		self.draw(screen)
