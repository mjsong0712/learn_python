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
		self.stage = [1,1,1,1]
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
			
			text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 20
			self.screen.blit(text, textpos)

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

			self.screen.blit(text,textpos)
			self.screen.blit(gangchi,gangchiRect)

			pygame.display.update()








	def jumpReef(self):
		boat_size = (300,248)
		class reef():
			def __init__(self,reefspeed,screen):
				self.screen = screen
				self.reefspeed = reefspeed
				self.size = (173,128)
				self.img = pygame.transform.scale(pygame.image.load('./res/reef.png'), self.size)
				self.imgRect = self.img.get_rect()
				self.imgRect.x = 2600
				self.imgRect.y = 910
			
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
		boatRect.x = 220
		boatRect.y = 760

		text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
		textpos=text.get_rect()
		textpos.x = 50
		textpos.y = 20
		



		isjumping = False

		
		a = 5
		#v = -20
		r_n = 0
		reef_L = [reef(20,self.screen)]
		
		t = time.time()
		interval = random.uniform(2,3)
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
							v = -80
			
			
			if isjumping:
				v+=a
				boatRect.y+=v
				if boatRect.y >= 760:
					isjumping = False
					boatRect.y = 760
					


			self.screen.blit(sky,skyRect)
			self.screen.blit(background,backgroundRect)
			text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 20
			self.screen.blit(text, textpos)
			
			if interval <= time.time()-t:
				interval = random.uniform(0.5 + (3/(r_n+2)), 1 + (4/(r_n+2)))
				t = time.time()
				reef_L.append(reef(20 + r_n * 1,self.screen))
				print(time.time())
				r_n += 1
				




			for i in range(len(reef_L)):
				reef_L[i].move()
				if reef_L[i].collide(boatRect):
					font = pygame.font.SysFont("notosanscjkkr",100)
					text = font.render("GameOver",True,(28,0,0))
					self.screen.blit(text,(1200,700))
					pygame.display.update()
					time.sleep(1)

					return


			if reef_L and reef_L[0].imgRect.x <= 0:
				reef_L.remove(reef_L[0])
				self.money += 1
			
			
			self.screen.blit(boat,boatRect)
			pygame.display.update()


	def Mine(self):
		level = 1
		if 20 <= self.money and self.money < 40:
			level = 2
		if 40 <= self.money and self.money < 60:
			level = 3
		if 60 <= self.money and self.money < 80:
			level = 4
		if 80 <= self.money:
			level = 5
		mineral_info = {'stone':(2,5/level),
						'iron':(5,10/level),
						'gold':(10,17/level),
						'diamond':(20,20/level)}
		class mineral():
			def __init__(self,itemname):
				self.itemname = itemname
				self.size = {'stone':(380,310),'iron':(370,352),'gold':(370,352),'diamond':(308,288)}
				self.img = pygame.transform.scale(pygame.image.load('./res/'+self.itemname+'.png'),self.size[itemname] )
				self.imgRect = self.img.get_rect()
				self.price = mineral_info[itemname][0]
				self.time = mineral_info[itemname][1]

			

			def collide(self, pos):
				x, y = pos
				if self.imgRect.x < x < self.imgRect.x + self.size[self.itemname][0]:
					if self.imgRect.y < y < self.imgRect.y + self.size[self.itemname][1]:
						return True
				return False



		background = pygame.image.load('./res/cave.jpg')
		background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
		backgroundRect = background.get_rect()
		backgroundRect.x = 0
		backgroundRect.y = 0

		D = mineral('diamond')
		D.imgRect.x, D.imgRect.y = 300, 600

		G = mineral('gold')
		G.imgRect.x, G.imgRect.y = 800, 600
		
		I = mineral('iron')
		I.imgRect.x, I.imgRect.y = 1300, 600
		
		S = mineral('stone')
		S.imgRect.x, S.imgRect.y = 1800, 600



# money따라 바뀌는걸로 수정
		pxL = [(340,255),(305,293),(202,192),(331,331),(331,331)]
		
		


		px = pygame.image.load('./res/Lv'+str(level)+'Px.png')
		px = pygame.transform.scale(px,(pxL[level-1][0],pxL[level-1][1]))
		pxRect = px.get_rect()


		minerals = [None, D, G, I, S]
		isClicking = 0

		while True:
			self.clock.tick(100)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						return
				if event.type == pygame.MOUSEBUTTONDOWN:
					t = time.time()
					for i in range(1,5):
						if minerals[i].collide(event.pos):
							isClicking = i
				if event.type == pygame.MOUSEBUTTONUP:
					isClicking = 0



			self.screen.blit(background,backgroundRect)
			self.screen.blit(S.img,S.imgRect)
			self.screen.blit(I.img,I.imgRect)
			self.screen.blit(G.img,G.imgRect)
			self.screen.blit(D.img,D.imgRect)
			text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 20
			self.screen.blit(text, textpos)

			mspos = pygame.mouse.get_pos()
			pxRect.x, pxRect.y = mspos[0] - 170, mspos[1] - 127
			
			def calcAngle(angle, maxangle):
				angle = int(angle)
				if (angle//maxangle) % 2 == 0:
					return angle % maxangle
				return 2 * maxangle - angle % (2 * maxangle)

			if isClicking:
				angle = calcAngle(((time.time()-t))*200, 30)
				rot_px = pygame.transform.rotate(px, angle)
				self.screen.blit(rot_px, rot_px.get_rect(center=mspos))

				if not minerals[isClicking].collide(mspos):
					isClicking = 0
				else:
					if time.time()-t >= minerals[isClicking].time:
						self.money += minerals[isClicking].price
						print("fin")
						isClicking = 0
			else:

				self.screen.blit(px, pxRect)



			pygame.display.update()
		

	def clean(self):
		class Trash():
			def __init__(self):
				imgL = ['pet.png','pet2.png','paper.png']
				self.img = pygame.image.load('./res/'+random.choice(imgL))
				self.imgRect = self.img.get_rect()
				self.imgRect.x = random.randint(0,2400)
				self.imgRect.y = random.randint(0,1200)

			def collide(self,x,y):
				return self.imgRect.collidepoint(x,y)


		background = pygame.image.load('./res/sea_background.png')
		background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
		backgroundRect = background.get_rect()
		backgroundRect.x = 0
		backgroundRect.y = 0

		trashbin = pygame.image.load('./res/trashbin.png')
		trashbin = pygame.transform.scale(trashbin,(380,436))
		trashbinRect = trashbin.get_rect()
		trashbinRect.x = 2200
		trashbinRect.y = 1000
		
		trashL = []
		for i in range(5):
			trashL.append(Trash())

		n = -1
		dx, dy = 0,0

		while True:
			self.clock.tick(100)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						return
				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					for i in range(len(trashL)):
						if trashL[i].collide(x, y):
							tx = trashL[i].imgRect.x
							ty = trashL[i].imgRect.y
							dx = tx - x
							dy = ty - y
							n = i
							break


				if event.type == pygame.MOUSEBUTTONUP and 0 <= n:
					trashL[n].imgRect.x = tx
					trashL[n].imgRect.y = ty
					n = -1
					# HOMEWORk! 휴지통 위에 있는지 확인
					# 보스 스테이지(침략) 기획, 사진 따오기


			
			if 0 <= n:
				mspos = pygame.mouse.get_pos()
				trashL[n].imgRect.x = mspos[0] + dx
				trashL[n].imgRect.y = mspos[1] + dy
				

			self.screen.blit(background,backgroundRect)
			self.screen.blit(trashbin,trashbinRect)
			for i in range(len(trashL)):
				self.screen.blit(trashL[i].img,trashL[i].imgRect)
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
						self.stage[1] += 1

					if self.mineBtnRect.collidepoint(x, y):
						self.Mine() # 3
						self.day += 1
						self.stage[2] += 1

					if self.cleanBtnRect.collidepoint(x, y):
						self.clean()
						self.day += 1
						self.stage[3] += 1




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
