# Intelligent TicTacToe using Minimax Algorithm

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-20%20passed-brightgreen)

A complete Tic Tac Toe implementation in Python featuring an intelligent AI opponent that uses the Minimax algorithm for unbeatable gameplay.

## Features

- **Player vs Player** mode - Play with a friend
- **Player vs AI** mode - Challenge the computer
- **Three Difficulty Levels:**
  - 🟢 **Easy**: Random moves (for beginners)
  - 🟡 **Medium**: Basic strategy (blocks and takes wins)
  - 🔴 **Hard**: Minimax algorithm (unbeatable!)
- **Clean CLI Interface** - Easy to use
- **Game Statistics** - Track wins, losses, and draws
- **Input Validation** - Handles invalid moves gracefully

## Installation

### Prerequisites

- Python 3.8 or higher

### Setup

```bash
# Clone the repository
git clone https://github.com/logeshkannan19/Intelligent-tictactoe-minimax.git

# Navigate to project directory
cd intelligent-tictactoe-minimax
```

## Usage

### Running the Game

```bash
# Run using Python module
python -m src.main
```

### Interactive Example

```
==================================================
       TIC TAC TOE - Minimax AI Edition
==================================================

Welcome to Intelligent Tic Tac Toe!

Game Rules:
  • The board is a 3x3 grid
  • Players take turns placing their mark (X or O)
  • First to get 3 in a row wins!

  Board positions:
  1 │ 2 │ 3
  ───┼───┼───
  4 │ 5 │ 6
  ───┼───┼───
  7 │ 8 │ 9

----------------------------------------
Select Game Mode:
  1. Player vs Player
  2. Player vs AI
  3. Exit
----------------------------------------

Enter choice (1-3): 2

----------------------------------------
Select Difficulty Level:
  1. Easy   (Random moves)
  2. Medium (Basic strategy)
  3. Hard   (Minimax - Unbeatable!)
----------------------------------------
```

## Project Structure

```
intelligent-tictactoe-minimax/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Game entry point
│   ├── game/                   # Core game logic
│   │   ├── board.py           # Board state management
│   │   ├── player.py          # Player classes
│   │   └── rules.py           # Win/draw detection
│   ├── ai/                    # AI implementation
│   │   ├── minimax.py         # Minimax algorithm
│   │   └── difficulty.py      # Difficulty levels
│   └── utils/                 # Utilities
│       ├── display.py         # CLI display
│       └── helpers.py         # Helper functions
├── tests/                     # Unit tests
│   ├── test_game.py
│   └── test_ai.py
├── docs/                      # Documentation
│   ├── architecture.md
│   └── minimax_explanation.md
├── .gitignore
├── README.md
└── LICENSE
```

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_game.py

# Run with verbose output
pytest -v
```

## How the AI Works

The AI uses the **Minimax algorithm** to make optimal decisions:

1. **Explores all possible game states** - Simulates every possible move
2. **Evaluates outcomes** - Assigns scores (+10 for win, -10 for loss, 0 for draw)
3. **Chooses best move** - Picks the move that guarantees the best outcome

### Why is the Hard difficulty unbeatable?

The Minimax algorithm assumes **both players play perfectly**. Since the AI never makes a mistake and assumes the opponent also never makes mistakes, the best result against perfect play is always a **draw**. You can never beat the AI on Hard mode - at best, you can tie!

For a detailed explanation, see [docs/minimax_explanation.md](docs/minimax_explanation.md).

## Documentation

- [Architecture](docs/architecture.md) - System design and class structure
- [Minimax Explanation](docs/minimax_explanation.md) - Detailed algorithm explanation

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Minimax algorithm is a classic AI concept from game theory
- Inspired by classic terminal games

---

⭐ Star this repository if you found it helpful!