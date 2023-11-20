import tkinter
import threading

class Window():
    def __init__(self):
        self.CreateWindow()
    
    def CreateWindow(self):
        self.root = tkinter.Tk()
        self.root.geometry("600x900")
        self.root.title("Game Window")
        self.root.mainloop()

main = Window()