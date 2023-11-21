import tkinter
import threading
import time
import random
import os

class Window():
    
    def __init__(self, data):
        self.data = data
    
    def Save(self):
        savefile = open("SaveData", 'w+')
        savefile.write(str(self.data["clicks"])+'\n')
        savefile.write(str(self.data["CPC"])+'\n')
        savefile.write(str(self.data["CPS"])+'\n')
        savefile.write(str(self.data["CPCPrice"])+'\n')
        savefile.write(str(self.data["CPSPrice"]))
        savefile.close()
    
    def Load(self):
        if os.path.isfile('./SaveData') == True:
            savefile = open("SaveData", 'r+')
            self.data["clicks"] = int(savefile.readline())
            self.data["CPC"] = int(savefile.readline())
            self.data["CPS"] = int(savefile.readline())
            self.data["CPCPrice"] = int(savefile.readline())
            self.data["CPSPrice"] = int(savefile.readline())
            self.DisplayUpdate()
        else:
            self.Save()
     
    def CPSLoop(self):
        while True:
            if self.data["CPS"] > 1:
                self.data["clicks"] += self.data["CPS"]
                time.sleep(1)
                self.DisplayUpdate()
    
    def buildWindowParts(self):
        self.root = tkinter.Tk()
        self.root.geometry("900x600")
        
        self.clickDisplay = tkinter.Label(self.root, text="Clicks: 0")
        self.ClickButton = tkinter.Button(self.root, text="Click Me!", command=self.Clicked)
        self.CPCDisplay = tkinter.Label(self.root, text="Clicks Per Click: 1")
        self.CPSDisplay = tkinter.Label(self.root, text="Clicks Per Second: 0")
        self.UpgradesButton = tkinter.Button(self.root, text="Open Upgrades", command=self.OpenUpgrades)
        self.SaveButton = tkinter.Button(self.root, text="Save", command=self.Save)
        self.LoadButton = tkinter.Button(self.root, text="Load", command=self.Load)
        
        self.clickDisplay.grid(row=0, column=0, sticky='nesw')
        self.ClickButton.grid(row=1, column=0, sticky='nesw')
        self.CPCDisplay.grid(row=2, column=0, sticky='nesw')
        self.CPSDisplay.grid(row=2, column=1, sticky='nesw')
        self.UpgradesButton.grid(row=3, column=0, sticky='nesw')
        self.SaveButton.grid(row=4, column=0, sticky='nesw')
        self.LoadButton.grid(row=4, column=1, sticky='nesw')

        self.root.mainloop()
        
    def CPCUpgraded(self):
        if self.data["clicks"] >= self.data["CPCPrice"]:
            self.data["CPC"] += 1
            self.data["clicks"] -= self.data["CPCPrice"]
            self.data["CPCPrice"] = self.data["CPCPrice"] * round((random.randint(200, 300)/100))
            self.UpgradesUpdate()

    def CPSUpgraded(self):
        if self.data["clicks"] >= self.data["CPSPrice"]:
            self.data["CPS"] += 1
            self.data["clicks"] -= self.data["CPSPrice"]
            self.data["CPSPrice"] = self.data["CPSPrice"] * round((random.randint(200, 300)/100))
            self.UpgradesUpdate()
    
    def Clicked(self):
        self.data["clicks"] += self.data["CPC"]
        self.DisplayUpdate()
        
    def DisplayUpdate(self):
        self.clickDisplay.config(text="Clicks: "+str(self.data["clicks"]))
        self.CPCDisplay.config(text="Clicks Per Click: "+str(self.data["CPC"]))
        self.CPSDisplay.config(text="Clicks Per Second: "+str(self.data["CPS"]))
    
    def UpgradesUpdate(self):
        self.CPCUpgrade.config(text="CPCUpgrade: "+str(self.data["CPCPrice"])+" Clicks")
        self.CPSUpgrade.config(text="CPSUpgrade: "+str(self.data["CPSPrice"])+" Clicks")
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