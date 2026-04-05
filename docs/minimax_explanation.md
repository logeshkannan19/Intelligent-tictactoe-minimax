# Minimax Algorithm Explanation

## What is Minimax?

Minimax is a decision-making algorithm used in two-player games like Tic Tac Toe, Chess, and Checkers. It helps the AI find the best possible move by looking ahead at all possible future game states.

## How It Works

The algorithm is named because:
- **Maximize** the AI's score (try to win)
- **Minimize** the opponent's score (try to make the opponent lose)

Think of it as: "What's the worst-case scenario if I make this move, and how do I make that worst case as good as possible?"

## Simple Example

Imagine a simplified game with only 3 positions:

```
Position 0: AI wins (+10)
Position 1: Draw (0)
Position 2: AI loses (-10)
```

The AI will always choose Position 0 because:
- Position 0 gives the best outcome (+10)
- Position 1 gives a draw (0)
- Position 2 gives the worst outcome (-10)

## Tic Tac Toe Application

### Step 1: Evaluate All Possible Moves

When it's the AI's turn, it looks at every empty position:

```
Current Board:     After AI moves:
  X │ O │           X │ O │
───┼───┼───       ───┼───┼───
  X │ O │           X │ O │ O
───┼───┼───       ───┼───┼───
  7 │ 8 │ 9         7 │ 8 │ 9
```

If AI plays at position 7:
- It creates a new board state
- Then it simulates what the opponent would do
- And what the AI would do after that
- And so on...

### Step 2: Recursive Evaluation

The algorithm goes deep into each possibility:

```
Level 0 (AI's turn):      Try position 7
    │
    ├── Level 1 (Opponent): Try position 8
    │       │
    │       ├── Level 2 (AI): Try position 9 → WIN! (+10)
    │       └── ...
    │
    └── Level 1 (Opponent): Try position 9
            │
            └── Level 2 (AI): Try position 8 → LOSE! (-10)
```

### Step 3: Choose the Best Move

Working backwards from the deepest levels:

- If opponent plays at position 8, AI can win at 9 → Score: +10
- If opponent plays at position 9, AI loses at 8 → Score: -10

The AI chooses the branch that leads to the best guaranteed outcome.

## Score System

The AI uses these scores:
- **+10**: AI wins
- **0**: Draw
- **-10**: Opponent wins

The AI tries to get as close to +10 as possible, while assuming the opponent will try to get as close to -10 as possible.

## Depth Consideration

We add a twist: faster wins are better than slower wins!

```
WIN_SCORE - depth   →   A win in 2 moves is better than a win in 4 moves
LOSE_SCORE + depth  →   A loss in 4 moves is better than a loss in 2 moves
```

This makes the AI finish games quickly when it can win.

## Why It's Unbeatable

The Minimax algorithm assumes both players play perfectly. If the AI never makes a mistake, and assumes the opponent also never makes a mistake, then:

1. If there's a way to win, the AI will find it
2. If the opponent can force a win, the AI will see it coming and try to delay it
3. The best result against perfect play is always a **draw**

## Alpha-Beta Pruning (Optional Enhancement)

Minimax explores many unnecessary game states. Alpha-beta pruning "prunes" branches that can't lead to a better outcome than what we've already found.

```
Without pruning:  ~55,000 positions evaluated
With pruning:     ~15,000 positions evaluated (same result!)
```

This makes the AI faster without changing its decisions.

## Code Implementation

Here's the core Minimax concept in Python:

```python
def minimax(board, depth, is_maximizing):
    # Check if game is over
    if check_winner(board) == 'AI':
        return WIN_SCORE - depth
    if check_winner(board) == 'Opponent':
        return LOSE_SCORE + depth
    if board.is_full():
        return 0
    
    if is_maximizing:
        # AI's turn - maximize score
        best = -infinity
        for move in available_moves:
            score = minimax(board, depth + 1, False)
            best = max(best, score)
        return best
    else:
        # Opponent's turn - minimize score
        best = +infinity
        for move in available_moves:
            score = minimax(board, depth + 1, True)
            best = min(best, score)
        return best
```

## Summary

| Concept | Description |
|---------|-------------|
| **Minimax** | Algorithm that explores all game possibilities |
| **Maximizing** | AI tries to get highest score |
| **Minimizing** | Assumes opponent tries to get lowest score |
| **Depth** | Number of moves ahead being considered |
| **Why unbeatable** | Assumes perfect play from both sides |

The Minimax algorithm is the foundation of game AI and is used in many more complex games like Chess and Go (with enhancements like Monte Carlo Tree Search).