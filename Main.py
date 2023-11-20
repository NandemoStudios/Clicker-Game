import tkinter
import threading

data = {
    "clicks": 0,
    "CPS": 0,
    "CPC": 1,
}

class Window():
    def __init__(self):
        self.CreateWindow()
    
    def CreateWindow(self):
        self.root = tkinter.Tk()
        self.root.geometry("900x600")
        self.root.title("Game Window")
        # The elements that go onto the screen
        self.clickDisplay = tkinter.Label(self.root, text="Clicks: 0")
        self.clickButton = tkinter.Button(self.root, text="Click Me!", command=self.clicked)
        # Packing all of items onto the screen
        self.clickDisplay.pack()
        self.clickButton.pack()
        self.root.mainloop()
    
    def clicked(self):
        data["clicks"] += data["CPC"]
        self.update()
    
    def update(self):
        self.clickDisplay.config(text="Clicks: "+str(data["clicks"]))

main = Window()