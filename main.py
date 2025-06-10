import random
random.seed(5)

from utils.board import Board

# Set the game: players, cards, cards per player
people = ["Alice", "Benjamin", "Clara", "David", "Emma", "Felix", "Grace", "Hugo", "Isla", "Jack"]
number_of_players = int(input("How many players would be in the game? (max. 10)"))

if number_of_players > 10:
    print("Too many players. Start over!")

else:
    players = random.sample(people, number_of_players)


# Initialising counters and history
turn_count = 0
number_of_cards = 0
history = []

game = Board(players, turn_count, number_of_cards, history)
