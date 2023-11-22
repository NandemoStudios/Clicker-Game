import Window
import threading
# Creates a library containing the default variable values for the game
data = {
    "clicks": 0,
    "CPC": 1,
    "CPS": 0,
    "CPCPrice": 10,
    "CPSPrice": 25,
}
# Calls the window.py window class and gives it the library above
# Then it starts the CPS loop
# Then it tells the window to display using the buildWindowParts function from Window.py
game = Window.Window(data)
CPSThread = threading.Thread(target=game.CPSLoop)
CPSThread.start()
game.buildWindowParts()