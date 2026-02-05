class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def value(self):
        total = 0
        aces = 0
        
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
                total += 11
            else:
                total += card.value()
        
        # Adjust aces from 11 to 1 if needed
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        
        return total
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.value() == 21
    
    def is_bust(self):
        return self.value() > 21
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return " ".join(str(card) for card in self.cards)
