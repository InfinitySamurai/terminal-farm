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


wantsAString("This is now actually a string")
testFunction(p)

print('hello world')
