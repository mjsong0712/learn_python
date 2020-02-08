"""
 Simple snake example.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import random
import sys
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
# Set initial speed
x_change = segment_width + segment_margin	
y_change = 0
 
class Block(pygame.sprite.Sprite):
	"""
	This class represents the ball.
	It derives from the "Sprite" class in Pygame.
	"""
 
	def __init__(self, color, width, height):
		""" Constructor. Pass in the color of the block,
		and its x and y position. """
 
		# Call the parent class (Sprite) constructor
		super(Block, self).__init__()
 
		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
 
		# Fetch the rectangle object that has the dimensions of the image
		# image.
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()

class Segment(pygame.sprite.Sprite):
	""" Class to represent one segment of the snake. """
	# -- Methods
	# Constructor function
	def __init__(self, x, y):
		# Call the parent's constructor
		super(Segment, self).__init__()
 
		# Set height, width
		self.image = pygame.Surface([segment_width, segment_height])
		self.image.fill(WHITE)
 
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

def segmentcollide(segment_list):
	l=len(segment_list)
	if (segment_list[0].rect.x<0 or segment_list[0].rect.y<0 or segment_list[0].rect.x>screen_width-10 or segment_list[0].rect.y>screen_height-10):return True
	for i in range(l):
		for j in range(i+1,l):
			if [segment_list[i].rect.x,segment_list[i].rect.y]==[segment_list[j].rect.x,segment_list[j].rect.y]:
				return True
	return False

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 700x400 sized screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
while True:

	x_change = segment_width + segment_margin
	y_change = 0
	
	block_list = pygame.sprite.Group()
	 
	# This is a list of every sprite. 
	# All blocks and the player block as well.
	all_sprites_list = pygame.sprite.Group()

	for i in range(50):
		# This represents a block
		block = Block(RED, 20, 15)
	 
		# Set a random location for the block
		block.rect.x = random.randrange(screen_width-15)
		block.rect.y = random.randrange(screen_height-15)
	 
		# Add the block to the list of objects
		block_list.add(block)
		all_sprites_list.add(block)
	# Set the title of the window
	pygame.display.set_caption('Snake Example')
	 
	# Create an initial snake
	snake_segments = []
	for i in range(50):
		x = - (segment_width + segment_margin) * i
		y = 200
		segment = Segment(x, y)
		snake_segments.append(segment)
		all_sprites_list.add(segment)
	 
	 
	clock = pygame.time.Clock()
	done = False
	score=0
	while not done:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	 
			# Set the speed based on the key pressed
			# We want the speed to be enough that we move a full
			# segment, plus the margin.
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = (segment_width + segment_margin) * -1
					y_change = 0
				if event.key == pygame.K_RIGHT:
					x_change = (segment_width + segment_margin)
					y_change = 0
				if event.key == pygame.K_UP:
					x_change = 0
					y_change = (segment_height + segment_margin) * -1
				if event.key == pygame.K_DOWN:
					x_change = 0
					y_change = (segment_height + segment_margin)
	 
		# Get rid of last segment of the snake
		# .pop() command removes last item in list
		old_segment = snake_segments.pop()
		all_sprites_list.remove(old_segment)

		# Figure out where new segment will be
		x = snake_segments[0].rect.x + x_change
		y = snake_segments[0].rect.y + y_change
		segment = Segment(x, y)

		if segmentcollide(snake_segments):
		
			gameover=True
			go = pygame.image.load('resource/image/Game_Over.jpg')
			gorect = go.get_rect()
			gorect.x = 100
			gorect.y = 100
			screen.fill(BLACK)
			screen.blit(go,gorect)
			screen.blit(textsurface,(600,0))
			pygame.display.flip()
			while gameover:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
						gameover=False
					if event.type == pygame.QUIT:
						sys.exit()
			break
						
		player=snake_segments[0]
		blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
	 
		# Check the list of collisions.
		for block in blocks_hit_list:
			score += 1
			


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# Insert new segment into the list
		snake_segments.insert(0, segment)
		all_sprites_list.add(segment)

		textsurface = myfont.render('SCORE: '+str(score), False, WHITE)
		if score==50:
			gameover=True
			go = pygame.image.load('resource/image/YouWin.png')
			gorect = go.get_rect()
			gorect.x = 28
			gorect.y = 50
			screen.fill(BLACK)
			screen.blit(textsurface,(600,0))
			screen.blit(go,gorect)
			pygame.display.flip()
			
			while gameover:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
						gameover=False
					if event.type == pygame.QUIT:
						sys.exit()
			break
		# -- Draw everything
		# Clear screen
		screen.fill(BLACK)
		screen.blit(textsurface,(600,0))
	 
		all_sprites_list.draw(screen)
	 
		# Flip screen
		pygame.display.flip()
	 
		# Pause
		clock.tick(10)

	continue

pygame.quit()