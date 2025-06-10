class Symbol:
    """
    This class allows to assign a colour [red, black]
    and a symbol [hearts, diamonds, clubs, spades] to one card 
    """
    def __init__(self, colour: str, icon: str):
        self.colour = colour
        self.icon = icon
    
    def __str__(self):    
        return f" The card has a {self.colour} {self.icon}."


class Card(Symbol):  # <--- Inherits from Symbol
    """ A class that defines a card: number, colour and icon. """

    def __init__(self, colour: str, icon: str, value: str):
        # Calling explicitly the Symbol constructor:
        super().__init__(colour, icon)
        # Intialising a new attribute called value
        self.value = value           

    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"The card: {self.value}, {self.colour}, {self.icon}"
