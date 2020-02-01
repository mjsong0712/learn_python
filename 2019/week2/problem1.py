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

def fsave():
	global seq
	ftypes = [('text file','*.txt'), ('excel file','*.csv'), ('All files', '*.*')]
	filename = dialog.asksaveasfilename(parent=top, filetypes=ftypes, title='Save a file', initialfile = 'textfile1.txt')
	file = open(filename,'w')
	file.write(text.get("1.0",END))
	file.close()

top = Tk()
top.grid()
frame = Frame(top)
frame.pack()

text = Text(frame, height =20, width =20)
text.grid(row = 0, column = 0, columnspan = 2)

filebutton= Button(frame, text ="Read a file",  command = fopen, width =10)
filebutton.grid(row = 2, column = 0)

savebutton= Button(frame, text ="Save a file",  command = fsave, width =10)
savebutton.grid(row = 1, columnspan = 2)

calc= Button(frame, text ="Count",  command = calc, width =10)
calc.grid(row = 2, column = 1)

label = Label(frame, text='A:0, T:0, G:0, C:0')
label.grid(row=3, columnspan=2)

mainloop()
