from Plant import Plant
from bearlibterminal import terminal

p: Plant = Plant("Apple Tree", 10)
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

terminal.open()
terminal.print(1, 1, "[font=gothic]Hello World[/font]")
terminal.refresh()

terminal.print(6, 6, "Test")
terminal.refresh()
terminal.composition(terminal.TK_ON)
terminal.print(6, 6, "tseT")
terminal.print(10, 10, "this is a long sentence")
terminal.print(10, 10, "another thing with overlap")
terminal.put(12, 12, 1)
terminal.put(12, 13, 15)
terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
