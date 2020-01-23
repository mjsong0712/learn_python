#-*- coding: utf-8 -*-
#Color와 Font를 바꾼다.
from Tkinter import *
import tkFont
class LabelDemo (Frame):
    
    def __init__(self):
        
        Frame.__init__(self)
        self.master.title ("Label Demo")
        self.grid()
        font1 = tkFont.Font (family= "Verdana", size=20, slant = "italic")#사용할 Font를 설정한다.
        self._label = Label(self, font = font1, text = "Hello world", bg="blue")#그 Font를 사용하는 label을 만든다, 색은 "blue"와 같이 tkinter에 입력된 색을 직접 쓰거나 #000000과 같은 형태로 구현할 수 있다.
        self._label.grid()
        
def main():
    LabelDemo().mainloop()
    
main()