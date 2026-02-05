from src.game import BlackjackGame
from src.ui import UI
from colorama import init

init(autoreset=False)


def main():
    UI.clear()
    UI.print_title()
    
    games_played = 0
    player_wins = 0
    dealer_wins = 0
    ties = 0
    
    while True:
        game = BlackjackGame()
        winner = game.play_round()
        
        games_played += 1
        if winner == "player":
            player_wins += 1
        elif winner == "dealer":
            dealer_wins += 1
        else:
            ties += 1
        
        UI.print_separator()
        print(f"STATISTICS")
        print(f"   Games: {games_played} | Player: {player_wins} | Dealer: {dealer_wins} | Ties: {ties}")
        
        if not UI.get_play_again():
            break
        
        UI.clear()
        UI.print_title()
    
    UI.print_separator()
    print(f"\nThanks for playing BlaCLI Jack!\n")
    print(f"Final Score: Player {player_wins} - {dealer_wins} Dealer")
    print()

if __name__ == "__main__":
    main()
