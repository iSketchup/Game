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
		self.row_count = self.image.get_height() // self.height
		self.col_count = self.image.get_width() // self.width
		self.frames()


	def frames(self):
		for row in range(self.row_count):
			for col in range(self.col_count):
				image = self.image.subsurface(pygame.Rect(col * self.width, row * self.height, self.width, self.height))
				image = pygame.transform.scale(image, (self.width * 4, self.height*4))
				self.frame_list.append(image)
