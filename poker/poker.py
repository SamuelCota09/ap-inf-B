import random

# deck is the set (no duplicates, unordered) that holds every card in the game
# Each card is represented as "rank+suit" (for example: "A♠", "10♦")
deck = {
    "2♦", "2♠", "2♥", "2♣",
    "3♦", "3♠", "3♥", "3♣",
    "4♦", "4♠", "4♥", "4♣",
    "5♦", "5♠", "5♥", "5♣",
    "6♦", "6♠", "6♥", "6♣",
    "7♦", "7♠", "7♥", "7♣",
    "8♦", "8♠", "8♥", "8♣",
    "9♦", "9♠", "9♥", "9♣",
    "10♦", "10♠", "10♥", "10♣",
    "J♦", "J♠", "J♥", "J♣",
    "Q♦", "Q♠", "Q♥", "Q♣",
    "K♦", "K♠", "K♥", "K♣",
    "A♦", "A♠", "A♥", "A♣",
}

table = random.sample(sorted(deck), 3)

# hand is a list with 5 different random cards from the deck

player_1 = random.sample(sorted(deck), 2)

player_2 = random.sample(sorted(deck), 2)

hand_1 = table + player_1

hand_2 = table + player_2

print("Deck:", sorted(deck))
print("1st Hand:", hand_1)
print("2st Hand:", hand_2)

# Optional rank mapping for later checks
rank_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

points_1 = []
for card in hand_1:
    rank = card[:-1] # card[:-1] removes the last card in the hand
    points_1.append(rank_values.get(rank, 0))

print("Points:", points_1)


points_2 = []
for card in hand_2:
    rank = card[:-1]
    points_2.append(rank_values.get(rank, 0))

print("Points:", points_2)

# 1. Extract the rank (everything except the last character, which is the suit)

ranks_1 = [card[:-1] for card in hand_1]
print(ranks_1)

ranks_2 = [card[:-1] for card in hand_2]
print(ranks_2)

# 2. Condition: If the number of unique ranks equals the total number of cards
if len(set(ranks_1)) == len(ranks_1) and len(set(ranks_2)) == len(ranks_2):
    print("There are no repeated ranks!")
    if max(points_1) > max(points_2): #max(list) é uma função que extrái o maior valor que está dentro da lista list
        print("1st hand wins")
    elif max(points_1) < max(points_2):
        print("2nd hand wins")
    else:
        print("Draw")
else:
    print("Found a repeated rank.")
