# -*- coding: utf-8 -*-
###################################################
#  HangMan
#  Class No :      
#  Studnet ID :
#  Name :                                             ==> IN ENGLISH
###################################################
import random
import time
from cs1graphics import * 
###################################################
class Card(object):
	
	def __init__(self, word, kind ):

		self.word = word     #str
		self.kind = kind     #str

###################################################

class Deck(object):   
	
	def __init__(self): 
		i = 0
		self.cards = []
		f = open("./data.txt")
		L = f.readlines()

		# self.cards  안에 data의 정보로 생성한 card object를 append 

		for line in L:
			ls = line.split()
			C1 = Card(ls[0], ls[1])
			self.cards.append(C1)
		random.shuffle(self.cards)
		print self.cards
	def draw(self):
		return self.cards.pop()


###################################################


class Button(object) :
	
	def __init__(self , key, centerPt ) :
		self.key = key
		self.centerPt = centerPt
		self.clicked = False 
 
	def select (self ) :
		self.clicked = True

	def release (self ) :
		self.clicked = False  
		
###################################################
class ButtonGraphic (object):
	
	def __init__ (self, button , layer  ) :
		self.button = button
		self.layer = layer
		self.size =  30
	  
		self.shape =  Square (self.size , self.button.centerPt)
		self.shape.setFillColor ('yellow')
		self.shape.setDepth(30)  
					
		self.text  = Text (self.button.key)    
		self.text.setFontColor('black')
		self.text.setFontSize(10)
		self.text.setDepth(20)
		


		self.text.moveTo(self.button.centerPt.getX(),self.button.centerPt.getY()) # <= Text 클래스로 만든 오브젝트에 포함된 함수 ex T1.moveTo(x,y)


		self.layer.add(self.shape)   
		self.layer.add(self.text)        
	
	def select (self ) :
		self.layer.remove(self.shape)
	 
	def release (self ) :
		self.layer.add(self.shape)

###################################################
class Keyboard(object) :
	
	def __init__ (self, x,y,canvas) :
		self.l = Layer() 
		self.x = x
		self.y = y
		self.canvas = canvas
		self.l.setDepth(30)   
		self.l.moveTo(self.x, self.y)   
  
		keys = [ ('Q', 5, 5 ), ('W' , 40, 5  ) ,('E', 75, 5), ('R', 110 ,5) , ('T', 145 ,5) ,('Y', 180, 5), ('U', 215,5), ('I', 250 ,5) ,('O' ,285, 5) ,('P', 320, 5) , ('A',  15 ,40 ), ('S' , 50 , 40) , ('D', 85, 40), ('F',120, 40) , ('G', 155,40), ('H', 190, 40 ), ('J' ,225 ,40 ), ('K' , 260,  40), ('L' ,295,40) , ('Z', 25, 75) , ('X', 60, 75), ('C',95,75) , ('V', 130,75) , ('B', 165,75), ('N', 200,75), ('M', 235,75) ]     
		
		self.keys = []
		self.keyGraphics = []

		for i in range(len(keys)):
			P1 = Point(keys[i][1], keys[i][2])	
			B1 = Button(keys[i][0], P1)

			self.keys.append(B1)
			self.keyGraphics.append(ButtonGraphic(B1,self.canvas))



		self.canvas.add(self.l)

	def click (self, i)  :   
		self.keys[i].select()
		self.keyGraphics[i].select()
	
	def clear(self) : # 버튼이 clicked면 버튼이랑 그래픽 클릭해제 해주기
		for i in range(len(self.keys)):
			if self.keys[i].clicked:
				self.keys[i].release()
			else:
				self.keys[i].select()



	def findKey (self , x, y ) :
		###########################
		#  [5] Implement Here         #
		pass  # delete this line after complete this method
		########################### 
	
###################################################

class Prisoner ():
	
	def __init__ (self, x,y,canvas) :
		self.l = Layer() 
		self.x = x
		self.y = y
		self.canvas = canvas
		self.l.setDepth(40)   
		self.step = 0
		
		p0 = Circle (15 , Point (120,45  )  )
		p1 = Path (Point (120,60  ) , Point (120,105 )  )
		p2 = Path (Point (120,75  ) , Point (75,63 )  )
		p3 = Path (Point (120,75 ) , Point (165,63  )  )                
		p4 = Circle (3 , Point (75,63 )  )        
		p5 = Circle (3 , Point (165,63 )  )
		p6 = Path (Point ( 120,105 ) , Point ( 80,135  ) , Point( 70,120 ) )        
		p7 = Path (Point ( 120,105) , Point ( 160,135  ) , Point( 170,120 ) )   # ==> right leg     
		
		self.pList = [p0,p1,p2,p3,p4,p5,p6,p7]
		
		for i in self.pList:            
			i.setBorderWidth(6)
		
		self.l.moveTo (self.x, self.y)
		self.canvas.add(self.l )      
		

	def hang (self):     
		###########################
		#  [6] Implement Here         #
		pass  # delete this line after complete this method
		###########################


	def die (self) :
		
		###########################
		# [7] Implement Here         #
		pass  # delete this line after complete this method
		###########################        
   
	def run (self) : 
		###########################
		#  [8] Implement Here         #
		pass  # delete this line after complete this method
		###########################        
	 
	def clear (self, success):    
		###########################
		#  [9] Implement Here         #
		pass  # delete this line after complete this method
		###########################        
	 

		 
				 
###################################################
class Scaffold ():
	
	def __init__ (self,x,y,canvas) :
		self.l = Layer() 
		self.x = x
		self.y = y
		self.canvas = canvas        
		self.l.setDepth(40)

		s1 = Path ( Point(30,150), Point (60,150))
		s2 = Path ( Point(45,15), Point (45,150))
		s3 = Path ( Point(45,15), Point (120,15))
		s4 = Path ( Point(120,15), Point (120,30))

		sList = [s1,s2,s3,s4]
		
		for i in sList :
			i.setBorderWidth(6)
			self.l.add (i)     
			
		self.l.moveTo (self.x, self.y)
		self.canvas.add(self.l )
	
	def down (self) :
		###########################
		#  [10]Implement Here         #
		pass  # delete this line after complete this method
		###########################     

	def up (self) :
		###########################
		# [11] Implement Here         #
		pass  # delete this line after complete this method
		###########################     
		
		
###################################################
class Table (object) :
	
	def __init__ (self):
		self.canvas = Canvas(800, 650, ' lemonchiffon', 'Hang Man')      
		self.title = Image ('hangman.png')
		self.title.moveTo (400,80)       
		self.canvas.add(self.title)
		
		self.scaffold = Scaffold (550,400, self.canvas)
		self.prisoner = Prisoner ( 550,400, self.canvas )
		self.keyboard = Keyboard(100, 450 ,self.canvas )

		self.cardWord  = Text("_")
		self.cardWord.setFontColor('red')
		self.cardWord.setFontSize(35)
		self.cardWord.moveTo(400, 200)
		self.canvas.add(self.cardWord )
 
		self.cardKind  = Text("_")
		self.cardKind.setFontColor('blue')
		self.cardKind.setFontSize(20)
		self.cardKind.moveTo(400,270)
		self.canvas.add(self.cardKind )
		
		self.message = Text("Click on the letters to guess which letters are in this word. \n Make 8 wrong guesses and you lost.")
		self.message.setFontColor('blue')
		self.message.setFontSize(15)
		self.message.moveTo(400,350)
		self.canvas.add(self.message)
  
		self.ask = Text("")   # Another round ? (y/n)
		self.ask.setFontColor('blue')
		self.ask.setFontSize(15)
		self.ask.moveTo(400, 600)
		self.canvas.add(self.ask)
						
		self.words  = Deck()
			  
	def changeCardWord (self, char) :
		###########################
		#  [12] Implement Here         #
		pass  # delete this line after complete this method
		###########################         
			 
	def setAnswer (self) :
		###########################
		# [13] Implement Here         #
		###########################          
		time.sleep(1)
		
			 
	def clear(self, success): 
		self.ask.setMessage("")           
		self.prisoner.clear(success)
		self.keyboard.clear()
		
		if success == True :
			self.scaffold.up()  
			
	def close(self):
		self.canvas.close()

 
####################################
###    hangman function 
####################################
def hangman (table) :
	
	table.card = table.words.draw( )    
	word_len = len(  table.card.word  )
	word_string = "_ " * word_len
	table.cardWord.setMessage ( word_string  )
	table.cardKind.setMessage ( "("+  table.card.kind + ")" )
	
	step = 0 

	while True:
		e = table.canvas.wait()
		d = e.getDescription()
		if d == "canvas close":
			return False
		if d != 'mouse click':
			continue
		###########################
		#  [14]Implement Here         #
		###########################
	  
		key_index = table.keyboard.findKey(x,y)    #  return key index 
		if key_index == None :                     #  not key
			continue 
		if table.keyboard.keys[key_index].clicked == True :   #already clicked
			continue        
		char = table.keyboard.keys[key_index].key.lower()      
		table.keyboard.click(key_index)                       # new key is clicked
	  
		if char  in  table.card.word :         #  right guess no step inclease
			table.changeCardWord (char)                         
		else :                      # wrong guess
			table.prisoner.hang()   # hang 
			step += 1   
		  
		if step >= 8 :              #  you lost
			table.prisoner.die()
			table.setAnswer()       #  show the answer
			time.sleep(1)
			return False
		if  not ('_'  in table.cardWord.getMessage() ):   # right answer !!!! you win
			table.scaffold.down()
			table.prisoner.run()
			return True
		  
####################################
###     main function 
####################################
def main():
	table = Table()
	while True :
		success = hangman(table)   # hangman return True when your answer is right
		table.ask.setMessage("Another round ? (y/n)   ")
	  
		while True:
			e = table.canvas.wait()
			d = e.getDescription()
			if d == "keyboard":
				key = e.getKey() 
				if key in ['y','Y'] :
					table.ask.setMessage("Another round ? (y/n) "+ key)
					time.sleep(1)
					table.clear(success)
					break
				else :      #game stop
					table.close( )
					return
		  
####################################   
main()
####################################