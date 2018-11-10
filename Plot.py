from typing import Any
from enum import Enum
from random import getrandbits


class symbols(Enum):
    UNTILLED = 219
    TILLED = 176
    WATERED = 177


class colors(Enum):
    UNTILLED = "#CC9260"
    TILLED = "#A6652D"
    WATERED = "#39A2CC"


class Plot():
    def __init__(self):
        self.object: Any = None
        self.tilled: bool = bool(getrandbits(1))
        self.watered: bool = bool(getrandbits(1))
        self.upPlot: Plot = None
        self.rightPlot: Plot = None
        self.downPlot: Plot = None
        self.leftPlot: Plot = None

    def __str__(self):
        plotState = """object: {}
        tilled: {}
        color: {}
        watered: {}
        """.format(self.object, self.tilled, self.color, self.watered)
        return plotState

    def display(self, terminal, x, y):
        symbol = symbols.UNTILLED
        color = colors.UNTILLED
        if self.tilled:
            symbol = symbols.TILLED
            color = colors.TILLED
        if self.watered:
            symbol = symbols.WATERED
            color = colors.WATERED
        terminal.color(terminal.color_from_name(color.value))
        terminal.put(x, y, symbol.value)
