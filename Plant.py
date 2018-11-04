from PlantStatus import PlantStatus


class Plant():
    def __init__(self, name, maxGrowth):
        self.name = name
        self.maxGrowth = maxGrowth
        self.growthAmount = 0
        self.watered = False
        self.status = PlantStatus.ALIVE

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
                if(self.growthAmount < self.maxGrowth):
                    self.growthAmount += 1
                    if (self.status == PlantStatus.SUPER):
                        self.growthAmount += 1
            else:
                self.status = PlantStatus.DYING
        elif (self.status == PlantStatus.DYING):
            if (self.watered):
                self.status = PlantStatus.ALIVE
            else:
                self.status = PlantStatus.DEAD

    def __str__(self):
        plantState = """
        name: {}
        growth: {}
        maxGrowth: {}
        watered: {}
        status: {}
        """.format(self.name, self.growthAmount, self.maxGrowth, self.watered, self.status)
        return plantState
