from colorama import Fore, Back, Style


class UI:
    CARD_WIDTH = 9
    CARD_HEIGHT = 7
    
    @staticmethod
    def clear():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_title():
        title = f"""{Fore.CYAN}
    ♠ ♥ ♦ ♣  BlaCLI JACK  ♠ ♥ ♦ ♣
{Style.RESET_ALL}"""
        print(title)
    
    @staticmethod
    def draw_card(card, hidden=False):
        if hidden:
            lines = [
                "┌─────────┐",
                "│ ▓▓▓▓▓▓▓ │",
                "│ ▓▓▓▓▓▓▓ │",
                "│ ▓▓▓▓▓▓▓ │",
                "│ ▓▓▓▓▓▓▓ │",
                "│ ▓▓▓▓▓▓▓ │",
                "└─────────┘",
            ]
        else:
            rank = card.rank
            suit = card.suit
            
            if suit in ['♥', '♦']:
                color = Fore.RED
            else:
                color = Fore.BLACK
            
            rank_top = f"{rank:<2}"
            rank_bottom = f"{rank:>2}"
            
            lines = [
                "┌─────────┐",
                f"│{color}{rank_top}{Style.RESET_ALL}       │",
                "│         │",
                f"│    {color}{suit}{Style.RESET_ALL}    │",
                "│         │",
                f"│       {color}{rank_bottom}{Style.RESET_ALL}│",
                "└─────────┘",
            ]
        
        return lines
    
    @staticmethod
    def display_hand(hand, label="Hand", hidden_count=0):
        print(f"\n{Fore.YELLOW}{label}{Style.RESET_ALL}")
        
        card_lines = []
        for i, card in enumerate(hand.cards):
            is_hidden = i < hidden_count
            card_lines.append(UI.draw_card(card, hidden=is_hidden))
        
        if not card_lines:
            print("  (empty)")
            return
        
        for row in range(UI.CARD_HEIGHT):
            line = "  "
            for card_art in card_lines:
                line += card_art[row] + "  "
            print(line)
        
        if hidden_count == 0:
            value_str = f"Value: {hand.value()}"
            if hand.is_blackjack():
                print(f"  {Fore.GREEN}{value_str} (BLACKJACK!){Style.RESET_ALL}")
            elif hand.is_bust():
                print(f"  {Fore.RED}{value_str} (BUST!){Style.RESET_ALL}")
            else:
                print(f"  {value_str}")
    
    @staticmethod
    def print_dealer_turn(dealer_hand):
        UI.display_hand(dealer_hand, label="Dealer's Hand", hidden_count=1)
    
    @staticmethod
    def print_dealer_final(dealer_hand):
        UI.display_hand(dealer_hand, label="Dealer's Hand", hidden_count=0)
    
    @staticmethod
    def print_player_hand(player_hand):
        UI.display_hand(player_hand, label="Your Hand", hidden_count=0)
    
    @staticmethod
    def print_separator():
        print(f"\n{Fore.CYAN}{'─' * 60}{Style.RESET_ALL}\n")
    
    @staticmethod
    def print_message(message, color=Fore.WHITE):
        print(f"{color}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def print_success(message):
        UI.print_message(f"✓ {message}", Fore.GREEN)
    
    @staticmethod
    def print_error(message):
        UI.print_message(f"✗ {message}", Fore.RED)
    
    @staticmethod
    def print_info(message):
        UI.print_message(f"ℹ {message}", Fore.CYAN)
    
    @staticmethod
    def get_player_action():
        while True:
            choice = input(f"\n{Fore.MAGENTA}(H)it or (S)tand? → {Style.RESET_ALL}").strip().upper()
            if choice in ['H', 'HIT']:
                return 'hit'
            elif choice in ['S', 'STAND']:
                return 'stand'
            else:
                UI.print_error("Invalid choice. Please enter 'H' or 'S'.")
    
    @staticmethod
    def get_play_again():
        while True:
            choice = input(f"\n{Fore.MAGENTA}Play again? (Y/N) → {Style.RESET_ALL}").strip().upper()
            if choice in ['Y', 'YES']:
                return True
            elif choice in ['N', 'NO']:
                return False
            else:
                UI.print_error("Invalid choice. Please enter 'Y' or 'N'.")
