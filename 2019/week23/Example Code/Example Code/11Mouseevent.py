#-*- coding: utf-8 -*-
# mouse event

from Tkinter import *

class Mouseevent(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("mouse event")
        self.grid()
        
        self._window = Label(self, text = "press the button")#기본 label을 설정
        self._window.grid(row = 1, column = 1)
    
        for i in range(1,4): # mouse event는 총 1,2,3이 있으므로 for문을 통해 돌린다.
            self.do_mouse('Button-%s'%i)
            self.do_mouse('ButtonRelease-%s'%i)
            self.do_mouse('Double-Button-%s'%i)    
        
    def do_mouse(self,eventname):
        def mouse_binding(event):
            msg = 'Mouse event %s' % eventname #이벤트를 받아서 문자열 + 이벤트 명으로 text를 교환
            self._window["text"] = msg
        self._window.bind_all('<%s>'%eventname, mouse_binding) #bind_all을 이용하여 한 label에 여러 이벤트를 bind한다.

    
def main():
    a=Mouseevent()
    a.mainloop()
        
main()