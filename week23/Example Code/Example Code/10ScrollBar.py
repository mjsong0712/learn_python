#-*- coding: utf-8 -*-
#scrollbar을 사용할 수 있는 GUI다.
#어려우니 주의
from Tkinter import *
class ListBox (Frame):
    def __init__(self):
        Frame.__init__ (self)
        self.master.title("List Box")
        self.grid()
        self._listPane = Frame(self)
        self._listPane.grid (row=0, column=0, sticky = N+S)
        self._yScroll = Scrollbar( self._listPane, orient = VERTICAL)#vertical하게 움직이는 scrollbar를 만든다.
        self._yScroll.grid (row=0, column=1, sticky = N+S)
        self._theList = Listbox(self._listPane, width = 6, height = 10, selectmode = SINGLE, yscrollcommand = self._yScroll.set)#한번에 하나의 변수를 선택 가능한, set 형태의 Listbox라는 component를 만든다.
        self._theList.grid (row=0, column =0, sticky = N+S)
        self._yScroll["command"] = self._theList.yview
        self._theList.insert (END, "Apple")#끝에 Apple을 삽입
        self._theList.insert (END, "Banana")
        self._theList.activate(0)#0번째 변수에 커서가 두어지도록 한다.
        self._inputVar = StringVar()
        self.inputEntry = Entry (self, width = 10, textvariable = self._inputVar)
        self.inputEntry.grid(row=0, column=1)
        self._button1 = Button(self, text = "insert", command = self._add)
        self._button2 = Button(self, text = "remove", command = self._remove)
        self._button1.grid (row=1, column=2)
        self._button2.grid (row=1, column=3)
        
    def _add(self):#맨 뒤에 새로운 item을 삽입한다.
        item = self._inputVar.get()
        if item !="":
            self._theList.insert(END, item)
            self._theList.see(END)
    def _remove(self):
        if self._theList.size() >0:
            self._theList.delete(ACTIVE)#ACTIVE되어있는 변수를 지운다.
            
def main():
    a=ListBox()
    a.mainloop()
    
main()
    