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
│   ├── game/
│   │   ├── board.py         # Board logic
│   │   ├── rules.py         # Win/draw detection
│   │   └── player.py        # Player classes
│   ├── ai/
│   │   ├── minimax.py       # Minimax algorithm
│   │   └── difficulty.py   # Difficulty levels
│   └── utils/
│       ├── display.py      # CLI display
│       └── helpers.py      # Utilities
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
* Web-based version (React + Flask)

---

## 📜 License

MIT License