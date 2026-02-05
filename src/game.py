from .deck import Deck
from .hand import Hand
from .ui import UI


class BlackjackGame:
    def __init__(self, num_decks=1):
        self.deck = Deck(num_decks)
        self.player_hand = None
        self.dealer_hand = None
        self.game_over = False
        self.player_busted = False
        self.dealer_busted = False
    
    def deal_initial_hands(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
    
    def player_turn(self):
        while True:
            UI.print_separator()
            UI.print_dealer_turn(self.dealer_hand)
            UI.print_separator()
            UI.print_player_hand(self.player_hand)
            
            if self.player_hand.is_blackjack():
                UI.print_success("Blackjack! You got 21 with your first two cards!")
                return
            
            action = UI.get_player_action()
            
            if action == 'hit':
                card = self.deck.draw()
                self.player_hand.add_card(card)
                UI.print_info(f"You drew: {card}")
                
                if self.player_hand.is_bust():
                    UI.print_error("You busted! Over 21.")
                    self.player_busted = True
                    return
            else:
                UI.print_success("You stand.")
                return
    
    def dealer_turn(self):
        if self.player_busted:
            return
        
        UI.print_separator()
        UI.print_info("Dealer's turn...")
        
        while self.dealer_hand.value() < 17:
            card = self.deck.draw()
            self.dealer_hand.add_card(card)
            UI.print_info(f"Dealer draws: {card}")
            
            if self.dealer_hand.is_bust():
                UI.print_error("Dealer busted! Over 21.")
                self.dealer_busted = True
                return
        
        UI.print_success(f"Dealer stands with {self.dealer_hand.value()}.")
    
    def determine_winner(self):
        UI.print_separator()
        UI.print_dealer_final(self.dealer_hand)
        UI.print_separator()
        UI.print_player_hand(self.player_hand)
        UI.print_separator()
        
        player_value = self.player_hand.value()
        dealer_value = self.dealer_hand.value()
        
        if self.player_busted:
            UI.print_error("You busted! Dealer wins!")
            return "dealer"
        
        if self.dealer_busted:
            UI.print_success("Dealer busted! You win!")
            return "player"
        
        if player_value > dealer_value:
            if self.player_hand.is_blackjack():
                UI.print_success("Blackjack! You win!")
            else:
                UI.print_success("You win!")
            return "player"
        elif dealer_value > player_value:
            UI.print_error("Dealer wins!")
            return "dealer"
        else:
            UI.print_info("It's a tie! Push!")
            return "tie"
    
    def play_round(self):
        self.deal_initial_hands()
        self.player_turn()
        self.dealer_turn()
        return self.determine_winner()
