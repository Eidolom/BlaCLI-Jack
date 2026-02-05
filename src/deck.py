import random
from .card import Card


class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = []
        self.reset()
    
    def reset(self):
        self.cards = []
        for _ in range(self.num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    self.cards.append(Card(suit, rank))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if not self.cards:
            self.reset()
        return self.cards.pop()
    
    def cards_remaining(self):
        return len(self.cards)
