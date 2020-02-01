from Tkinter import *
import tkFileDialog as dialog

seq=''

def fopen():
	global seq
	f = dialog.askopenfile(parent=top, mode='rb', title='Choose a file')
	seq = f.read()
	text.insert(END, seq)

def calc():
	result=count(text.get("1.0",END))
	print result
	label['text']='A:'+str(result['A'])+', T:'+str(result['T'])+', G:'+str(result['G'])+', C:'+str(result['C'])

def count(s):
	print 
	D={'A':0,'G':0,'C':0,'T':0}
	for x in s:
		if x in D:
			D[x]+=1
	return D

top = Tk()
top.grid()
frame = Frame(top)
frame.pack()

text = Text(frame, height =20, width =20)
text.grid(row = 0, column = 0, columnspan = 2)

filebutton= Button(frame, text ="Read a file",  command = fopen, width =10)
filebutton.grid(row = 1, column = 0)

calc= Button(frame, text ="Count",  command = calc, width =10)
calc.grid(row = 1, column = 1)

label = Label(frame, text='A:0, T:0, G:0, C:0')
label.grid(row=2, columnspan=2)

mainloop()
