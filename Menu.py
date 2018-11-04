from typing import List, Dict, Any, Callable


class Menu():
    # options = [{"text": str, "callback": function}]
    # list of dictionaries
    options: List[Dict[str, Any]] = []

    def __init__(self, terminal, width: int):
        self.width: int = width
        self.terminal = terminal

    def addOption(self, text: str, callback: Callable):
        self.options.append({"text": text, "callback": callback})

    def displayOptions(self, posx: int, posy: int):
        for index, option in enumerate(self.options):
            optionText = "{}. {}".format(index, option["text"])
            self.terminal.print(posx, posy+index, optionText)
        self.terminal.refresh()
