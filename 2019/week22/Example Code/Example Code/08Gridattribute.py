from Tkinter import *

class grid_attribute(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title("attributing grid")
        self.grid()
        
        self._label1 = Label (self, text = "I attribute")
        self._label1.grid(row=1, column =0, sticky= N+S)#label�� �����ϴ� ������ N+S�� �����Ѵ�
        
def main():
    a=grid_attribute().mainloop()
        
main()
        