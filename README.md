# BlaCLI Jack ♠ ♥ ♦ ♣

A fun, interactive Blackjack game that runs in your terminal with colorful ASCII art!

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- 🎴 Beautiful ASCII art card designs
- 🎨 Colorful terminal output using colorama
- 🎮 Classic Blackjack gameplay (hit/stand)
- 📊 Game statistics tracking
- 🔄 Play multiple rounds
- 🎯 Dealer AI follows standard casino rules (hits on 16, stands on 17)

## Screenshots

```
    ♠ ♥ ♦ ♣  BlaCLI JACK  ♠ ♥ ♦ ♣

Dealer's Hand
  ┌─────────┐  ┌─────────┐
  │ ▓▓▓▓▓▓▓ │  │K        │
  │ ▓▓▓▓▓▓▓ │  │         │
  │ ▓▓▓▓▓▓▓ │  │    ♥    │
  │ ▓▓▓▓▓▓▓ │  │         │
  │ ▓▓▓▓▓▓▓ │  │        K│
  └─────────┘  └─────────┘

Your Hand
  ┌─────────┐  ┌─────────┐
  │A        │  │Q        │
  │         │  │         │
  │    ♠    │  │    ♦    │
  │         │  │         │
  │        A│  │        Q│
  └─────────┘  └─────────┘
  Value: 21 (BLACKJACK!)
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BlaCLI-Jack.git
   cd BlaCLI-Jack
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the game:
```bash
python main.py
```

### How to Play

1. The dealer and you are dealt two cards each
2. The dealer's first card is hidden
3. Choose to **Hit** (draw another card) or **Stand** (keep current hand)
4. Try to get as close to 21 as possible without going over
5. Dealer must hit on 16 or less, stand on 17 or more
6. Player with the higher value wins (without going over 21)

### Controls

- `H` or `Hit` - Draw another card
- `S` or `Stand` - Keep your current hand
- `Y` or `Yes` - Play another round
- `N` or `No` - Exit the game

## Project Structure

```
BlaCLI Jack/
├── main.py              # Entry point for the game
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
└── src/
    ├── __init__.py
    ├── card.py         # Card class
    ├── deck.py         # Deck management
    ├── hand.py         # Hand logic and scoring
    ├── game.py         # Main game logic
    └── ui.py           # Terminal UI and ASCII art
```

## Game Rules

- Number cards (2-10) are worth their face value
- Face cards (J, Q, K) are worth 10
- Aces are worth 11 (automatically adjusted to 1 if hand would bust)
- **Blackjack**: 21 with first two cards
- **Bust**: Hand value exceeds 21
- **Push**: Tie between player and dealer

## Dependencies

- [colorama](https://pypi.org/project/colorama/) - Cross-platform colored terminal output

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built as a fun CLI project to learn Python
- Inspired by classic casino Blackjack

## Future Enhancements

Possible features to add:
- 💰 Betting system with chips
- 🎲 Split pairs option
- 📈 Double down feature
- 🎰 Insurance option
- 💾 Save/load game statistics
- 🏆 High score tracking

---

Made with ♥ by Eidolom

Enjoy the game! 🎮
