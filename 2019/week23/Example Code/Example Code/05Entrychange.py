#-*- coding: utf-8 -*-
#Entry의 크기나 특징을 바꾸는 code이다.
from Tkinter import *
from tkMessageBox import *
class EntryDemo (Frame):
    
    def __init__ (self):
        Frame.__init__(self)
        self.master.title ("Average of Three")
        self.grid()
        
        self._first_label = Label(self, text = "First Integer")
        self._first_label.grid(row = 0, column = 0)
        self._firstVar = IntVar()
        self._firstEntry = Entry (self, justify="center", width = 7, textvariable = self._firstVar)#justify로 가운데 정렬을, width를 7글자로 맞추었다.
        self._firstEntry.grid(row = 0, column = 1)
        
        self._second_label = Label(self, text = "Second Integer")
        self._second_label.grid(row = 1, column = 0)
        self._secondVar = IntVar()
        self._secondEntry = Entry (self, justify="center", width = 7, textvariable = self._secondVar)
        self._secondEntry.grid(row = 1, column = 1)
        
        self._third_label = Label(self, text = "Third Integer")
        self._third_label.grid(row = 2, column = 0)
        self._thirdVar = IntVar()
        self._thirdEntry = Entry (self, justify="center", width = 7, textvariable = self._thirdVar)
        self._thirdEntry.grid(row = 2, column = 1)

        self._sum_label = Label(self, text = "Sum of Three")
        self._sum_label.grid(row = 3, column = 0)
        self._sumVar = IntVar()
        self._sumEntry = Entry (self, justify="center", width = 7, textvariable = self._sumVar)
        self._sumEntry.grid(row = 3, column = 1)
        
        self._button = Button (self, text = "Compute", command = self._sum, bg = "#%02x%02x%02x" % (191,229,217))
        self._button.grid(row =4, column = 0, columnspan = 1)
        
    def _sum(self):
        try:
            a = self._firstVar.get()
            b = self._secondVar.get()
            c = self._thirdVar.get()
            answer = a + b + c
            self._sumVar.set(answer)
        except ValueError:
            showerror (message = "Error : Bad format", parent = self)

def main():
    a = EntryDemo().mainloop()
    
main()
        