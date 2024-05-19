import sys, pygame
from player import Player
from spritesheet import Spritesheet



def heart(screen):
	def heart():
		heart = Spritesheet('Attachments/UI/heart.png', 1234)

		heart.draw(screen)


def main():

	pygame.init()

	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.display.set_caption("1 vs 1")
	clock = pygame.time.Clock()
	running = True

	#cotroler zeug
	controllers = []

	# Player init
	player = Player(3)

	while running:

		screen.fill('white')


		player.displayer(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.JOYDEVICEADDED:
				controller = pygame.joystick.Joystick(event.device_index)
				controllers.append(controller)

			for controller in controllers:
				#moovement left and right
				if controller.get_axis(0):
					player.moovement()
				# up and down
				elif controller.get_axis(1):
					player.moovement()


			heart(screen)

		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
    main()