import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((100, 199))
pygame.display.set_caption('HOLADIEWALDFEE')
clock = pygame.time.Clock()

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()



	pygame.display.update()
	clock.tick(60)