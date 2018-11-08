from typing import Any


class Plot():
    def __init__(self):
        self.object: Any = None
        self.tilled: bool = False
        self.color: str = "#ffffff"
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
