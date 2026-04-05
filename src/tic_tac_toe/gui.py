"""
Tic Tac Toe GUI - Tkinter-based graphical interface.

This module provides a graphical user interface for Tic Tac Toe
with an AI opponent using the Minimax algorithm.

Author: AI Assistant
"""

import tkinter as tk
from tkinter import messagebox
import sys


class TicTacToeGUI:
    """
    Tkinter-based GUI for Tic Tac Toe.
    
    Features:
    - 3x3 grid buttons
    - Player vs AI mode
    - Difficulty selection
    - Score tracking
    - Visual feedback
    """
    
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Game state
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.game_active = True
        self.difficulty = 'hard'  # hard, medium, easy
        
        # Score tracking
        self.player_wins = 0
        self.ai_wins = 0
        self.draws = 0
        
        # AI mark
        self.ai_mark = 'O'
        self.player_mark = 'X'
        
        # Create UI
        self._create_widgets()
        self._create_menu()
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Title
        self.title_label = tk.Label(
            self.root, 
            text="Tic Tac Toe", 
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=10)
        
        # Score display
        self.score_label = tk.Label(
            self.root,
            text=f"Player (X): 0  |  AI (O): 0  |  Draws: 0",
            font=("Arial", 12)
        )
        self.score_label.pack(pady=5)
        
        # Status message
        self.status_label = tk.Label(
            self.root,
            text="Your turn!",
            font=("Arial", 14),
            fg="blue"
        )
        self.status_label.pack(pady=5)
        
        # Game board frame
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=20)
        
        # Create 3x3 grid of buttons
        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                self.board_frame,
                text="",
                font=("Arial", 32, "bold"),
                width=3,
                height=1,
                bg="#f0f0f0",
                fg="black",
                command=lambda i=i: self.on_button_click(i)
            )
            row, col = i // 3, i % 3
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)
        
        # Control buttons frame
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=10)
        
        # New Game button
        self.new_game_btn = tk.Button(
            self.control_frame,
            text="New Game",
            font=("Arial", 12),
            command=self.reset_game,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        )
        self.new_game_btn.grid(row=0, column=0, padx=5)
        
        # Difficulty button
        self.difficulty_btn = tk.Button(
            self.control_frame,
            text=f"Difficulty: {self.difficulty.capitalize()}",
            font=("Arial", 12),
            command=self.cycle_difficulty,
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=5
        )
        self.difficulty_btn.grid(row=0, column=1, padx=5)
    
    def _create_menu(self):
        """Create menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Game menu
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.reset_game)
        game_menu.add_command(label="Exit", command=self.root.quit)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="How to Play", command=self.show_help)
    
    def show_help(self):
        """Display help information."""
        messagebox.showinfo(
            "How to Play",
            "Tic Tac Toe - How to Play\n\n"
            "1. Click on an empty cell to place your mark (X)\n"
            "2. Get 3 in a row (horizontal, vertical, or diagonal) to win\n"
            "3. The AI (O) will make its move after yours\n\n"
            "Difficulty Levels:\n"
            "- Easy: Random moves\n"
            "- Medium: Basic strategy\n"
            "- Hard: Unbeatable AI (Minimax)"
        )
    
    def cycle_difficulty(self):
        """Cycle through difficulty levels."""
        levels = ['easy', 'medium', 'hard']
        current_idx = levels.index(self.difficulty)
        self.difficulty = levels[(current_idx + 1) % 3]
        self.difficulty_btn.config(text=f"Difficulty: {self.difficulty.capitalize()}")
        self.reset_game()
    
    def on_button_click(self, position):
        """Handle button click for player's move."""
        if not self.game_active or self.board[position] != '':
            return
        
        # Make player's move
        self.make_move(position, self.player_mark)
        
        if self.check_game_end():
            return
        
        # AI's turn
        self.status_label.config(text="AI is thinking...", fg="orange")
        self.root.update()
        
        # Get AI move
        ai_position = self.get_ai_move()
        self.make_move(ai_position, self.ai_mark)
        
        self.check_game_end()
    
    def make_move(self, position, mark):
        """Make a move on the board."""
        self.board[position] = mark
        self.buttons[position].config(text=mark, fg="red" if mark == "X" else "blue")
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_ai_move(self):
        """Get AI's move based on difficulty level."""
        if self.difficulty == 'easy':
            return self._get_easy_move()
        elif self.difficulty == 'medium':
            return self._get_medium_move()
        else:
            return self._get_hard_move()
    
    def _get_easy_move(self):
        """Get random available move."""
        available = [i for i in range(9) if self.board[i] == '']
        return available[int(len(available) * __import__('random').random())]
    
    def _get_medium_move(self):
        """Get move with basic strategy."""
        available = [i for i in range(9) if self.board[i] == '']
        
        # Try to win
        for pos in available:
            test_board = self.board.copy()
            test_board[pos] = self.ai_mark
            if self._check_winner(test_board) == self.ai_mark:
                return pos
        
        # Block opponent
        for pos in available:
            test_board = self.board.copy()
            test_board[pos] = self.player_mark
            if self._check_winner(test_board) == self.player_mark:
                return pos
        
        # Take center
        if 4 in available:
            return 4
        
        return available[int(len(available) * __import__('random').random())]
    
    def _get_hard_move(self):
        """Get move using Minimax algorithm."""
        best_score = float('-inf')
        best_move = None
        
        available = [i for i in range(9) if self.board[i] == '']
        
        for move in available:
            # Make move
            self.board[move] = self.ai_mark
            
            # Get minimax value
            score = self._minimax(self.board, 0, False)
            
            # Undo move
            self.board[move] = ''
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _minimax(self, board, depth, is_maximizing):
        """Minimax algorithm."""
        winner = self._check_winner(board)
        
        if winner == self.ai_mark:
            return 10 - depth
        elif winner == self.player_mark:
            return depth - 10
        elif '' not in board:
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = self.ai_mark
                    score = self._minimax(board, depth + 1, False)
                    board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = self.player_mark
                    score = self._minimax(board, depth + 1, True)
                    board[i] = ''
                    best_score = min(score, best_score)
            return best_score
    
    def _check_winner(self, board):
        """Check winner on given board state."""
        winning_lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for line in winning_lines:
            if board[line[0]] and board[line[0]] == board[line[1]] == board[line[2]]:
                return board[line[0]]
        
        if '' not in board:
            return 'draw'
        
        return None
    
    def check_game_end(self):
        """Check if game has ended."""
        winner = self._check_winner(self.board)
        
        if winner:
            self.game_active = False
            
            if winner == 'draw':
                self.draws += 1
                self.status_label.config(text="It's a Draw!", fg="purple")
                messagebox.showinfo("Game Over", "It's a Draw!")
            elif winner == self.player_mark:
                self.player_wins += 1
                self.status_label.config(text="You Win!", fg="green")
                messagebox.showinfo("Game Over", "Congratulations! You Win!")
            else:
                self.ai_wins += 1
                self.status_label.config(text="AI Wins!", fg="red")
                messagebox.showinfo("Game Over", "AI Wins! Better luck next time.")
            
            self.update_score()
            return True
        
        # Update status for next turn
        if self.current_player == self.player_mark:
            self.status_label.config(text="Your turn!", fg="blue")
        
        return False
    
    def update_score(self):
        """Update score display."""
        self.score_label.config(
            text=f"Player (X): {self.player_wins}  |  AI (O): {self.ai_wins}  |  Draws: {self.draws}"
        )
    
    def reset_game(self):
        """Reset the game for a new round."""
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.game_active = True
        
        for btn in self.buttons:
            btn.config(text="", bg="#f0f0f0")
        
        self.status_label.config(text="Your turn!", fg="blue")


def main():
    """Main entry point for GUI version."""
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()