import pygame
import sys

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1400



white = (255, 255, 255)
black = (0, 0, 0)

pygame.font.init()

fontSmall=pygame.font.Font(None,40)
fontBig=pygame.font.Font(None,200)

def startScreen(screen):
	background = pygame.Rect((0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.draw.rect(screen, white, background)

	img = pygame.image.load('./res/Intro.png')


	imgWidth = 1250
	imgHeight = 1122
	img = pygame.transform.scale(img,(imgWidth,imgHeight))
	rect = img.get_rect()
	rect.x = (SCREEN_WIDTH - imgWidth)//2
	rect.y = (SCREEN_HEIGHT - imgHeight)//2
	screen.blit(img,rect)


class Game():
	def __init__(self, screen):
		self.money = 0
		self.day = 1
		self.stage = [1,1,1,1,1]
		self.clock = pygame.time.Clock()
		self.screen = screen


		gangBtn = pygame.image.load('./res/title.png')
		self.gangBtn = pygame.transform.scale(gangBtn,(400,100))
		self.gangBtnRect = self.gangBtn.get_rect()
		self.gangBtnRect.x = 100
		self.gangBtnRect.y = 1000		#1







	def drawMain(self):
		background = pygame.Rect((0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.draw.rect(self.screen, white, background)
		
		text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
		textpos=text.get_rect()
		textpos.x = 50
		textpos.y = 20
		screen.blit(text,textpos)

		text=fontSmall.render("Day : "+str(self.day),1,(0,0,0))
		textpos=text.get_rect()
		textpos.x = 2400
		textpos.y = 20
		screen.blit(text,textpos)

		self.screen.blit(self.gangBtn,self.gangBtnRect) #2

	def saveGangchi(self):
		pass




	def playGame(self):
		while True:
			#print("bb")
			self.clock.tick(10)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						return
				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					if self.gangBtnRect.collidepoint(x, y):
						self.saveGangchi() # 3
						self.day += 1
						self.stage[0] += 1




			self.drawMain()



			pygame.display.update()












pygame.init()
pygame.display.set_caption("Dokdo Defense")
#screen = pygame.display.set_mode((2560, 1440), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

		
clock = pygame.time.Clock()
startScreen(screen)



gameStart = 0

while not gameStart:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			if event.key == pygame.K_SPACE:
				gameStart = 1

	pygame.display.update()


game = Game(screen)
game.playGame()


pygame.quit()
