from typing import Any
from enum import Enum


class symbols(Enum):
    TILLED = 160
    WATERED = 161


class colors(Enum):
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
