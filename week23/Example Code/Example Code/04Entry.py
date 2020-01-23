#-*- coding: utf-8 -*-
#사용자가 직접 변수를 입력할 수 있는 Entry를 만든다.
#덤으로 Error가 생길 시 나오는 Error box를 만드는 법을 만들었다.
from Tkinter import *
from tkMessageBox import * #Error box와 관련된 함수들이 들어있다.
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
        
        self._third_label = Label(self, text = "Third Integer")
        self._third_label.grid(row = 2, column = 0)
        self._thirdVar = IntVar()
        self._thirdEntry = Entry (self, textvariable = self._thirdVar)
        self._thirdEntry.grid(row = 2, column = 1)

        self._sum_label = Label(self, text = "Sum of Three")
        self._sum_label.grid(row = 3, column = 0)
        self._sumVar = IntVar()
        self._sumEntry = Entry (self, textvariable = self._sumVar)
        self._sumEntry.grid(row = 3, column = 1)
        
        self._button = Button (self, text = "Compute", command = self._sum)
        self._button.grid(row =4, column = 0, columnspan = 1)
        
    def _sum(self):
        self._first_label["text"] = str(self._firstVar.get())
        try:#a+b+c가 제대로 되는지 확인한다.
            a = self._firstVar.get()
            b = self._secondVar.get()
            c = self._thirdVar.get()
            answer = a + b + c
            self._sumVar.set(answer)
        except ValueError:#Error가 생길 경우 아래와 같은 errorbox를 띄운다.
            self._sumEntry.delete(0,1)
            self._sumEntry.insert(0,"error")

def main():
    a = EntryDemo().mainloop()
    
main()
        