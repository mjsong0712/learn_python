import random
import pygame
import time
import sys
pygame.init()

suit_names = ['Clubs','Spades','Hearts','Diamonds']
face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

fontSmall=pygame.font.Font(None,40)
fontBig=pygame.font.Font(None,200)
initialMoney=1000

def create_deck():
	deck=[]
	for i in range(len(suit_names)):
		for j in range(len(face_names)):
			deck.append((face_names[j],suit_names[i],value[j]))
	random.shuffle(deck)
	return deck

def grade(Dealer,Player): # DS, DB, PS, PB, T
	if Dealer.value==21:
		if Player.value==21:
			if len(Dealer.hand)==2:
				if len(Player.hand)==2:
					return 'T'
				return 'DB'
			if len(Player.hand)==2:
				return 'PB'
			return 'T'

		elif len(Dealer.hand)==2:
			return 'DB'
		return 'DS'

	if Player.value==21:
		if len(Player.hand)==2:
			return 'PB'
		return 'PS'

	if Player.value>21:
		return 'DS'

	if Dealer.value>21:
		return 'PS'

	if Dealer.value>Player.value:
		return 'DS'

	if Player.value>Dealer.value:
		return 'PS'

	if Dealer.value==Player.value:
		return 'T'            

class Deck:
	def __init__(self):
		L=create_deck()
		self.deck=[]
		for i in range(len(L)):
			self.deck.append(Card(L[i]))

	def draw(self):
		C = self.deck.pop()
		if len(self.deck)==0:
			print ('creating deck...')
			L=create_deck()
			self.deck=[]
			for i in range(len(L)):
				self.deck.append(Card(L[i]))
		return C

class Card():
	def __init__(self,C,hidden=False):
		self.face=C[0]
		self.suit=C[1]
		self.value=C[2]
		self.hidden=hidden
		self.image='res/'+str(suit_names.index(self.suit)*13+face_names.index(self.face)+1)+'.png'

	def show(self,screen,x,y):
		if self.hidden:
			cardimg=pygame.image.load('res/back_1.png')
		else:
			cardimg=pygame.image.load(self.image)
		cardimg=pygame.transform.scale(cardimg,(90,125))
		cardrect=cardimg.get_rect()
		cardrect.x=x
		cardrect.y=y
		screen.blit(cardimg,cardrect)

class player:
	def __init__(self,money,screen,background,dealer=False):
		self.screen=screen
		self.background=background
		self.money=money
		self.dealer=dealer
		self.hand=[]
		self.value=0
		self.ace=0

	def __str__(self):
		ans=''
		for c in self.hand:
			ans+='('+c.suit+','+c.face+')'
		return ans

	def draw(self,deck):
		c=deck.draw()
		if len(self.hand)==0 and self.dealer:
			c.hidden=True

		self.hand.append(c)

		if c.face=='Ace':
			self.ace+=1

		self.calcvalue()

	def calcvalue(self):
		self.value=0
		for c in self.hand:
			self.value+=c.value
		if self.value<=21:
			return
		elif self.ace>0:
			for i in range(self.ace):
				self.value-=10
				if self.value<=21:
					return

	def clear(self):
		self.hand=[]
		self.ace=False
		self.value=0

class Chip(pygame.sprite.Sprite):
 
	def __init__(self, value, x, y):
		super(Chip,self).__init__()
 
		self.image = pygame.image.load('res/chip_'+str(value)+'.png')
		self.image = pygame.transform.scale(self.image,(80,80))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.value = value



def main():
	screen = pygame.display.set_mode((1280, 760),pygame.FULLSCREEN)
	pygame.display.set_caption("Black Jack Game")
	
	background = pygame.image.load('res/background.png')
	background = pygame.transform.scale(background,(1280,760))
	screen.blit(background, (0, 0))
	
	P=player(initialMoney,screen,background)
	D=player(0,screen,background,True)

	deck=Deck()

	def draw_table(betted_chips=None, deck=deck, c=None, screen=screen, background=background, D=D,P=P):
		screen.blit(background, (0, 0))

		l=len(D.hand)
		x0=640-55*l+10
		for i in range(len(D.hand)):
			D.hand[i].show(D.screen ,x0+i*110,35)

		l=len(P.hand)
		x0=640-55*l+10
		for i in range(len(P.hand)):
			P.hand[i].show(P.screen ,x0+i*110,600)

		all_sprites_list = pygame.sprite.Group()


		chip = Chip(10,910,500)
		all_sprites_list.add(chip)

		chip = Chip(20,1030,500)
		all_sprites_list.add(chip)

		chip = Chip(50,1150,500)
		all_sprites_list.add(chip)

		chip = Chip(100,910,400)
		all_sprites_list.add(chip)

		chip = Chip(500,1030,400)
		all_sprites_list.add(chip)

		chip = Chip(1000,1150,400)
		all_sprites_list.add(chip)

		chips=pygame.image.load('res/chips.png')
		chips=pygame.transform.scale(chips,(150,150))
		chips_rect=chips.get_rect()
		chips_rect.x=1000
		chips_rect.y=150
		screen.blit(chips,chips_rect)

		scoreboard=pygame.image.load('res/scoreboard.png')
		scoreboard=pygame.transform.scale(scoreboard,(200,40))
		scoreboard_rect=scoreboard.get_rect()
		scoreboard_rect.x=970
		scoreboard_rect.y=340
		screen.blit(scoreboard,scoreboard_rect)

		button=pygame.image.load('res/button.png')
		button=pygame.transform.scale(button,(153,41))
		button_rect=button.get_rect()
		button_rect.x=564
		button_rect.y=450
		screen.blit(button,button_rect)

		text=fontSmall.render(str(P.money)+'$',1,(0,0,0))
		textpos=text.get_rect()
		textpos.right=1150
		textpos.y=347
		screen.blit(text,textpos)

		if len(deck.deck)>=5:
			deckimg = pygame.image.load('res/back_5.png')
		else:
			deckimg = pygame.image.load('res/back_'+str(len(deck.deck))+'.png')

		deckimg = pygame.transform.scale(deckimg,(94,130))
		deck_rect = deckimg.get_rect()
		deck_rect.x = 600
		deck_rect.y = 300
		screen.blit(deckimg,deck_rect)

		text=fontSmall.render(str(len(deck.deck)),1,(0,0,0))
		textpos=text.get_rect()
		textpos.x = 700
		textpos.y = 400
		screen.blit(text,textpos)

		if betted_chips!=None:
			betted_chips.draw(screen)

		all_sprites_list.draw(screen)

		pygame.display.flip()
		return all_sprites_list

	keepGoing = True

	while P.money>=10:
		screen.blit(background, (0, 0))
		bet = 0
		betted = pygame.sprite.Group()
		betting=True
		chips = draw_table()
		while betting:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if 564<pos[0]<717 and 450<pos[1]<491:
						betting=False
					clicked_sprites = [s for s in chips if s.rect.collidepoint(pos)]
					for s in clicked_sprites:
						if s.value<=P.money:
							bet+=s.value
							P.money-=s.value
							x=random.randint(30,150)
							y=random.randint(200,350)
							betted.add(Chip(s.value,x,y))
							draw_table(betted)
							pygame.display.flip()

		clock = pygame.time.Clock()

		D.draw(deck)
		draw_table(betted)
		
		P.draw(deck)
		draw_table(betted)
		
		D.draw(deck)
		draw_table(betted)

		P.draw(deck)
		draw_table(betted)

		pygame.display.flip()
		drawing=True
		while drawing:
			if P.value>=21:
				break
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if 564<pos[0]<717 and 450<pos[1]<491:
						P.draw(deck)
						draw_table(betted)
					else:
						drawing=False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
					
				if event.type == pygame.QUIT:
					sys.exit()

		D.hand[0].hidden=False
		#D.show()
		while D.value<17:
			D.draw(deck)

		screen.blit(background, (0, 0))
		draw_table(betted)

		result = grade(D,P)
		print (P,'||',D,' ',result)
		if result=='PS':
			P.money+=int(1.5*bet)
		if result=='PB':
			P.money+=2*bet
		if result=='T':
			P.money+=bet
		if result=='DB':
			P.money-=int(bet*0.5)

		waiting=True
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					waiting=False
		D.clear()
		P.clear()

	screen.blit(background, (0, 0))
	text=fontBig.render('Good Game',1,(0,0,0))
	textpos=text.get_rect()
	textpos.centerx=640
	textpos.centery=380
	screen.blit(text,textpos)
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				sys.exit()
				
if __name__ == "__main__":
	main()
