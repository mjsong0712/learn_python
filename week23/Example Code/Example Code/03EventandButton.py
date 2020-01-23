#-*- coding: utf-8 -*-
#사용자가 직접 조종할 수 있는 Event를 만든다.
from Tkinter import *
class ButtonDemo (Frame):
    
    def __init__ (self):
        Frame.__init__(self)
        self.master.title ("Button Demo")
        self.grid()
        self._label = Label(self, text = "Hello")
        self._label.grid()
        self._button = Button (self, text= "Click Me", command = self._switch)#클릭할 시 command를 실행하는 Button을 만든다.
        self._button.grid()
        
    def _switch(self):
        if self._label["text"] == "Hello" :
            self._label["text"] = "Goodbye"
        else:
            self._label["text"] = "Hello"
            
def main():
    a = ButtonDemo().mainloop()
    
main()