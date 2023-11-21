import Window
import threading

data = {
    "clicks": 0,
    "CPC": 1,
    "CPS": 0,
    "CPCPrice": 10,
    "CPSPrice": 25,
}

game = Window.Window(data)
CPSThread = threading.Thread(target=game.CPSLoop)
CPSThread.start()
game.buildWindowParts()