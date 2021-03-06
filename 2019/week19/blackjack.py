# -*- coding: utf-8 -*-
# 변수명 예시
# L, M, N
# list, number_list, numbers
# input

# 함수 사용시 f1(input), f2()
# 변수 사용시 v1 = v2 + v3

# range(5) == [0, 1, 2, 3, 4]
# [0 for i in range(5)] == [0, 0, 0, 0, 0]

# m = m + 1 <=> m += 1 

# a<c and c<b <=> a<c<b

# 바꾸기: a,b = b,a

# 리스트 원소 추가 L.append(a)

# L.sort()

# L = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9,10,11,12]]
# len(L) == 3
# L[0] == [1,2,3,4]
# L[0][0] == 1
# len(L[0]) == 4

# 입력: a = raw_input("enter input")

# a in B: boolean(True/False)
# var in [1, 2, 3]

import random

class Card:
	def __init__(self,number,face,hidden):
		self.number = number
		self.face = face
		self.hidden = hidden

	def __str__(self):
		if self.hidden:
			return "(?????????)"
		else:
			return "("+str(self.number)+","+self.face+")"
class Player:
	def __init__(self):
		self.hand = []
		self.money = money

	def show(self):
		l = len(self.hand)
		for i in range(l):
			print self.hand[i],
		print

	def countnumber(self):
		l = len(self.hand)
		SUM = 0
		for i in range(l):
			if self.hand[i].number in ["J", "Q", "K"]:
				SUM += 10
			else:
				SUM += self.hand[i].number
		return SUM 

class Deck:
	def __init__(self):
		self.cards = [] 
		self.genCards()

	def genCards(self):
		faces = [[1,"spade  "],[1,"clover "],[1,"heart  "],[1,"diamond"],[2,"spade  "],[2,"clover "],[2,"heart  "],[2,"diamond"],[3,"spade  "],[3,"clover "],[3,"heart  "],[3,"diamond"],[4,"spade  "],[4,"clover "],[4,"heart  "],[4,"diamond"],[5,"spade  "],[5,"clover "],[5,"heart  "],[5,"diamond"],[6,"spade  "],[6,"clover "],[6,"heart  "],[6,"diamond"],[7,"spade  "],[7,"clover "],[7,"heart  "],[7,"diamond"],[8,"spade  "],[8,"clover "],[8,"heart  "],[8,"diamond"],[9,"spade  "],[9,"clover "],[9,"heart  "],[9,"diamond"],[10,"spade  "],[10,"clover "],[10,"heart  "],[10,"diamond"],["J","spade  "],["J","clover "],["J","heart  "],["J","diamond"],["Q","spade  "],["Q","clover "],["Q","heart  "],["Q","diamond"],["K","spade  "],["K","clover "],["K","heart  "],["K","diamond"]]
		for c in faces:
			self.cards.append(Card(c[0],c[1],True))
		random.shuffle(self.cards)

	def deal(self):
		if self.cards == []:
			self.genCards()
		return self.cards.pop()





money = 1000
print "############ black jack ############"
print "your money :", money
print
while 1:
	betMoney = int(raw_input("bet :"))
	deck = Deck()
	player = Player()
	dealer = Player()
	player.hand.append(deck.deal()) 
	dealer.hand.append(deck.deal()) 
	player.hand.append(deck.deal()) 
	dealer.hand.append(deck.deal())
	player.hand[0].hidden = False
	player.hand[1].hidden = False
	dealer.hand[1].hidden = False
	print
	print "player: ",
	player.show()
	print "dealer: ",
	dealer.show()
	print

	while 1:
		if raw_input("stop or go: ") == 'stop':
			print
			break
		else:
			print
			c = deck.deal()
			c.hidden = False
			player.hand.append(c)
			if player.countnumber() > 21:
				break
			print "player: ",
			player.show()
			print "dealer: ",
			dealer.show()
			print

	dealer.hand[0].hidden = False
	
	while dealer.countnumber() < 17 :
		c = deck.deal()
		c.hidden = False
		dealer.hand.append(c)
	print
	print "player: ",
	player.show()
	print "dealer: ",
	dealer.show()
	ps = player.countnumber()
	ds = dealer.countnumber()
	if ps > 21 or ps < ds <= 21:
		print "you lose!!!"
		money -= betMoney
	elif ps == ds:
		print "draw!!!"
	else:
		print "you win!!!"
		money += betMoney

	print
	print "your money :", money
	print "##############################"
	if raw_input("continue?(yes/no)") == 'no':
		break




