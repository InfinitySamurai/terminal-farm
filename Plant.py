from enum import Enum


class PlantStatus(Enum):
    ALIVE = 1
    DYING = 2
    DEAD = 3
    SUPER = 4


plantColor = {
    PlantStatus.ALIVE: "#66ff66",
    PlantStatus.DEAD: "#333300",
    PlantStatus.DYING: "#996633",
    PlantStatus.SUPER: "#ff00ff"
}


class Plant():
    def __init__(self, name, maxGrowth, symbol):
        self.name = name
        self.maxGrowth = maxGrowth
        self.growthAmount = 0
        self.watered = False
        self.status = PlantStatus.ALIVE
        self.symbol = symbol

    def water(self):
        if(self.watered):
            print('This plant is already watered')
        else:
            self.watered = True

    def update(self):
        print("updating plant")
        print(self.status)
        print(PlantStatus.ALIVE)
        if (self.status == PlantStatus.ALIVE):
            if (self.watered):
                self.watered = False
                self.growthAmount += 1
                if (self.status == PlantStatus.SUPER):
                    self.growthAmount += 1
                if(self.growthAmount > self.maxGrowth):
                    self.growthAmount = self.maxGrowth
            else:
                self.status = PlantStatus.DYING
        elif (self.status == PlantStatus.DYING):
            if (self.watered):
                self.status = PlantStatus.ALIVE
            else:
                self.status = PlantStatus.DEAD

    def display(self, terminal, x: int, y: int):
        terminal.color(plantColor[self.status])
        terminal.put(x, y, self.symbol)
        terminal.refresh()

    def __str__(self):
        plantState = """name: {}
        growth: {}
        maxGrowth: {}
        watered: {}
        status: {}
        symbol: {}
        """.format(self.name, self.growthAmount, self.maxGrowth,
                   self.watered, self.status, self.symbol)
        return plantState
