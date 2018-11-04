class Plant():
    def __init__(self, name, maxGrowth):
        self.name = name
        self.maxGrowth = maxGrowth
        self.growthState = 0
        self.watered = False

    def water(self):
        self.watered = True

    def __str__(self):
        return "growth state: {}, watered: {}".format(
            self.growthState, self.watered)
