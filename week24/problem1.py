# -*- coding: utf-8 -*-

from Tkinter import *
class EntryDemo (Frame):

	def __init__ (self):
		Frame.__init__(self)
		self.master.title ("Average of Three")
		self.grid()

		self._first_label = Label(self, text = "First Integer")
		self._first_label.grid(row = 0, column = 0)
		self._firstVar = IntVar()#입력받을 변수와 형태를 정한다.
		self._firstEntry = Entry (self, textvariable = self._firstVar)#변수를 입력할 수 있는 Entry라는 창을 만든다.
		self._firstEntry.grid(row = 0, column = 1)

		self._second_label = Label(self, text = "Second Integer")
		self._second_label.grid(row = 1, column = 0)
		self._secondVar = IntVar()
		self._secondEntry = Entry (self, textvariable = self._secondVar)
		self._secondEntry.grid(row = 1, column = 1)

		self._button = Button (self, text = "result", command = self.calc)
		self._button.grid(row =4, column = 0, columnspan = 1)

		self._label = Label(self, text = "")#기본 창 안에 Label이라는 형태의 text를 넣을 수 있는 단위체를 만든다.
		self._label.grid()#self._label을 구현한다.
	def calc(self):
		n1 = self._firstVar.get()
		n2 = self._secondVar.get()
		self._label["text"] = n1 + n2

def main():
	EntryDemo().mainloop()
	
main()