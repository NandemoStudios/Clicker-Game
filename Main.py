
import tkinter
import threading
import time

data = {
    "clicks": 0,
    "CPC": 1,
    "CPS": 0,
    "CPCPrice": 10,
    "CPSPrice": 25,
}

class Window():
    
    def __init__(self):
        self.CPSThread = threading.Thread(target=self.CPSLoop)
        self.buildWindowParts()
     
    def CPSLoop(self):
        while True:
            if data["CPS"] > 1:
                data["clicks"] += data["CPS"]
                time.sleep(1)
                self.DisplayUpdate()
    
    def buildWindowParts(self):
        self.root = tkinter.Tk()
        self.root.geometry = ("600x900")
        
        self.clickDisplay = tkinter.Label(self.root, text="Clicks: 0")
        self.ClickButton = tkinter.Button(self.root, text="Click Me!", command=self.Clicked)
        self.CPCDisplay = tkinter.Label(self.root, text="Clicks Per Click: 1")
        self.CPSDisplay = tkinter.Label(self.root, text="Clicks Per Second: 0")
        self.UpgradesButton = tkinter.Button(self.root, text="Open Upgrades", command=self.OpenUpgrades)
        
        self.clickDisplay.pack()
        self.ClickButton.pack()
        self.CPSThread.start()
        self.UpgradesButton.pack()
        self.CPCDisplay.pack()
        self.CPSDisplay.pack()
        self.root.mainloop()
        
    def CPCUpgraded(self):
        if data["clicks"] >= data["CPCPrice"]:
            data["CPC"] += 1
            data["clicks"] -= data["CPCPrice"]
            data["CPCPrice"] = data["CPCPrice"] * 2
            self.UpgradesUpdate()

    def CPSUpgraded(self):
        if data["clicks"] >= data["CPSPrice"]:
            data["CPS"] += 1
            data["clicks"] -= data["CPSPrice"]
            data["CPSPrice"] = data["CPSPrice"] * 2
            self.UpgradesUpdate()
    
    def Clicked(self):
        data["clicks"] += data["CPC"]
        self.DisplayUpdate()
        
    def DisplayUpdate(self):
        self.clickDisplay.config(text="Clicks: "+str(data["clicks"]))
        self.CPCDisplay.config(text="Clicks Per Click: "+str(data["CPC"]))
        self.CPSDisplay.config(text="Clicks Per Second: "+str(data["CPS"]))
    
    def UpgradesUpdate(self):
        self.CPCUpgrade.config(text="CPCUpgrade: "+str(data["CPCPrice"])+" Clicks")
        self.CPSUpgrade.config(text="CPSUpgrade: "+str(data["CPSPrice"])+" Clicks")
        self.DisplayUpdate()
     
    def OpenUpgrades(self):
        self.uproot = tkinter.Tk()
        self.uproot.geometry("600x900")
        self.CPCUpgrade = tkinter.Button(self.uproot, text="CPCUpgrade: 10 Clicks", command=self.CPCUpgraded)
        self.CPSUpgrade = tkinter.Button(self.uproot, text="CPSUpgrade: 25 Clicks", command=self.CPSUpgraded)
        self.CloseButton = tkinter.Button(self.uproot, text="Close", command=self.uproot.destroy)
        
        self.CPCUpgrade.pack()
        self.CPSUpgrade.pack()
        self.CloseButton.pack()

        self.uproot.mainloop()

game = Window()