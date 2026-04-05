# Tic Tac Toe

A complete Tic Tac Toe implementation in Python with an intelligent AI opponent using the Minimax algorithm.

## Features

- **Player vs Player** mode
- **Player vs AI** mode with 3 difficulty levels:
  - Easy: Random moves
  - Medium: Basic blocking and winning logic
  - Hard: Unbeatable Minimax algorithm
- **Tkinter GUI** version available
- Score tracking across games
- Comprehensive test suite

## Requirements

- Python 3.8+

## Installation

```bash
# Clone or navigate to the project directory
cd tic_tac_toe

# Install the package (optional)
pip install -e .
```

## Running the Game

### Command-Line Version

```bash
# Using the installed script (after pip install)
tic-tac-toe

# Or directly with Python
PYTHONPATH=src python3 -m tic_tac_toe.main
```

### GUI Version

```bash
PYTHONPATH=src python3 -m tic_tac_toe.gui

# Or after installation
tic-tac-toe-gui
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tic_tac_toe
```

## Project Structure

```
tic_tac_toe/
├── pyproject.toml          # Package configuration
├── README.md               # This file
├── src/
│   └── tic_tac_toe/        # Main package
│       ├── __init__.py     # Package exports
│       ├── board.py        # Board state & logic
│       ├── player.py       # Human & AI players
│       ├── game.py         # Game loop
│       ├── main.py         # CLI entry point
│       └── gui.py          # Tkinter GUI
└── tests/
    └── test_tic_tac_toe.py # Unit tests
```

## AI Implementation

### Minimax Algorithm

The "Hard" difficulty uses the **Minimax algorithm** to achieve unbeatable play:

1. **Recursive evaluation**: Explores all possible game states
2. **Scoring**: +10 for AI win, -10 for opponent win, 0 for draw
3. **Optimization**: Prefers faster wins (lower depth = higher score)

### Alpha-Beta Pruning (Optional Enhancement)

The algorithm can be optimized with alpha-beta pruning to reduce the number of nodes evaluated while maintaining the same result.

## License

MIT