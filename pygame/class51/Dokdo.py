import pygame
import sys

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Dokdo Defense")
#screen = pygame.display.set_mode((2560, 1440), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))







def startScreen(screen):
	background = pygame.Rect((0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.draw.rect(screen, white, background)
	
	cardimg=pygame.image.load('res/back_1.png')






		
clock = pygame.time.Clock()
while True:

	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()


	start()








pygame.quit()