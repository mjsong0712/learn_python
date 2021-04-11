import pygame
import sys
import random
import time
import math

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440

HP_BAR_WIDTH = int(2560 * 0.9)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 20, 20)

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
		self.money = 10000
		self.day = 99
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
		gangchi_size = (70,70)
		fishsize = {1 : (70,33), 3 : (50,50), 5 : (50,50)}
		class Fish():
			def __init__(self, size, screen, level, gangchiRect):# size: 1,3,5
				self.size = size
				self.level = level
				self.img = pygame.transform.scale(pygame.image.load('./res/fish_'+str(size)+'.png'), fishsize[self.size])
				self.imgRect = self.img.get_rect()
				self.imgRect.x = random.randint(200,SCREEN_WIDTH-200)
				self.imgRect.y = random.randint(200,SCREEN_HEIGHT-200)
				# homework 겹치면 안겹칠때까지 다시 생성
				while self.collide(gangchiRect):
					self.imgRect.x = random.randint(200,SCREEN_WIDTH-200)
					self.imgRect.y = random.randint(200,SCREEN_HEIGHT-200)
				

				self.screen = screen

				self.v_x = random.randint(-4-level*1, 4+level*1)
				self.v_y = random.randint(-4-level*1, 4+level*1)

			def move(self):
				self.imgRect.x += self.v_x
				self.imgRect.y += self.v_y
				if self.imgRect.x < 0 or self.imgRect.x > SCREEN_WIDTH-fishsize[self.size][0]:
					self.v_x *= -1
				if self.imgRect.y < 0 or self.imgRect.y > SCREEN_HEIGHT-fishsize[self.size][1]:
					self.v_y *= -1
				self.screen.blit(self.img, self.imgRect)

			def collide(self, gangchiRect):
				if gangchiRect.x-fishsize[self.size][0] < self.imgRect.x < gangchiRect.x + gangchi_size[0]:
					if gangchiRect.y-fishsize[self.size][1] < self.imgRect.y < gangchiRect.y + gangchi_size[1]:
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

		
		fishN = [4, 6, 7, 8, 9, 10, 10, 10, 10, 11]

		fishL = []

		for i in range(fishN[self.day//10]):
			fishL.append(Fish(1,self.screen,self.stage[0], gangchiRect))
			fishL.append(Fish(3,self.screen,self.stage[0], gangchiRect))
			fishL.append(Fish(5,self.screen,self.stage[0], gangchiRect))
		
		t=time.time()
		
		
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

			timetext=fontSmall.render("%.1f sec"%(15-(time.time()-t)),1,(0,0,0))
			timetextpos=timetext.get_rect()
			timetextpos.x = 50
			timetextpos.y = 90

			text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 20
			

			self.screen.blit(background, backgroundRect)
			self.screen.blit(timetext, timetextpos)
			
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
				pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
				self.screen.blit(text,(1000,600))
				pygame.display.update()
				time.sleep(0.8)
				return

			if 15-(time.time()-t) <= 0:
				font = pygame.font.SysFont('lato',200)
				text=font.render("Time Over",1,(0,0,0))
				textpos=text.get_rect()
				textpos.x = 800
				textpos.y = 800

				pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
				self.screen.blit(text,textpos)
				pygame.display.update()

				time.sleep(0.8)
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

		
		a = 3
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
							v = -60
			
			
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
				interval = random.uniform(1.2 + (3/(r_n+2)), 1.7  + (4/(r_n+2)))
				t = time.time()
				reef_L.append(reef(20 + r_n * 1,self.screen))
				#print(time.time())
				r_n += 1
				




			for i in range(len(reef_L)):
				reef_L[i].move()
				if reef_L[i].collide(boatRect):
					font = pygame.font.SysFont("notosanscjkkr",100)
					text = font.render("GameOver",True,(28,0,0))
					pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
					self.screen.blit(text,(1200,700))
					pygame.display.update()
					time.sleep(0.8)

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
						'iron':(4,10/level),
						'gold':(7,16/level),
						'diamond':(9,20/level)}
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

		
		p = time.time()
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

			timetext=fontSmall.render("%.1f sec"%(30-(time.time()-p)),1,(255,255,255))
			timetextpos=timetext.get_rect()
			timetextpos.x = 50
			timetextpos.y = 90

			text=fontSmall.render("Money : "+str(self.money),1,(255,255,255))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 20

			self.screen.blit(background,backgroundRect)
			self.screen.blit(timetext, timetextpos)
			self.screen.blit(S.img,S.imgRect)
			self.screen.blit(I.img,I.imgRect)
			self.screen.blit(G.img,G.imgRect)
			self.screen.blit(D.img,D.imgRect)
			
			self.screen.blit(text, textpos)


			mspos = pygame.mouse.get_pos()
			pxRect.x, pxRect.y = mspos[0] - 170, mspos[1] - 127
			
			if 30-(time.time()-p) <= 0:
				text=fontBig.render("Time Over",1,(0,0,0))
				textpos=text.get_rect()
				textpos.x = 800
				textpos.y = 500
				pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
				self.screen.blit(text,textpos)
				pygame.display.update()

				time.sleep(0.8)
				return

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
				imgSize = [(134,51),(98,137),(108,126)]
				self.i = random.randint(0,2)
				self.size = imgSize[self.i]
				self.img = pygame.transform.scale(pygame.image.load('./res/'+ imgL[self.i]),self.size)
				self.imgRect = self.img.get_rect()
				self.imgRect.x = random.randint(0,2400)
				self.imgRect.y = random.randint(0,1200)

				while 2050<=self.imgRect.x<=2400 and 850<=self.imgRect.y<=1200:
					self.imgRect.x = random.randint(0,2400)
					self.imgRect.y = random.randint(0,1200)
				

				self.isFalling = 0
				self.isSelected = False
				self.v = 5

			def collide(self,x,y):
				return self.imgRect.collidepoint(x,y)
		
		


		background = pygame.image.load('./res/sea_background.png')
		background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
		backgroundRect = background.get_rect()
		backgroundRect.x = 0
		backgroundRect.y = 0

		trashbin = pygame.image.load('./res/trashbin_front.png')
		trashbin = pygame.transform.scale(trashbin,(380,436))
		trashbinRect = trashbin.get_rect()
		trashbinRect.x = 2200
		trashbinRect.y = 1000

		trashbinb = pygame.image.load('./res/trashbin_back.png')
		trashbinb = pygame.transform.scale(trashbinb,(380,436))
		trashbinbRect = trashbinb.get_rect()
		trashbinbRect.x = 2200
		trashbinbRect.y = 1000





		
		trashL = []
		for i in range(15+int(self.stage[2]*1.5)):
			trashL.append(Trash())

		
		T = [0 for i in range(len(trashL))]

		n = -1
		dx, dy = 0,0
		t = time.time()
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
							if not trashL[i].isSelected:
								tx = trashL[i].imgRect.x
								ty = trashL[i].imgRect.y
								dx = tx - x
								dy = ty - y
								n = i
								break


				if event.type == pygame.MOUSEBUTTONUP and 0 <= n:
					x, y = event.pos
					if trashbinRect.x <= trashL[n].imgRect.x and \
					trashL[n].imgRect.x + trashL[n].size[0] <= trashbinRect.x + 380 and \
					trashL[n].imgRect.y + trashL[n].size[1] <= trashbinRect.y and  \
					trashbinRect.y - 500 <= trashL[n].imgRect.y:

						trashL[n].isFalling = 1
						trashL[n].isSelected = True
						print("o")
					else:
						trashL[n].imgRect.x = tx
						trashL[n].imgRect.y = ty
					
					n = -1
					
					
					# HOMEWORk!
					# 보스 스테이지(침략) 기획, 사진 따오기

			
			

			timetext=fontSmall.render("%.1f sec"%(30-(time.time()-t)),1,(0,0,0))
			timetextpos=timetext.get_rect()
			timetextpos.x = 50
			timetextpos.y = 20

			text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 50
			
			if 0 <= n:
				mspos = pygame.mouse.get_pos()
				trashL[n].imgRect.x = mspos[0] + dx
				trashL[n].imgRect.y = mspos[1] + dy
				

			self.screen.blit(background,backgroundRect)
			self.screen.blit(timetext, timetextpos)
			self.screen.blit(trashbinb,trashbinbRect)
			self.screen.blit(text, textpos)
			
			for i in range(len(trashL)):
				if trashL[i].isFalling == 1:
					trashL[i].imgRect.y += trashL[i].v
					trashL[i].v += 1
					if trashL[i].imgRect.y -5 >= trashbinRect.y:
						trashL[i].isFalling = 0
						self.money += 1
						T[i] = 1

				self.screen.blit(trashL[i].img,trashL[i].imgRect)


			self.screen.blit(trashbin,trashbinRect)
			

			u = 1
			for i in range(len(T)):

				if T[i] == 0:
					u = 0
					break
			if u == 1 :
				font = pygame.font.SysFont('lato',200)
				text=font.render("Clear",1,(0,0,0))
				textpos=text.get_rect()
				textpos.x = 1200
				textpos.y = 600

				pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
				self.screen.blit(text,textpos)
				pygame.display.update()

				time.sleep(0.8)
				return

			if 30-(time.time()-t) <= 0:
				font = pygame.font.SysFont('lato',200)
				text=font.render("Time Over",1,(0,0,0))
				textpos=text.get_rect()
				textpos.x = 1200
				textpos.y = 600


				self.screen.blit(text,textpos)
				pygame.display.update()

				time.sleep(0.8)
				return
			pygame.display.update()

	
	def bossStage(self):
		stage = int(self.day / 10)
		boss_hp = 2000
		monster_hp = [10, 20, 25, 35, 40, 50, 55, 60, 100, boss_hp]
		
		class monster():
			def __init__(self,stage,monsterspeed):
				self.stage = stage
				self.monsterspeed = monsterspeed
				self.monster_size = {1 : (108,133), 2 : (381,265), 3 : (294,412), 4 : (336,338), 5 : (325,396), 6 : (387,360), 7 : (337,350), 8 : (350,384), 9 : (462,341), 10 : (462,341)}
				self.monster_hp = monster_hp[self.stage-1]
				self.monster = pygame.transform.scale(pygame.image.load('./res/monster'+str(stage)+'.png'), self.monster_size[stage])
				self.monsterRect = self.monster.get_rect()
				self.monsterRect.x = 2000
				self.monsterRect.y = random.randint(50, 1100)

			def move(self):
				self.monsterRect.x -= self.monsterspeed

		class Gun():
			def __init__(self,size):
				self.size = size
				self.size_px = {1 : (329,227), 2 : (381,203), 3 : (861,223), 4 : (687,324)}
				self.rect = {1 : (200,100), 2 : (200, 400), 3 : (200, 700), 4 : (200,1000)}
				self.offset = {1 : (-50,0), 2 : (-50, 0), 3 : (-180, 0), 4 : (-150,0)}
				self.priceL = {1 : 10, 2 : 50, 3 : 100, 4 : 500}
				self.img = pygame.transform.scale(pygame.image.load('./res/gun'+str(size)+'.png'), self.size_px[self.size])
				self.imgRect = self.img.get_rect()
				self.imgRect.x = self.rect[self.size][0]
				self.imgRect.y = self.rect[self.size][1]
				self.pricebtn = pygame.transform.scale(pygame.image.load('./res/gun'+str(size)+'price.png'), (209,128))
				self.pricebtnRect = self.pricebtn.get_rect()
				self.pricebtnRect.x = self.rect[self.size][0] + self.size_px[self.size][0] + 100
				self.pricebtnRect.y = self.rect[self.size][1]

		def slotSelect(slotL):
			N = [1,2,3,4]
			pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
			text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 20
			self.screen.blit(text, textpos)
			S = []

			for i in range(4):
				slotbtn = pygame.image.load('./res/slotgun' +str(slotL[i]) +'.png')
				slotbtn = pygame.transform.scale(slotbtn,(342,158))
				slotbtnRect = slotbtn.get_rect()
				slotbtnRect.x = (400*N[i])+200
				slotbtnRect.y = 600
				self.screen.blit(slotbtn,slotbtnRect)
				S.append(slotbtnRect)

			
			


			pygame.display.update()
			print("while in")
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							sys.exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						x, y = event.pos
						for i in range(len(N)):
							if S[i].collidepoint(x, y):
								if slotL[i] == 0:
									self.screen.blit(slotbtn,slotbtnRect)
									pygame.display.update()
									return i

		G0 = Gun(1)
		G1 = Gun(2)
		G2 = Gun(3)
		G3 = Gun(4)

		L = [G0, G1, G2, G3]
		slotL = [0,0,0,0]

		shoptext = pygame.image.load('./res/shopText.png')
		shoptext = pygame.transform.scale(shoptext,(564, 289))
		shoptextRect = shoptext.get_rect()
		shoptextRect.x = 1000
		shoptextRect.y = 50	

		battlebtn = pygame.image.load('./res/battlestartbtn.png')
		battlebtn = pygame.transform.scale(battlebtn,(484, 179))
		battlebtnRect = battlebtn.get_rect()
		battlebtnRect.x = 1800
		battlebtnRect.y = 1000


		monsterL = []




		def drawShop(slotL):
			text=fontSmall.render("Money : "+str(self.money),1,(0,0,0))
			textpos=text.get_rect()
			textpos.x = 50
			textpos.y = 20



			pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
			for i in range(4):
				slotbtn = pygame.image.load('./res/slotgun' +str(slotL[i]) +'.png')
				slotbtn = pygame.transform.scale(slotbtn,(200,100))
				slotbtnRect = slotbtn.get_rect()
				slotbtnRect.x = 2000
				slotbtnRect.y = 200+(200*i)
				self.screen.blit(slotbtn, slotbtnRect)

			self.screen.blit(shoptext, shoptextRect)
			self.screen.blit(G0.img, G0.imgRect)
			self.screen.blit(G0.pricebtn, G0.pricebtnRect)
			self.screen.blit(G1.img, G1.imgRect)
			self.screen.blit(G1.pricebtn, G1.pricebtnRect)
			self.screen.blit(G2.img, G2.imgRect)
			self.screen.blit(G2.pricebtn, G2.pricebtnRect)
			self.screen.blit(G3.img, G3.imgRect)
			self.screen.blit(G3.pricebtn, G3.pricebtnRect)
			self.screen.blit(text, textpos)

			self.screen.blit(battlebtn, battlebtnRect)
			pygame.display.update()

		

		def battle(slotL):
			class Explosion:
				def __init__(self, x, y):
					self.timer = time.time()

					self.img = pygame.image.load('./res/gun4explode.png')
					self.img = pygame.transform.scale(self.img, (123,133))

					self.imgRect = self.img.get_rect()
					self.imgRect.x = x + 40
					self.imgRect.y = y - 40



			class Bullet:

				def __init__(self, level, startPos, angle, screen):
					self.level = level
					self.screen = screen
					self.startPos = startPos
					self.angle = angle
					self.vx = 10 * math.cos(self.angle)
					self.vy = 10 * math.sin(self.angle)

					# hw 총알들 크기 조정해서 화면에 종류별로 다 띄우기
					self.sizeL = {1:(43, 26), 2:(72, 23), 3:(65, 16), 4:(113, 23)}
					self.offset = {1:(100,70,140), 2:(150,70,140), 3:(500,70,140), 4:(370,130,140)}
					self.damage = {1:1, 2:3, 3:5, 4:10} 
					self.img = pygame.image.load('./res/bullet'+str(level)+'.png')
					self.img = pygame.transform.scale(self.img,self.sizeL[self.level])
					
					self.img = pygame.transform.rotate(self.img, -1*self.angle * 180 / math.pi)

					self.imgRect = self.img.get_rect()


					self.imgRect.x = startPos[0] + self.offset[self.level][0] + math.cos(self.angle)*self.offset[self.level][2]
					self.imgRect.y = startPos[1] + self.offset[self.level][1] + math.sin(self.angle)*self.offset[self.level][2]

				def move(self):
					
					self.imgRect.x += int(self.vx)
					self.imgRect.y += int(self.vy)
					self.screen.blit(self.img, self.imgRect)

					
					

			pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)

			
			GunL = []
			BulletL = []
			expL = []
			for i in range(4):
				if slotL[i] != 0:
					G = Gun(slotL[i])
			
					G.img = pygame.transform.scale(G.img,(G.size_px[slotL[i]][0]//2, G.size_px[slotL[i]][1]//2))
					G.imgRect = G.img.get_rect()
					G.imgRect.x = 10 + G.offset[G.size][0]
					G.imgRect.y = 150 + (250*i) + G.offset[G.size][1]

					GunL.append(G)
					# print(BulletL)


					#self.screen.blit(G.img, G.imgRect)



			killed_cnt = 0
			spawned_cnt = 0
			monstersL = [30, 35, 50, 40, 40, 30, 20, 20, 5, 0]
			speedL = 	[3,  3,  3,  4,  5,  3,  2,  4,  2, 1]
			
			monsters = monstersL[int(self.day/10)-1]

			bossmob = monster(10, 1)
			t = time.time()

			t1 = time.time()

			
			blt_rsp = False

			cleartext=fontBig.render("Clear",1,(0,0,0))
			cleartextpos=cleartext.get_rect()
			cleartextpos.x = 1100
			cleartextpos.y = 600

			monsterSpawningHp = [1400, 1100, 800, 500, 200, -100]
			spawningMonsterLevel = [1,3,5,7,9]
			mshIndex = 0
			while True:
				self.clock.tick(100)
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							sys.exit()
	
				pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)

				for i in range(len(BulletL)):
					BulletL[i].move()

				if self.day != 100:
					text=fontSmall.render(str(killed_cnt) + "/"+str(monsters),1,(0,0,0))
					textpos=text.get_rect()
					textpos.x = 50
					textpos.y = 20
					self.screen.blit(text, textpos)
				else:
					text=fontSmall.render("Boss Stage",1,(0,0,0))
					textpos=text.get_rect()
					textpos.x = 30
					textpos.y = 50
					self.screen.blit(text, textpos)

				if self.day == 100 and bossmob.monster_hp <= 0:
					bossmob.monsterspeed = 0
					bossmob.monsterRect.x = 100
					bossmob.monsterRect.y = -1000



				if self.day == 100:	
					bossmob.move()
					self.screen.blit(bossmob.monster, bossmob.monsterRect)
				
				for i in range(len(monsterL)):
					monsterL[i].move()
					self.screen.blit(monsterL[i].monster, monsterL[i].monsterRect)


				if expL and time.time() - expL[0].timer > 0.15:
					expL = expL[1:]

				for i in range(len(expL)):
					self.screen.blit(expL[i].img, expL[i].imgRect)
				

				if (self.day == 100 and bossmob.monsterRect.x <= 0) or (monsterL and monsterL[0].monsterRect.x <= 0):
					# monsterL.remove(monsterL[0])
					font = pygame.font.SysFont('lato',200)
					text=font.render("Game Over",1,(0,0,0))
					textpos=text.get_rect()
					textpos.x = 1000
					textpos.y = 600

					pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
					self.screen.blit(text, textpos)
					pygame.display.update()
					time.sleep(0.8)
					return 0




				if time.time() - t1 >= 0.3:
					blt_rsp = True
					
					t1 = time.time()




				for i in range(len(GunL)):

					Gx = GunL[i].imgRect.x + GunL[i].size_px[GunL[i].size][0]//2
					Gy = GunL[i].imgRect.y + GunL[i].size_px[GunL[i].size][1]//2

					mspos = pygame.mouse.get_pos() 
					angle = math.atan2(mspos[0]- Gx, mspos[1]- Gy) - math.pi/2

					if blt_rsp:
						Blt = Bullet(GunL[i].size,(GunL[i].imgRect.x, GunL[i].imgRect.y),-1*angle,self.screen)
						BulletL.append(Blt)

					angle = angle * 180 / math.pi
					rot_gun = pygame.transform.rotate(GunL[i].img, angle)
					rot_rect = rot_gun.get_rect(center= (Gx,Gy))
					self.screen.blit(rot_gun, rot_rect)

				if blt_rsp:
					blt_rsp = False


				i = 0
				
				while i < len(BulletL):
					if self.day == 100:
						tmp = monsterL[:] + [bossmob]
					else:
						tmp = monsterL
					isRemoved = False
					# print(len(BulletL))
					blt = BulletL[i]
					for j in range(len(tmp)):
						if tmp[j].monsterRect.x - blt.sizeL[blt.level][0] <= blt.imgRect.x <= tmp[j].monsterRect.x + tmp[j].monster_size[tmp[j].stage][0]:
							if tmp[j].monsterRect.y - blt.sizeL[blt.level][1] <= blt.imgRect.y <= tmp[j].monsterRect.y + tmp[j].monster_size[tmp[j].stage][1]:
								if blt.level == 4:
									expL.append(Explosion(blt.imgRect.x, blt.imgRect.y))
								BulletL.remove(blt)
								isRemoved = True
								tmp[j].monster_hp -= blt.damage[blt.level]

								break


					if isRemoved == False:
						i += 1

				j = 0
				while j < len(monsterL):
					if monsterL[j].monster_hp <= 0:
						monsterL.remove(monsterL[j])
					else:
						j += 1

					#self.screen.blit(GunL[i].img, GunL[i].imgRect)

				if (self.day != 100 and killed_cnt >= monsters) or (self.day == 100 and monsterL == [] and bossmob.monster_hp <= 0): # fix
					pygame.draw.rect(self.screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)
					self.screen.blit(cleartext, cleartextpos)
					pygame.display.update()
					time.sleep(0.8)
					return 1

				if self.day == 100:
					pygame.draw.rect(self.screen, black, [200, 50, HP_BAR_WIDTH+5, 50], 2)
					if 0 < HP_BAR_WIDTH-int((boss_hp-bossmob.monster_hp)*(HP_BAR_WIDTH/boss_hp)):
						pygame.draw.rect(self.screen, red, [203, 53, HP_BAR_WIDTH-int((boss_hp-bossmob.monster_hp)*(HP_BAR_WIDTH/boss_hp)), 45])
				

				

				if bossmob.monster_hp < monsterSpawningHp[mshIndex]:
					for i in range(5):
						monsterL.append(monster(spawningMonsterLevel[mshIndex],speedL[spawningMonsterLevel[mshIndex]-1]))
					mshIndex += 1
				pygame.display.update()


				if time.time()-t >= 1:
					if spawned_cnt < monsters:
						monsterL.append(monster(stage,speedL[stage-1]))
						spawned_cnt += 1
						t = time.time()
					


				

			############### 다음 시간
			# 화면 밖 총알
			# 뭐 하나 더 있었는데 뭐더라





		drawShop(slotL)

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					for i in range(len(L)):
						if L[i].pricebtnRect.collidepoint(x, y):
							if self.money >= L[i].priceL[L[i].size]:
								if 0 in slotL:
									self.money -= L[i].priceL[L[i].size]
									selected = slotSelect(slotL)
									slotL[selected] = i+1
								

									drawShop(slotL)
							else:
								text=fontSmall.render("Not available for purchase",1,(0,0,0))
								textpos=text.get_rect()
								textpos.x = 700
								textpos.y = 20
								self.screen.blit(text, textpos)
								pygame.display.update()
								time.sleep(1)
								drawShop(slotL)
						if battlebtnRect.collidepoint(x, y):
							result = battle(slotL)
							return result

							

					

						
						
					pygame.display.update()




	def playGame(self):
		while True:
			if self.day % 10 == 0:
				result = self.bossStage()
				
				if result == 0:
					return 0
				else:
					self.day += 1
			#print("bb")
			self.clock.tick(10)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_r:
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


while True:

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
	result = game.playGame()

	if result == 0:
		continue
	if result == 1:
		pygame.draw.rect(screen, white, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT],0)

		text=fontSmall.render("Game clear",1,(0,0,0))
		textpos=text.get_rect()
		textpos.x = 700
		textpos.y = 20

		screen.blit(text, textpos)

		pygame.display.update()
		time.sleep(3)
		break






pygame.quit()
pygame.display.update()