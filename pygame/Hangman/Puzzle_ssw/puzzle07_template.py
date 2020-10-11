from cs1media import *
from cs1graphics import *
import time  
import random
import sys

#---------------------------------------------------------------------------
#                  Student's Information  ==> Change here
#---------------------------------------------------------------------------
#  NAME  : 
#  Student ID : 
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
#                        Global variable initialize  
#---------------------------------------------------------------------------

# Piece graphic images will be saved in the TEMP directory
PATH = "./Temp/"    

# Starting x,y position of source and destination boards
SOURCE_START_X = 100  
SOURCE_START_Y = 140
DEST_START_X = 740
DEST_START_Y = 140
IMAGE_W = 360    # original image width  
IMAGE_H = 360    # original image height  

# Set default value. They will be cannged after user inputs the NUMBER
NUMBER = 2       # default divide number 2X2 
PIECE_W = IMAGE_W  / NUMBER      # one piece image width size
PIECE_H = IMAGE_H  / NUMBER      # one piece image height size


###########################################################################
#                               class Piece
###########################################################################

class Piece(object):                                 

	def __init__(self, row ,column):
		self.row = row                 # row and column of piece is the piece's location of
		self.column = column           # original image  
		self.image_name = "img" + str(row)  + str(column) +".jpg"
		
		# loc_row and loc_column are piece's row and column value on source board 
		# this piece's location value will be reset after shuffle  
		self.loc_row = 0
		self.loc_column = 0

	def __str__(self):
		return self.image_name
	   

###########################################################################
#                               class Deck
###########################################################################
class Deck(object):
 
	def __init__(self):  
		self.pieces = [ ]   
		#-----------------------------------------
		# Make NUMBER * NUMBER Piece objects 
		# and append to the self.pieces list
		# Shuffle self.pieces
		#-----------------------------------------
		
		for i in range(NUMBER):
			for j in range(NUMBER):	
				self.pieces.append(Piece(i,j))

		random.shuffle(self.pieces)


	def draw(self):
		return self.pieces.pop(0)
 

###########################################################################
#                           class  PieceGraphics
###########################################################################

class PieceGraphics(object):
  
	def __init__(self, piece ):
		self.layer = Layer()      #layer for a piece image
		self.layer.setDepth(45)
		self.image = Image(PATH + piece.image_name)     
		self.layer.add(self.image)
		

		# calculate self.x and self.y the coordination of piece image on the canvas
		i =  piece.loc_row
		j =  piece.loc_column
		self.x = SOURCE_START_X  +  PIECE_W /2  +   PIECE_W * j 
		self.y = SOURCE_START_Y  +  PIECE_H /2  +   PIECE_H * i

		self.layer.move (self.x , self.y)
		return 
 
###########################################################################
#                           class  Board
###########################################################################

class Board(object):

	def __init__(self, canvas , x, y):

		self.canvas = canvas
		self.x = x                          # start x position of board
		self.y = y                          # start y position of board
		self.w =  PIECE_W * NUMBER          # board's width
		self.h =  PIECE_H * NUMBER  	    # board's height
		
		#---------------------------------------------------
		# Initialize three NUMBER by NUMBER 2-d lists 
		# At first, all list is set as None :
		#     self.pieces , self.graphics , self.frames 
		#---------------------------------------------------
		self.pieces   = [ [None] * NUMBER for k in range (NUMBER)]    # list of piece objects
		self.graphics = [ [None] * NUMBER for k in range (NUMBER)]    # list of graphic objects related pieces
		self.frames   = [ [None] * NUMBER for k in range (NUMBER)]    # list of frame objects for receive user's click event
		
		self.selected_frame = (None,None)   # keep current selected frame's row and column
		self.number_of_pieces = 0           # number of piece objects located on this board
		
		self.rectangle = Rectangle (self.w, self.h)
		self.rectangle.setBorderWidth = 2 
		self.rectangle.setFillColor ('lemonchiffon')
		self.rectangle.setDepth (100)
		self.rectangle.moveTo ( ( self.x + self.w /2 )  , ( self.y + self.h/2 ) )
		self.canvas.add (self.rectangle )
	
	def clear(self):
		#--------------------------------------------------------------
		# Remove all graphics images and frame images on the canvas 
		#---------------------------------------------------------------
		for i in NUMBER:
			for j in NUMBER:	
				if self.graphics[i][j]!=None:
					self.canvas.remove(self.graphics[i][j].layer)

		# Reset three lists : self.pieces , self.graphics , self.frames
		self.graphics = [ [None] * NUMBER for k in range (NUMBER)]
		self.pieces   = [ [None] * NUMBER for k in range (NUMBER)]
		self.frames   = [ [None] * NUMBER for k in range (NUMBER)]
		
		self.selected_frame = (None,None)
		self.number_of_pieces = 0
	
	def add_piece(self, piece):  	
		#------------------------------------------------------
		# This method is called only one time at puzzleGame()
		# Using a piece object, add a new piece object to the source_board  
		# Make a related graphic object   
		# Using self.number_of_pieces, set piece object's attributes
		#    piece.loc_row and piece.loc_column (location on the board)
		# Set pieces list and graphics list for saving objects
		# Change number_of_pieces 
		# Show the graphic image on the canvas
		#------------------------------------------------------
		pi=self.number_of_pieces/NUMBER
		pj=self.number_of_pieces%NUMBER

		piece.loc_row=pi
		piece.loc_column=pj
		self.pieces[pi][pj]=piece
		self.number_of_pieces+=1
		self.graphics[pi][pj]=PieceGraphics(piece)
		self.canvas.add(self.graphics[pi][pj].layer)
	
	def add_frames (self):	
		#---------------------------------------------------
		# Generate Number * Number frame objects 
		# Set frames list and add the layer on the canvas
		#---------------------------------------------------
		for i in range(NUMBER):
			for j in range(NUMBER):
				aframe = Frame(self.canvas,self.x, self.y, i,j)
				self.frames[i][j]= aframe
				self.canvas.add(aframe.layer)
  
  
	def click_position(self , x, y) :
		#-------------------------------------------------------------------
		# This method is called when clicked (x,y) coordination is on the board
		# Calculate which frame is clicked on this board.
		# Change current selected frame using unselect() and select() method
		#--------------------------------------------------------------------
		pj=(x-self.x)/PIECE_W
		pi=(y-self.y)/PIECE_H

		selected_i, selected_j = self.selected_frame
		if selected_i!=None:
			self.frames[selected_i][selected_j].unselect()
		
		self.frames[pi][pj].select()
		self.selected_frame=(pi,pj)
		print pi,pj,'selected frame'

###########################################################################
#                           class   Frame
########################################################################### 

class Frame(object):
	def __init__ (self, canvas , start_x,  start_y, row, column ):
		self.canvas = canvas
		self.row = row
		self.column = column
	 
		self.layer = Layer() 
		self.rectangle = Rectangle(PIECE_W, PIECE_H)
		self.rectangle.setBorderWidth = 1
		self.rectangle.setBorderColor ('red')
		self.layer.add (self.rectangle ) 
		self.layer.setDepth (40)
		#----------------------------------------------------------
			# start_x, start_y is the starting position of the board
		# Calculate the coordination of frame using row and column
		# Move the frame's layer for showing the rectangle.
		#----------------------------------------------------------
		self.x = start_x  +  PIECE_W * self.column
		self.y = start_y  +  PIECE_H * self.row
		self.layer.move (self.x + PIECE_W /2 , self.y + PIECE_H /2 )	

	def __str__(self):
		return str(self.row)+str(self.column)
	
	def select (self) :
		#------------------------------------------------------------------
		# When a frame is selected, change the depth and color "blue"
		#------------------------------------------------------------------
		print self.row,self.column,'*'
		self.rectangle.setBorderColor('blue')
		self.layer.setDepth(1)
 
	
	def unselect(self) :
		#------------------------------------------------------------------
		# When a frame is unselected, change the depth and color "red"  
		#------------------------------------------------------------------
		self.rectangle.setBorderColor('red')
		self.layer.setDepth(40)
 

###########################################################################
#                           class   Button
########################################################################### 

class Button (object):
 
	def __init__(self,  canvas, x,y, image , direction ):
		"""Create a button displayed at indicated position on canvas."""
		self.canvas = canvas
		self.x = x   # start position
		self.y = y
		self.w = 50  # button image size
		self.h = 50
		self.d = direction  #  "backware" / "forward"
		
		self.image = image
		self.layer = Layer()               #layer for a button image
		self.layer.add(self.image)
		self.layer.moveTo(self.x + self.w/2 , self.y + self.h/2) 	
		self.canvas.add(self.layer)   	



		#---------------------------------------------------------------------------
		#  click_button ()
		#---------------------------------------------------------------------------
		# Check the states of two boards' selected frames.
		# When forward button is clicked, source_board's frame must have a piece and
		#    dest_board's frame  must be empty.
		# When backward button is clicked, source_board's frame must be empty and
		#    dest_board's frame  must have a piece. 
		# If proper frames are selected,
		#      call table.move_piece() and set score. (whenever image is moved, add 1) 
		#      clear the message 
		# Otherwise, show proper message
		#     if frame of two boards is not selected, 
		#             "Select Source and Destination frame. "
		#     if selected frame's state is wrong,
		#             "Start frame must have a piece and End frame must be empty."
		#---------------------------------------------------------------------------
	
	def click_button(self, table):

		if self.d=="forward":
			fromT=table.source_board
			toT=table.dest_board
		else:
			fromT=table.dest_board
			toT=table.source_board

		if fromT.selected_frame==(None,None) or toT.selected_frame==(None,None):
			print 'show 1'
			table.show_message("Select Source and Destination frame.")
			return

		fi, fj=fromT.selected_frame
		ti, tj=toT.selected_frame

		if fromT.pieces[fi][fj]==None or toT.pieces[ti][tj]!=None:
			table.show_message("Start frame must have a piece and End frame must be empty.")
			return

		table.move_piece(fromT,toT)
		table.show_message("")


###########################################################################
#                           class   Table
########################################################################### 

class Table(object):
   
	def __init__(self):
		
		self.canvas =  Canvas( 1200 ,630 ,'ivory','Puzzle Game')
		self.source_board  =  Board (self.canvas, SOURCE_START_X, SOURCE_START_Y )	
		self.dest_board    =  Board (self.canvas, DEST_START_X , DEST_START_Y ) 
		
		title_img = Image(".\Images\puzzle.png")	
		title_img.moveTo (600 , 70  )	
		self.canvas.add (title_img )     	
		  
		self.message = Text("Play Game !!!") 
		self.message.setFontColor('black')
		self.message.setFontSize(20)    
		self.message.moveTo( 600, 550)
		self.canvas.add(self.message)
		
		self.question = Text(" ")
		self.question.setFontColor('black')
		self.question.setFontSize(20)
		self.question.moveTo( 600, 600)
		self.canvas.add(self.question)
		
		self.scoreText = Text("Try : ") 
		self.scoreText.setFontColor('black')
		self.scoreText.setFontSize(20)    
		self.scoreText.moveTo( 580, 300)
		self.canvas.add(self.scoreText)
		
		self.score = Text("0") 
		self.score.setFontColor('black')
		self.score.setFontSize(20)    
		self.score.moveTo( 645, 300)
		self.canvas.add(self.score)	
		
		self.rectangle = Rectangle ( 130, 130 )
		self.rectangle.setBorderWidth = 2
		self.rectangle.setFillColor ('coral')
		self.rectangle.setDepth (200)
		self.rectangle.moveTo (600 , 210  )
		self.canvas.add (self.rectangle )    
			
		self.small_image = Image(".\Images\small_image.jpg") 
		self.layer = Layer()               #layer for a small image
		self.layer.add(self.small_image)
		self.layer.moveTo (600 , 210   )	
		self.canvas.add (self.layer )   	

		
		backward_img = Image(".\Images\\backward.jpg") 
		self.backward = Button (self.canvas, 525, 375, backward_img, "backward")
	 
		forward_img = Image(".\Images\\forward.jpg") 
		self.forward = Button (self.canvas, 625, 375, forward_img , "forward")
		
	 
		#------------------------------------------------------------
		# Receive a user's click event  until the user select
		# source board or destination board or two buttons 
		#------------------------------------------------------------
	def click(self) :
		while True:
			e = self.canvas.wait( )
			d = e.getDescription( )
			
			if d != 'mouse click':   
				continue
			
			p = self.canvas.getMouseCoordinates( )   
			pos_x = p.getX()
			pos_y= p.getY()
			
			if self.check_position(pos_x, pos_y):
				break
			
		#-----------------------------------------------------------------------------
		# Receive clicked coordination (x,y) and check which object is clicked
		# if (x,y) coordination is on the board object , call related board.click_position()
		# or it is on the button object, call related button.click_button()
		# This method return True when (x,y) is proper position (select objects)
		# otherwise (click position is not on the boards or buttons) return False
		#-----------------------------------------------------------------------------
	
	def check_position(self , x, y) :
		proper_position = False
		
		if (self.source_board.x < x < self.source_board.x + self.source_board.w ) and (self.source_board.y < y < self.source_board.y + self.source_board.h ) :
			proper_position = True
			self.source_board.click_position(x,y)
			
		elif (self.dest_board.x < x < self.dest_board.x + self.dest_board.w ) and (self.dest_board.y < y < self.dest_board.y + self.dest_board.h ) :
			proper_position = True
			self.dest_board.click_position(x,y)

		elif (self.backward.x < x < self.backward.x + self.backward.w ) and (self.backward.y < y < self.backward.y + self.backward.h ) :
			proper_position = True
			self.backward.click_button(self)
			
		elif (self.forward.x < x < self.forward.x + self.forward.w ) and (self.forward.y < y < self.forward.y + self.forward.h ) :
			proper_position = True
			self.forward.click_button(self)
			
		return proper_position 
   
   
	#-----------------------------------------------------------------------------
	# Move a piece object which is located on the selected frame of from_board
	#     to the selected frame of to_board.
	# Using board's selected_frame attribute, find target piece  
	# You need to change two boards' attributes :pieces, number_of_pieces, graphics
	# And move the related piece graphic's layer for showing
	#-----------------------------------------------------------------------------
	
	def move_piece(self, from_board , to_board):

		print 'move'
		
		fi=from_board.selected_frame[0]
		fj=from_board.selected_frame[1]
		ti=to_board.selected_frame[0]
		tj=to_board.selected_frame[1]
		fx,fy=from_board.frames[fi][fj].x,from_board.frames[fi][fj].y
		tx,ty=to_board.frames[ti][tj].x,to_board.frames[ti][tj].y

		from_board.selected_frame, to_board.selected_frame = to_board.selected_frame, from_board.selected_frame

		from_board.frames[fi][fj], to_board.frames[ti][tj] = to_board.frames[ti][tj], from_board.frames[fi][fj]

		from_board.graphics[fi][fj], to_board.graphics[ti][tj] = to_board.graphics[ti][tj], from_board.graphics[fi][fj]

		to_board.graphics[ti][tj].layer.move(tx-fx,ty-fy)

		from_board.pieces[fi][fj], to_board.pieces[ti][tj] = to_board.pieces[ti][tj], from_board.pieces[fi][fj]
	
   
	def clear(self):
		"""Clear everything on the table."""

		self.source_board.clear()	
		self.dest_board.clear()
		self.message.setMessage("")
		self.question.setMessage("")
		self.score.setMessage("0")
	  
		  
	def show_message(self, text):
		self.message.setMessage(text)
	  
	def ask(self, prompt):
		self.question.setMessage(prompt)
		while True:
			e = self.canvas.wait()
			d = e.getDescription()
			if d == "canvas close":
				sys.exit(1)
			if d == "keyboard":
				key = e.getKey() 
				if key == 'y':
					self.question.setMessage(prompt+" "+key)
					return True
				if key == 'n':
					self.question.setMessage(prompt+" "+key)
					self.question.setMessage("")
					return False
	
	def close(self):
		self.canvas.close()
	  
	  
#---------------------------------------------------------------------------
#                            puzzleGame ()
#---------------------------------------------------------------------------
# Initialize a new deck 
# Add source and destination board's frames
# Add all pieces of deck on the source board
# Show the message "Play Game !!!" and start game
# Receive the user's click event until 
#   all the pieces are moved to destination board &
#   all positions are correct (destination board's whole image is same as original image )
#---------------------------------------------------------------------------

def puzzleGame(table):
	deck = Deck()
	table.source_board.add_frames()	
	table.dest_board.add_frames()  
	
	for  i  in range (len(deck.pieces)):
		table.source_board.add_piece(deck.draw()) 
	
	table.show_message("Play Game !!!")     
	time.sleep(1)  	
	
	while True:
		table.click()
		
		if table.dest_board.number_of_pieces == NUMBER * NUMBER : 
			finish = True
			for i in range(NUMBER):
				for j in range(NUMBER) :
					if not (table.dest_board.pieces[i][j].row == i and table.dest_board.pieces[i][j].column == j):
						finish = False
					if finish:
						break
	return

#---------------------------------------------------------------------------
#                            makePieceFiles ()
#---------------------------------------------------------------------------
# Using input parameter img object, this function generates num * num 
# pieces of graphic images and save that as jpg file format in the PATH directory.
# For example, if num == 2, after this function is executed,
# img00.jpg, img01.jpg, img10.jpg, img11.jpg will be created under ./TEMP/
#---------------------------------------------------------------------------  

def makePieceFiles(img, num): 
	global PIECE_W
	global PIECE_H
	w,h=PIECE_W/num,PIECE_H/num
	for i in range(num):
		for j in range(num):
			result = create_picture(PIECE_W, PIECE_H)
			for x in range(PIECE_W):
				for y in range(PIECE_H):
					result.set(x,y,img.get(PIECE_W*i+x,PIECE_H*j+y))
			result.save_as("./Temp/img"+str(i)+str(j)+".jpg")
 
		
#---------------------------------------------------------------------------
#                                  main() 
#---------------------------------------------------------------------------

def main() :
	global NUMBER 
	global PIECE_W
	global PIECE_H
   
	while True:
		NUMBER = raw_input("Input divide number: (2~6) ")  #2,3,4,5,6
		if (NUMBER == "") :
			NUMBER  = 2  # default 2*2 pieces
			break
		else :
			NUMBER = int(NUMBER.strip())    
			if   (2<= NUMBER <= 6 ) :
				break    

	img = load_picture(".\Images\image360.jpg")
	PIECE_W = IMAGE_W/NUMBER
	PIECE_H = IMAGE_H/NUMBER
 
	makePieceFiles(img, NUMBER)   # generate the piece image files
	
	table = Table() 
	
	while True:
		puzzleGame(table)
		if not table.ask("Another round?(y/n)"):
			break    
		time.sleep(1)
	table.clear()
	table.close()

###########################################################################
main()
