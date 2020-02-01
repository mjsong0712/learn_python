#-*- coding: utf-8 -*-
#기본적인 창을 띄우는 코드이다.
from Tkinter import *
class LabelDemo (Frame):
    
    def __init__(self):
        
        Frame.__init__(self)#Tkinter의 기능을 상속받는다.       
        self.master.title ("Label Demo!!!")#창의 제목을 설정
        self.grid()#기본이 되는 창을 구현한다.
        self._label = Label(self, text = "Hello world")#기본 창 안에 Label이라는 형태의 text를 넣을 수 있는 단위체를 만든다.
        self._label.grid()#self._label을 구현한다.
        
def main():
    LabelDemo().mainloop()
    
main()