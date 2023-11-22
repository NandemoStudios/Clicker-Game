import tkinter
import threading
import time
import random
import os

class Window():
    # Runs when class called, just defines the data argument and thats it
    def __init__(self, data):
        self.data = data
    # Writes each part of the data to a new line
    def Save(self):
        savefile = open("SaveData", 'w+')
        savefile.write(str(self.data["clicks"])+'\n')
        savefile.write(str(self.data["CPC"])+'\n')
        savefile.write(str(self.data["CPS"])+'\n')
        savefile.write(str(self.data["CPCPrice"])+'\n')
        savefile.write(str(self.data["CPSPrice"]))
        savefile.close()
    # Checks if the file 'SaveData' exists
    # If it does, reads each line, assigning variables to the saved data
    # If not, it saves the current data, to create the file
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
     # Checks if the CPS value is not 0
     # Then increases clicks by CPS, then waits a second
    def CPSLoop(self):
        while True:
            if self.data["CPS"] >= 1:
                print("More than one")
                self.data["clicks"] += self.data["CPS"]
                time.sleep(1)
                self.DisplayUpdate()
    
    def buildWindowParts(self):
        self.root = tkinter.Tk()
        self.root.geometry("900x600")
        # Define all of the elements that go onto the screen
        self.clickDisplay = tkinter.Label(self.root, text="Clicks: 0")
        self.ClickButton = tkinter.Button(self.root, text="Click Me!", command=self.Clicked)
        self.CPCDisplay = tkinter.Label(self.root, text="Clicks Per Click: 1")
        self.CPSDisplay = tkinter.Label(self.root, text="Clicks Per Second: 0")
        self.UpgradesButton = tkinter.Button(self.root, text="Open Upgrades", command=self.CallUpgradeThread)
        self.SaveButton = tkinter.Button(self.root, text="Save", command=self.Save)
        self.LoadButton = tkinter.Button(self.root, text="Load", command=self.Load)
        # Add the toolbar
        self.toolbar = tkinter.Menu(self.root)
        self.game_menu = tkinter.Menu(self.toolbar, tearoff=False)
        self.game_menu.add_command(label="Save", command=self.Save, accelerator="Ctrl+S")
        self.game_menu.add_command(label="Load", command=self.Load, accelerator="Crtl+L")
        self.game_menu.add_separator()
        self.game_menu.add_command(label="Exit", command=self.root.destroy)
        self.toolbar.add_cascade(label="Game", menu=self.game_menu)
        self.root.config(menu=self.toolbar)
        # Add all of the elements onto the screen in their respective places
        self.clickDisplay.grid(row=0, column=0, sticky='nesw', columnspan=2)
        self.ClickButton.grid(row=1, column=0, sticky='nesw', columnspan=2)
        self.CPCDisplay.grid(row=2, column=0, sticky='nesw')
        self.CPSDisplay.grid(row=2, column=1, sticky='nesw')
        self.UpgradesButton.grid(row=3, column=0, sticky='nesw', columnspan=2)
        self.SaveButton.grid(row=4, column=0, sticky='nesw')
        self.LoadButton.grid(row=4, column=1, sticky='nesw')
        # Start the window
        self.root.mainloop()
        
    def CPCUpgraded(self):
        # Check if the player has enough money, if so, give them the upgrade and take the price away
        if self.data["clicks"] >= self.data["CPCPrice"]:
            self.data["CPC"] += 1
            self.data["clicks"] -= self.data["CPCPrice"]
            # Change the price randomly between 2 and 3 times, then rounds it to a whole number
            self.data["CPCPrice"] = self.data["CPCPrice"] * round((random.randint(200, 300)/100))
            self.UpgradesUpdate()
        # Refer to comments above, its the same process
    def CPSUpgraded(self):
        if self.data["clicks"] >= self.data["CPSPrice"]:
            self.data["CPS"] += 1
            self.data["clicks"] -= self.data["CPSPrice"]
            self.data["CPSPrice"] = self.data["CPSPrice"] * round((random.randint(200, 300)/100))
            self.UpgradesUpdate()
    # Just increases the clicks by the CPC value each time the button is clicked, then puts the new count on screen
    def Clicked(self):
        self.data["clicks"] += self.data["CPC"]
        self.DisplayUpdate()

    # This is what changes the values on screen to their new values
    def DisplayUpdate(self):
        self.clickDisplay.config(text="Clicks: "+str(self.data["clicks"]))
        self.CPCDisplay.config(text="Clicks Per Click: "+str(self.data["CPC"]))
        self.CPSDisplay.config(text="Clicks Per Second: "+str(self.data["CPS"]))
    # Updates the prices on the upgrades screen
    def UpgradesUpdate(self):
        self.CPCUpgrade.config(text="CPCUpgrade: "+str(self.data["CPCPrice"])+" Clicks")
        self.CPSUpgrade.config(text="CPSUpgrade: "+str(self.data["CPSPrice"])+" Clicks")
        self.DisplayUpdate()
    # Starts the upgrades menu on a new thread so the root window doesn't freeze
    def CallUpgradeThread(self):
        self.updateThread = threading.Thread(target=self.OpenUpgrades, daemon=True)
        self.updateThread.start()
     # Creates the Upgrades window
    def OpenUpgrades(self):
        # Defines uproot as a window, sets the size and adds the elements
        self.uproot = tkinter.Tk()
        self.uproot.geometry("600x900")
        self.CPCUpgrade = tkinter.Button(self.uproot, text="CPCUpgrade: 10 Clicks", command=self.CPCUpgraded)
        self.CPSUpgrade = tkinter.Button(self.uproot, text="CPSUpgrade: 25 Clicks", command=self.CPSUpgraded)
        self.CloseButton = tkinter.Button(self.uproot, text="Close", command=self.uproot.destroy)
        # telling the window to display them in what order
        self.CPCUpgrade.pack()
        self.CPSUpgrade.pack()
        self.CloseButton.pack()
        # Starts the window, then updates the values on screen
        # Because the window can be opened and closed and values will go back to default
        # If they are not refreshed when the window is made
        self.uproot.mainloop()
        self.UpgradesUpdate()