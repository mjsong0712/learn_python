# -*- coding: utf-8 -*-
from Tkinter import *

class grid_attribute(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title("attributing grid")
        self.master.geometry ("200x200")
        self.grid()
        self._entry = Entry(self, justify="center", width = 30)
        self._entry.grid(row=0, column = 0)
        self._label1 = Label (self, text = "I attribute", width = 10, height = 10)
        self._label1.grid(row=1, column =0, sticky=W)#label이 시작하는 방향을 N+S로 결정한다
        
def main():
    a=grid_attribute().mainloop()
        
main()
        