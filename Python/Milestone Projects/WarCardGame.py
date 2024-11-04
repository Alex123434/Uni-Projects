import random

values = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
suits = ("Hearts", "Diamonds", "Clubs", "Spades" )
ranks = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

# Card Class

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
two_hearts = Card("Hearts", "Two")
three_clubs = Card("Clubs", "Three")

print(two_hearts)
print(three_clubs.value)

# Deck Class
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create a new card and add it to the deck
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

# Shuffle Deck 

    def shuffle(self):
            random.shuffle(self.all_cards)

    def deal_one_card(self):
         return self.all_cards.pop()

new_deck = Deck()
new_deck.shuffle()
print(new_deck.all_cards[0])

       