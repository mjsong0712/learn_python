from Tkinter import *

class Keyboardevent(Frame):
    
    def key(self,event):
        if event.char==event.keysym:
            msg ='Normal Key %r' % event.char
        elif len(event.char)== 1:
            msg ='Punctuation Key %r (%s)' % (event.keysym, event.char)
        else:
            msg ='Special Key %r' % event.keysym
        self._window["text"] = msg
    
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title("keyboard event")
        self.grid()
        
        self._window = Label(self, text = "Press any key")
        self._window.pack(paroofx = 10, paroofy = 10 )  
        
        self._window.bind_all('<Key>', self.key)    
    
def main():
    a=Keyboardevent()
    a.mainloop()
        
main()