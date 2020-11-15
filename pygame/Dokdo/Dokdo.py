import pygame
import sys
import random
import time

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1400



white = (255, 255, 255)
black = (0, 0, 0)

GANGCHI_SPEED = 50

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


		gangBtn = pygame.image.load('./res/gangchi_feed.png')
		self.gangBtn = pygame.transform.scale(gangBtn,(400,100))
		self.gangBtnRect = self.gangBtn.get_rect()
		self.gangBtnRect.x = 200
		self.gangBtnRect.y = 1000		#1

		reefBtn = pygame.image.load('./res/amcho_button.png')
		self.reefBtn = pygame.transform.scale(reefBtn,(400,100))
		self.reefBtnRect = self.reefBtn.get_rect()
		self.reefBtnRect.x = 800
		self.reefBtnRect.y = 1000

		cleanBtn = pygame.image.load('./res/clean_button.png')
		self.cleanBtn = pygame.transform.scale(cleanBtn,(400,100))
		self.cleanBtnRect = self.cleanBtn.get_rect()
		self.cleanBtnRect.x = 1400
		self.cleanBtnRect.y = 1000

		mineBtn = pygame.image.load('./res/mining_button.png')
		self.mineBtn = pygame.transform.scale(mineBtn,(400,100))
		self.mineBtnRect = self.mineBtn.get_rect()
		self.mineBtnRect.x = 2000
		self.mineBtnRect.y = 1000


	def drawMain(self):
		background = pygame.Rect((0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.draw.rect(self.screen, white, background)

		text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
		textpos=text.get_rect()
		textpos.x = 50
		textpos.y = 20
		self.screen.blit(text,textpos)

		text=fontSmall.render("Day : "+str(self.day),1,(0,0,0))
		textpos=text.get_rect()
		textpos.x = 2400
		textpos.y = 20
		self.screen.blit(text,textpos)

		self.screen.blit(self.gangBtn,self.gangBtnRect) #2
		self.screen.blit(self.reefBtn,self.reefBtnRect)
		self.screen.blit(self.cleanBtn,self.cleanBtnRect)
		self.screen.blit(self.mineBtn,self.mineBtnRect)


	def saveGangchi(self):
		gangchi_size = (300,300)
		class Fish():
			def __init__(self, size, screen, level, gangchiRect):# size: 1,3,5
				self.size = size
				self.size_px = {1 : (141,67), 3 : (100,100), 5 : (100,100)}
				self.level = level
				
				self.img = pygame.transform.scale(pygame.image.load('./res/fish_'+str(size)+'.png'), self.size_px[self.size])
				self.imgRect = self.img.get_rect()
				self.imgRect.x = random.randint(200,SCREEN_WIDTH-200)
				self.imgRect.y = random.randint(200,SCREEN_HEIGHT-200)
				# homework 겹치면 안겹칠때까지 다시 생성
				while self.collide(gangchiRect):
					self.imgRect.x = random.randint(200,SCREEN_WIDTH-200)
					self.imgRect.y = random.randint(200,SCREEN_HEIGHT-200)
				

				self.screen = screen

				self.v_x = random.randint(-4+level*1, 4+level*1)
				self.v_y = random.randint(-4+level*1, 4+level*1)

			def move(self):
				self.imgRect.x += self.v_x
				self.imgRect.y += self.v_y
				if self.imgRect.x < 0 or self.imgRect.x > SCREEN_WIDTH-self.size_px[self.size][0]:
					self.v_x *= -1
				if self.imgRect.y < 0 or self.imgRect.y > SCREEN_HEIGHT-self.size_px[self.size][1]:
					self.v_y *= -1
				self.screen.blit(self.img, self.imgRect)

			def collide(self, gangchiRect):
				if gangchiRect.x-self.size_px[self.size][0] < self.imgRect.x < gangchiRect.x + gangchi_size[0]:
					if gangchiRect.y-self.size_px[self.size][1] < self.imgRect.y < gangchiRect.y + gangchi_size[1]:
						return True
				return False



		background = pygame.image.load('./res/sea_background.png')
		background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
		backgroundRect = background.get_rect()
		backgroundRect.x = 0
		backgroundRect.y = 0

		self.screen.blit(background,backgroundRect)
		
		
		gangchi = pygame.image.load('./res/gangchi.png')
		gangchi = pygame.transform.scale(gangchi,gangchi_size)
		gangchiRect = gangchi.get_rect()
		gangchiRect.x = 1280
		gangchiRect.y = 700

		fishL = []

		for i in range(5):
			fishL.append(Fish(1,self.screen,self.stage[0], gangchiRect))
			fishL.append(Fish(3,self.screen,self.stage[0], gangchiRect))
			fishL.append(Fish(5,self.screen,self.stage[0], gangchiRect))
		
		while True:
			self.clock.tick(100)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_q:
						return

			keys = pygame.key.get_pressed()

			if (keys[pygame.K_UP]):
				gangchiRect.y -= GANGCHI_SPEED

			if (keys[pygame.K_DOWN]):
				gangchiRect.y += GANGCHI_SPEED

			if (keys[pygame.K_LEFT]):
				gangchiRect.x -= GANGCHI_SPEED

			if (keys[pygame.K_RIGHT]):
				gangchiRect.x += GANGCHI_SPEED


			self.screen.blit(background, backgroundRect)
			



			i = 0
			while i < len(fishL):
				fishL[i].move()
				if fishL[i].collide(gangchiRect):
					self.money += 1
					fishL.remove(fishL[i])
				else:
					i+=1

			if len(fishL) == 0:
				# stage clear code
				font = pygame.font.SysFont('lato',200)
				text = font.render("Stage Clear",True,(28,0,0))
				self.screen.blit(text,(1000,600))
				pygame.display.update()
				time.sleep(1)
				return


			self.screen.blit(gangchi,gangchiRect)

			pygame.display.update()








	def jumpReef(self):
		boat_size = (400,330)
		class reef():
			def __init__(self,reefspeed,screen):
				self.screen = screen
				self.reefspeed = reefspeed
				self.size = (217,160)
				self.img = pygame.transform.scale(pygame.image.load('./res/reef.png'), self.size)
				self.imgRect = self.img.get_rect()
				self.imgRect.x = 2600
				self.imgRect.y = 880
			
			def move(self):
				self.imgRect.x -= self.reefspeed

				self.screen.blit(self.img, self.imgRect)

			def collide(self, boatRect):
				if boatRect.x-self.size[0] < self.imgRect.x < boatRect.x + boat_size[0]:
					if boatRect.y-self.size[1] < self.imgRect.y < boatRect.y + boat_size[1]:
						return True
				return False
			



		
		background = pygame.image.load('./res/sea.png')
		background = pygame.transform.scale(background,(SCREEN_WIDTH,400))
		backgroundRect = background.get_rect()
		backgroundRect.x = 0
		backgroundRect.y = 1000

		sky = pygame.image.load('./res/sky.jpg')
		sky = pygame.transform.scale(sky,(SCREEN_WIDTH,1000))
		skyRect = sky.get_rect()
		skyRect.x = 0
		skyRect.y = 0
		

		boat = pygame.image.load('./res/boat.png')
		boat = pygame.transform.scale(boat,boat_size)
		boatRect = boat.get_rect()
		boatRect.x = 300
		boatRect.y = 700



		isjumping = False

		
		a = 8
		#v = -20
		r_n = 0
		reef_L = [reef(20,self.screen)]
		
		t = time.time()

		while True:

			self.clock.tick(100)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_q:
						return
					if event.key == pygame.K_SPACE:
						if not isjumping:
							isjumping = True
							v = -90
			
			
			if isjumping:
				v+=a
				boatRect.y+=v
				if boatRect.y >= 700:
					isjumping = False
					boatRect.y = 700
					


			self.screen.blit(sky,skyRect)
			self.screen.blit(background,backgroundRect)

			
			if 8 / (r_n + 4) <= time.time()-t:
				t = time.time()
				print ("c@@")
				reef_L.append(reef(20 + r_n * 1,self.screen))
				r_n += 1




			for i in range(len(reef_L)):
				reef_L[i].move()
				if reef_L[i].collide(boatRect):
					pass
					print ("collide")
					#gane over

			if reef_L[0].imgRect.x <= 0:
				reef_L.remove(reef_L[0])
			
			
			self.screen.blit(boat,boatRect)
			pygame.display.update()












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

					if self.reefBtnRect.collidepoint(x, y):
						self.jumpReef() # 3
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
