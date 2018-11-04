from Plant import Plant
from Menu import Menu
from bearlibterminal import terminal

p: Plant = Plant("Apple Tree", 10)
print(p)
p.water()
print(p)

terminal.open()

menu: Menu = Menu(terminal, 30)
menu.addOption("First Option", print)
menu.addOption("Second Option", print)
menu.displayOptions(10, 10)


while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
