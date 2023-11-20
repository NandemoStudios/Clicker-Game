import tkinter
import threading

class Window():
    def __init__(self):
        self.CreateWindow()
    
    def CreateWindow(self):
        self.root = tkinter.Tk()
        self.root.mainloop()

main = Window()