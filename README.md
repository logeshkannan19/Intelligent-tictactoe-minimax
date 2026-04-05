# 🧠 Intelligent Tic Tac Toe AI

### Minimax Algorithm | CLI + GUI | Python Project

A fully-featured Tic Tac Toe game built in Python with an intelligent AI opponent powered by the **Minimax algorithm**. The AI plays optimally and is unbeatable in hard mode.

---

## 🚀 Demo Features

* 🎮 Player vs Player mode
* 🤖 AI Opponent (3 Difficulty Levels)
* 🧠 Hard Mode: Unbeatable Minimax AI
* 🖥️ CLI + Tkinter GUI versions
* 📊 Score tracking system
* 🧪 Unit testing with pytest

---

## 🧠 AI Strategy

The AI uses the **Minimax algorithm**, a decision-making technique that:

* Explores all possible moves
* Simulates future game states
* Chooses the optimal move
* Ensures the best possible outcome

👉 Result: **The AI never loses**

---

## 📂 Project Structure

```
intelligent-tictactoe-minimax/
├── src/
│   ├── main.py              # Entry point (CLI)
│   ├── gui.py               # Tkinter GUI
│   ├── game/
│   │   ├── board.py         # Board logic
│   │   ├── rules.py         # Win/draw detection
│   │   └── player.py       # Player classes
│   ├── ai/
│   │   ├── minimax.py       # Minimax algorithm
│   │   └── difficulty.py   # Difficulty levels
│   └── utils/
│       ├── display.py       # CLI display
│       └── helpers.py       # Utilities
├── tests/
│   ├── test_game.py
│   └── test_ai.py
├── docs/
│   ├── architecture.md
│   └── minimax_explanation.md
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 🏗️ Architecture

### Module Overview

| Module | Description |
|--------|-------------|
| `src/game/board.py` | Manages 3x3 board state, move making/undoing |
| `src/game/rules.py` | Win/draw detection, game state evaluation |
| `src/game/player.py` | Player classes: HumanPlayer, AIPlayer |
| `src/ai/minimax.py` | Minimax algorithm for optimal AI |
| `src/ai/difficulty.py` | Difficulty enum (Easy/Medium/Hard) |
| `src/utils/display.py` | CLI board display & messages |
| `src/gui.py` | Tkinter GUI version |

### Class Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Player (Abstract)                        │
├─────────────────────────────────────────────────────────────┤
│ + mark: str    + name: str    + wins/losses/draws: int      │
├─────────────────────────────────────────────────────────────┤
│ + get_move(board: Board) -> int                             │
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
│ + SIZE: int = 3    + WINNING_LINES: List                    │
│ + cells: List[str]                                          │
├─────────────────────────────────────────────────────────────┤
│ + make_move(position, mark) -> bool                         │
│ + undo_move(position) -> bool                               │
│ + get_available_moves() -> List[int]                        │
│ + is_full() -> bool                                         │
│ + copy() -> Board                                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                       MinimaxAI                              │
├─────────────────────────────────────────────────────────────┤
│ + WIN_SCORE: int = 10    + LOSE_SCORE: int = -10            │
│ + ai_mark: str    + opponent_mark: str                      │
├─────────────────────────────────────────────────────────────┤
│ + get_best_move(board) -> int                               │
│ + _minimax(board, depth, is_maximizing) -> int             │
│ + evaluate_position(board) -> int                           │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Game Start**: `main.py` initializes `Game` with players
2. **Turn Loop**: Display → Get Move → Update Board → Check End
3. **AI Turn**: `AIPlayer.get_move()` → `MinimaxAI.get_best_move()` → Optimal Position

---

## ⚙️ Installation

```bash
git clone https://github.com/logeshkannan19/Intelligent-tictactoe-minimax.git
cd Intelligent-tictactoe-minimax
pip install -e .
```

---

## ▶️ Run the Game

### CLI

```bash
PYTHONPATH=src python -m src.main
```

### GUI (Tkinter)

```bash
PYTHONPATH=src python -m src.gui
```

### Web App (Streamlit)

```bash
pip install streamlit
streamlit run webapp.py
```

---

## 🚀 Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [streamlit.io](https://streamlit.io) and sign in
3. Click "New App" and select your repository
4. Set the main file to `webapp.py`
5. Click "Deploy!"

Your web app will be live at: `https://your-app-name.streamlit.app`

---

## 🧪 Run Tests

```bash
pytest
```

---

## 📸 Screenshots

*Add screenshots here (very important for GitHub visibility)*

---

## 🔥 Future Improvements

* Online multiplayer
* Reinforcement Learning AI
* Enhanced web UI with animations

---

## 📜 License

MIT License