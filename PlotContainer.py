from Plot import Plot
from typing import List, Any, Union


class PlotContainer():

    def __init__(self, x, y, width, height):
        self.x: int = x
        self.y: int = y

        self.width: int = width
        self.height: int = height

        self.topLeftPlot: Plot = self.createPlots(self.width, self.height)

    def createPlots(self, width, height) -> Plot:
        firstPlot: Union[Plot, None] = None
        previousPlotRow: List[Plot] = []
        for i in range(height):
            previousPlot: Union[Plot, None] = None
            currentPlotRow: List[Plot] = []
            for j in range(width):
                newPlot: Plot = Plot()
                if(i == 0 and firstPlot is None):
                    firstPlot = newPlot
                if(previousPlot):
                    previousPlot.rightPlot = newPlot
                    newPlot.leftPlot = previousPlot
                if(previousPlotRow):
                    newPlot.upPlot = previousPlotRow[j]
                    previousPlotRow[j].downPlot = newPlot
                previousPlot = newPlot
                currentPlotRow.append(newPlot)
            previousPlotRow = currentPlotRow
        return firstPlot

    # def addObject(self, o: Any, x: int, y: int):
    #     if (x > self.maxX):
    #         raise Exception("PlotContainer x: {} too large for maxX: {}".format(x, self.maxX))
    #     if (y > self.maxY):
    #         raise Exception("PlotContainer y: {} too large for maxY: {}".format(y, self.maxY))

    def display(self, terminal):
        self.displayRow(terminal, self.topLeftPlot, self.x, self.y)
        terminal.refresh()

    def displayRow(self, terminal, firstPlot, x, y):
        self.displayPlot(terminal, firstPlot, x, y)
        if(firstPlot.downPlot):
            self.displayRow(terminal, firstPlot.downPlot, x, y + 1)

    def displayPlot(self, terminal, plot, x, y):
        plot.display(terminal, x, y)
        if(plot.rightPlot):
            self.displayPlot(terminal, plot.rightPlot, x + 1, y)
