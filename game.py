from Plant import Plant

p: Plant = Plant()
print(p)
p.water()
print(p)


def testFunction(plant: Plant):
    print("We got passed a plant")
    print(plant)


def wantsAString(thing: str):
    print(thing)


wantsAString(1)
testFunction("not a plant")
