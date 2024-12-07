class ElementKilmukhametov:
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

element_na = ElementKilmukhametov(name="Sodium", symbol="Na", number=11)
element_na.dump()
