from deck import Deck

class Board:
    """
    This class allows to create and follow the game.
    States the player in the game
    What cards they get
    What cards they played at each turn 
    """
    def __init__(self, players: list, turn_count: int, active_cards: int, history_cards: list):
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards
    
    def start_game(self):
        deck = Deck()
        deck.fill_deck()
        deck.distribute(self.players)
 
