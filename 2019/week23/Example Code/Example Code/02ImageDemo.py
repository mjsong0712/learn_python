#-*- coding: utf-8 -*-
#이미지를 띄을 수 있는 code이다.
from Tkinter import *
class ImageDemo (Frame):
    
    def __init__ (self):
        
        Frame.__init__(self)
        self.master.title ("image Demo")
        self.grid()
        self._image1 = PhotoImage( file = "Shop.gif" )#폴더 내에서 사진을 가져온다.
        self._textLabel = Label(self, image = self._image1)#가져온 사진으로 Label을 만든다.
        self._textLabel.grid()
        self._text2Label = Label(self, text = "Shop")
        self._text2Label.grid()
        
        
def main():
    a = ImageDemo()
    a.mainloop()
    
main()

        