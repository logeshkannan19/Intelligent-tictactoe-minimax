# Architecture Documentation

## Project Overview

The Intelligent TicTacToe project is a Python-based Tic Tac Toe game with an AI opponent that uses the Minimax algorithm for optimal decision making.

## System Architecture

```
intelligent-tictactoe-minimax/
├── src/
│   ├── main.py              # Entry point
│   ├── game/                # Game logic
│   │   ├── board.py         # Board state management
│   │   ├── player.py        # Player classes (Human, AI)
│   │   └── rules.py         # Game rules and win detection
│   ├── ai/                  # AI implementation
│   │   ├── minimax.py       # Minimax algorithm
│   │   └── difficulty.py    # Difficulty levels
│   └── utils/               # Utilities
│       ├── display.py       # CLI display
│       └── helpers.py       # Helper functions
├── tests/                   # Unit tests
└── docs/                    # Documentation
```

## Module Descriptions

### Game Module (`src/game/`)

#### Board (`board.py`)
- Manages the 3x3 game board state
- Handles move making and undoing
- Provides available move calculation

#### Rules (`rules.py`)
- Win detection (rows, columns, diagonals)
- Draw detection
- Game state evaluation

#### Player (`player.py`)
- `Player`: Abstract base class
- `HumanPlayer`: Gets moves from user input
- `AIPlayer`: Delegates to AI based on difficulty

### AI Module (`src/ai/`)

#### Minimax (`minimax.py`)
- Implements the Minimax algorithm
- Provides optimal move selection
- Includes position evaluation for non-terminal states

#### Difficulty (`difficulty.py`)
- Enum for difficulty levels
- Easy (random), Medium (basic), Hard (Minimax)

### Utils Module (`src/utils/`)

#### Display (`display.py`)
- Board visualization
- Message formatting
- Menu display

#### Helpers (`helpers.py`)
- Input validation
- Confirmation dialogs

## Class Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         Player (ABC)                        │
├─────────────────────────────────────────────────────────────┤
│ + mark: str                                                  │
│ + name: str                                                  │
│ + wins: int                                                  │
│ + losses: int                                               │
│ + draws: int                                                │
├─────────────────────────────────────────────────────────────┤
│ + get_move(board: Board) -> int                              │
└─────────────────────────────────────────────────────────────┘
          │                           │
          ▼                           ▼
┌─────────────────────┐   ┌─────────────────────────────────────┐
│    HumanPlayer      │   │           AIPlayer                  │
├─────────────────────┤   ├─────────────────────────────────────┤
│ + get_move(): int   │   │ + level: Difficulty                 │
└─────────────────────┘   │ + get_move(): int                   │
                           │   - _get_easy_move(): int           │
                           │   - _get_medium_move(): int        │
                           │   - _get_hard_move(): int          │
                           └─────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                         Board                                │
├─────────────────────────────────────────────────────────────┤
│ + SIZE: int = 3                                             │
│ + WINNING_LINES: List[List[int]]                            │
│ + cells: List[str]                                          │
├─────────────────────────────────────────────────────────────┤
│ + make_move(position: int, mark: str) -> bool               │
│ + undo_move(position: int) -> bool                          │
│ + get_available_moves() -> List[int]                       │
│ + is_full() -> bool                                         │
│ + copy() -> Board                                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                       MinimaxAI                              │
├─────────────────────────────────────────────────────────────┤
│ + WIN_SCORE: int = 10                                       │
│ + LOSE_SCORE: int = -10                                     │
│ + ai_mark: str                                              │
│ + opponent_mark: str                                       │
├─────────────────────────────────────────────────────────────┤
│ + get_best_move(board: Board) -> int                        │
│ + _minimax(board, depth, is_maximizing) -> int              │
│ + evaluate_position(board: Board) -> int                   │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

1. **Game Start**: `main.py` initializes `Game` with appropriate players
2. **Turn Loop**: 
   - Display board
   - Call `player.get_move(board)`
   - Update board state
   - Check game end conditions
3. **AI Turn**:
   - `AIPlayer.get_move()` calls `MinimaxAI.get_best_move()`
   - Minimax explores game tree recursively
   - Returns optimal position

## Design Patterns

1. **Strategy Pattern**: AI difficulty levels
2. **Template Method**: Player base class
3. **Factory**: Difficulty enum conversion

## Testing Strategy

- Unit tests for each module
- Mock user input in HumanPlayer tests
- Test Minimax on specific board states
- Test edge cases (full board, no moves, etc.)