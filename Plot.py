from typing import Any
from enum import Enum


class symbols(Enum):
    UNTILLED = 203
    TILLED = 160
    WATERED = 161


class colors(Enum):
    UNTILLED = "CC9260"
    TILLED = "A6652D"
    WATERED = "39A2CC"


class Plot():
    def __init__(self):
        self.object: Any = None
        self.tilled: bool = False
        self.watered: bool = False
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
        print("displaying at {}, {}".format(x, y))
        terminal.put(x, y, "e")
