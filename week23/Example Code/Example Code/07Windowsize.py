#-*- coding: utf-8 -*-
#window의 크기를 조절한다.
from Tkinter import *
class LabelDemo (Frame):
    
    def __init__(self):
        
        Frame.__init__(self)
        self.master.title ("Label Demo")
        self.master.geometry ("200x200")#100*200 pixel
        self.master.resizable(1,1)#(horizontal,vertical)-0으로 하면 invariable하다(1로 하면 variable)
        self.grid()
        self._label = Label(self, text = "Hello world")
        self._label.grid()
        
def main():
    LabelDemo().mainloop()
    
main()