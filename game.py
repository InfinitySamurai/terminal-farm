from Plant import Plant
from Menu import Menu
from bearlibterminal import terminal

p: Plant = Plant("Apple Tree", 10, "@")

terminal.open()

menu: Menu = Menu(terminal, 30)
menu.addOption("First Option", p.water)
menu.addOption("Second Option", p.water)
menu.displayOptions(10, 10)


p.display(terminal, 30, 30)
p.update()
p.display(terminal, 31, 30)

while terminal.peek() != terminal.TK_CLOSE:
    input = terminal.read()
    if(input == 30):
        menu.selectOption(0)
    elif(input == 31):
        menu.selectOption(1)
    elif(input == 224 or input == 41):
        terminal.close()

terminal.close()
