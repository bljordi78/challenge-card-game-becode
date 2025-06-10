from random import shuffle
from card import Card

class Deck:
    """
    This class allows to create a deck with 52 unique cards 
    """
    def __init__(self):
        """Initialise the lists of values"""
        colour = ['red', 'black']
        icon = ['hearts', 'diamonds', 'clubs', 'spades']
        value = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        
        self.obj = Card(colour, icon, value)
    
    def fill_deck(self):
        """ Iterate through all lists to create a list of unique combinations"""
        deck = []
        for s in self.obj.icon:
            for v in self.obj.value:
                if s in ['hearts', 'diamonds']: 
                    card = f"{v}-red-{s}"
                    deck.append(card)
                else:
                    card = f"{v}-red-{s}"
                    deck.append(card)
        shuffle(deck)
        return deck
    
    def shuffle(self):
        pass

    def distribute(self, player):
        pass
        




deck = Deck()
deck = deck.fill_deck()
print(deck)

