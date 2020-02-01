# -*- coding: utf-8 -*-
#�������� component�� ���� GUI�� ���� ���ϰ� ����� ����̴�.
from Tkinter import *
class ComplexLayout (Frame):
    def __init__ (self):
        Frame.__init__ (self)
        self.master.title("complex layout")
        self.grid()
        
        self._dataPane = Frame(self)#�������� component�� �� Frame�� ���� ��ġ�Ѵ�.
        self._dataPane.grid(row = 0, column= 0)
        
        self._label1 = Label (self._dataPane, text = "Label 1")#self�� �� �ڸ��� self._dataPane�� �־� dataPane�ȿ� component�� �ִ´�.
        self._label1.grid (row = 0, column = 0)
        self._entry1= Entry(self._dataPane)
        self._entry1.grid(row = 0, column = 1)
        self._label2 = Label (self._dataPane, text = "Label 2")
        self._label2.grid (row = 1, column = 0)
        self._entry2= Entry(self._dataPane)
        self._entry2.grid(row = 1, column = 1)
        
        self._buttonPane = Frame(self)
        self._buttonPane.grid(row = 1, column = 0)
        
        self._button1 = Button(self._buttonPane, text = "B1")
        self._button2 = Button(self._buttonPane, text = "B2")
        self._button3 = Button(self._buttonPane, text = "B3")
        self._button4 = Button(self._buttonPane, text = "B4")
        
        self._button1.grid (row = 0, column = 0)
        self._button2.grid (row = 0, column = 1)
        self._button3.grid (row = 0, column = 2)
        self._button4.grid (row = 0, column = 3)
        
def main():
    a=ComplexLayout()
    a.mainloop()
    
main()