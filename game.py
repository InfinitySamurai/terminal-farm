from Plant import Plant
from Menu import Menu
from bearlibterminal import terminal

p: Plant = Plant("Apple Tree", 10)

terminal.open()

menu: Menu = Menu(terminal, 30)
menu.addOption("First Option", p.water)
menu.addOption("Second Option", p.water)
menu.displayOptions(10, 10)

print(p)
menu.selectOption(0)
print(p)
menu.selectOption(1)
print(p)

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
