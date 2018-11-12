from Plant import Plant
from Menu import Menu
from PlotContainer import PlotContainer
from bearlibterminal import terminal
from typing import List, Any

gameObjects: List[Any] = []


def updateAllGameObjects():
    for object in gameObjects:
        object.update()


terminal.open()
# menu: Menu = Menu(terminal, 30)
# menu.addOption("Water Plant", p.water)
# menu.addOption("Advance Time", updateAllGameObjects)
# menu.displayOptions(10, 10)


# p.display(terminal, 30, 30)
# p.update()
# p.display(terminal, 31, 30)

pc = PlotContainer(5, 5, 50, 30)
p = Plant("Apple", 10, '@')
pc.addObject(p, 3, 4)
pc.addObject(Plant("Cherry", 10, 'P'), 7, 2)
pc.display(terminal)

while terminal.peek() != terminal.TK_CLOSE:
    userInput = terminal.read()
    if(userInput == 30):
        # menu.selectOption(0)
        print("nothing")
    elif(userInput == 31):
        # menu.selectOption(1)
        print("nothing2")
    elif(userInput == 224 or userInput == 41):
        terminal.close()
