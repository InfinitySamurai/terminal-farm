from Plot import Plot
from typing import List, Any


class PlotContainer():

    def __init__(self, x, y, width, height):
        self.x: int = x
        self.y: int = y

        self.width: int = width
        self.height: int = height

        self.plots: List[List[Plot]] = self.createPlots(self.width, self.height)

    def createPlots(self, width, height):
        allPlots = []
        for i in range(height):
            rowPlots = []
            for k in range(width):
                rowPlots.append(Plot())
            allPlots.append(rowPlots)
        return allPlots

    def addObject(self, o: Any, x: int, y: int):
        if (x > self.width):
            raise Exception("PlotContainer x: {} too large for width: {}".format(x, self.width))
        if (y > self.height):
            raise Exception("PlotContainer y: {} too large for height: {}".format(y, self.height))
        plot = self.getPlot(x, y)
        plot.object = o

    def display(self, terminal):
        for i, row in enumerate(self.plots):
            for k, plot in enumerate(row):
                plot: Plot
                x = self.x + k
                y = self.y + i
                if(plot):
                    plot.display(terminal, x, y)
        terminal.refresh()

    def getPlot(self, x: int, y: int) -> Plot:
        return self.plots[y][x]

    def setPlot(self, x: int, y: int, p: Plot):
        self.plots[y][x] = p
