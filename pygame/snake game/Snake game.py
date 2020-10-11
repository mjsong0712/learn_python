"""
 Simple snake example.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import time
from datetime import datetime
from datetime import timedelta

GREEN = (0,255,0)
BLACK = (100,100,200)
WHITE = (255,255,255)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLOCK_SIZE = 20

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def draw_background(screen):
	background = pygame.Rect((0,0), (SCREEN_WIDTH, SCREEN_WIDTH))
	pygame.draw.rect(screen, BLACK, background)

def draw_block(screen, color, position):
	block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
	pygame.draw.rect(screen, color, block)

class Snake:
	def __init__(self):
		self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)] 
		self.direction = 'north'  
		self.color = WHITE
	
	def draw(self, screen):
		for position in self.positions:
			draw_block(screen, self.color, position)
   
	def crawl(self):
		head_position = self.positions[0]
		if self.direction == 'north':
			head_position -= 1

		elif self.direction == 'south':
			head_position += 1

		elif self.direction == 'west':
			head_position -= 1

		elif self.direction == 'east':
			head_position += 1
		



class Apple:  
	def __init__(self, position=(5, 5)):
		self.position = position
		self.color = GREEN
	def draw(self, screen):
		draw_block(screen, self.color, self.position)


class GameBoard:
	width = 20  
	height = 20  

	def __init__(self):
		self.snake = Snake()  
		self.apple = Apple()

	def draw(self, screen):
		self.apple.draw(screen)
		self.snake.draw(screen)

game_board = GameBoard()

DIRECTION_ON_KEY = {
	pygame.K_UP: 'north',
	pygame.K_DOWN: 'south',
	pygame.K_LEFT: 'west',
	pygame.K_RIGHT: 'east',

}
block_direction = 'east'
block_position = [0,0]
last_moved_time = datetime.now()

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key in DIRECTION_ON_KEY:
				block_direction = DIRECTION_ON_KEY[event.key]

	if timedelta(seconds = 1) <= datetime.now() - last_moved_time:
		pass
		#last_moved_time = datetime.now()

	draw_background(screen)

	game_board.draw(screen)
	pygame.display.update()