from enum import Enum


class MoveKeys(Enum):
    LEFT = 80
    UP = 82
    RIGHT = 79
    DOWN = 81


class Player():
    def __init__(self, x, y, layer=50):
        self.symbol = "P"
        self.color = "#6699ff"
        self.layer = layer
        self.x = x
        self.y = y

    def handleKeyPress(self, key, rootx, rooty, terminal):
        if(key == MoveKeys.LEFT.value):
            print("hit left")
            self.x -= 1
        if(key == MoveKeys.RIGHT.value):
            self.x += 1
        if(key == MoveKeys.UP.value):
            self.y -= 1
        if(key == MoveKeys.DOWN.value):
            self.y += 1
        self.display(rootx, rooty, terminal)

    def display(self, rootx, rooty, terminal):
        terminal.layer(self.layer)

        terminal.clear_area(0, 0, 500, 500)

        terminal.color(self.color)
        terminal.put(rootx + self.x, rooty + self.y, self.symbol)
        terminal.refresh()
