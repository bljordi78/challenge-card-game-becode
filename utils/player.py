import random

class Player:
    """
    This class allows to assign a set of cards to each player
    """
    def __init__(self, card: list, turn_count: int, number_of_cards: int, history: str):
               
        self.card = card
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def play(self):
        """
        The method makes a random choice in the cards
        Appends that card to the players history
        and return the given card
        """
        rd = random.choice(self.card)
        self.history.append(rd)
        print(f"{self.name} on turn {self.turn_count} played: {rd}.")
        return rd
 