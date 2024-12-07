class ElementMukhamedov:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name
    
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def number(self):
        return self.__number


    def dump(self):
        print(f"Name: {self.name}\t Symbol: {self.symbol}\t Number: {self.number}")

element = ElementMukhamedov(name="Silicon", symbol="Si", number=14)
element.dump()
