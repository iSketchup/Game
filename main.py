import sys, pygame
from player import Player

def main():

	pygame.init()

	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.display.set_caption('HOLADIEWALDFEE')
	clock = pygame.time.Clock()
	running = True

	#Player init
	player = Player()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.JOYDEVICEADDED:
				stick = pygame.joystick.Joystick(event.device_index)
				sticks.append(stick)

		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
    main()