# -*- coding: utf-8 -*-
from Tkinter import *
window = Tk()

def calc():
	a = int(first_entry.get())
	b = int(second_entry.get())
	result["text"] = str(a + b)

first_number = Label(window, text = "First number")
first_number.grid(row = 0, column = 0)

second_number = Label(window, text = "Second number")
second_number.grid(row = 1, column = 0)

first_entry = Entry(window)
first_entry.grid(row = 0, column = 1)

second_entry = Entry(window)
second_entry.grid(row = 1, column = 1)

resultBtn = Button(window, text = "result", command = calc)
resultBtn.grid(row = 2, column = 0)

result = Label(window, text = "")
result.grid(row = 2, column = 1)

window.mainloop()




