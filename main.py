import pygame
import const



def main():
	pygame.display.set_mode((0,0), pygame.RESIZABLE)
	running = True


	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False






if __name__ == '__main__':
	main()
