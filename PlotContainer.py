from Plot import Plot
from typing import List, Any, Union


class PlotContainer():

    def __init__(self, x, y, maxX, maxY):
        self.x: int = x
        self.y: int = y
        self.maxX: int = maxX
        self.maxY: int = maxY
        self.topLeftPlot: Plot = self.createPlots(maxX, maxY)

    def createPlots(self, xSize, ySize) -> Plot:
        firstPlot: Union[Plot, None] = None
        previousPlotRow: List[Plot] = []
        for i in range(xSize):
            previousPlot: Union[Plot, None] = None
            currentPlotRow: List[Plot] = []
            for j in range(ySize):
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

    def addObject(self, o: Any, x: int, y: int):
        if (x > self.maxX):
            raise Exception("PlotContainer x: {} too large for maxX: {}".format(x, self.maxX))
        if (y > self.maxY):
            raise Exception("PlotContainer y: {} too large for maxY: {}".format(y, self.maxY))
