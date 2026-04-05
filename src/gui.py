"""
GUI Module - Tkinter-based graphical interface for Tic Tac Toe.

This module provides a graphical user interface for Tic Tac Toe
with an AI opponent using the Minimax algorithm.

Author: Logesh Kannan
"""

import tkinter as tk
from tkinter import messagebox
import random
from src.game.board import Board
from src.game.rules import GameRules
from src.ai.minimax import MinimaxAI
from src.ai.difficulty import Difficulty


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
    
    def __init__(self, root: tk.Tk) -> None:
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Tic Tac Toe - Minimax AI")
        self.root.geometry("400x520")
        self.root.resizable(False, False)
        
        # Game state
        self.board = Board()
        self.current_player = "X"
        self.game_active = True
        self.difficulty = Difficulty.HARD
        
        # Score tracking
        self.player_wins = 0
        self.ai_wins = 0
        self.draws = 0
        
        # Marks
        self.ai_mark = "O"
        self.player_mark = "X"
        
        # AI
        self.ai = MinimaxAI(self.ai_mark)
        
        # Create UI
        self._create_widgets()
    
    def _create_widgets(self) -> None:
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
                command=lambda i=i: self._on_button_click(i)
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
            command=self._reset_game,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        )
        self.new_game_btn.grid(row=0, column=0, padx=5)
        
        # Difficulty button
        self.difficulty_btn = tk.Button(
            self.control_frame,
            text=f"Difficulty: {self.difficulty}",
            font=("Arial", 12),
            command=self._cycle_difficulty,
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=5
        )
        self.difficulty_btn.grid(row=0, column=1, padx=5)
    
    def _on_button_click(self, position: int) -> None:
        """Handle button click for player's move."""
        if not self.game_active or not self.board.is_position_empty(position):
            return
        
        # Make player's move
        self._make_move(position, self.player_mark)
        
        if self._check_game_end():
            return
        
        # AI's turn
        self.status_label.config(text="AI is thinking...", fg="orange")
        self.root.update()
        
        # Get AI move
        ai_position = self._get_ai_move()
        self._make_move(ai_position, self.ai_mark)
        
        self._check_game_end()
    
    def _make_move(self, position: int, mark: str) -> None:
        """Make a move on the board and update UI."""
        self.board.make_move(position, mark)
        color = "red" if mark == "X" else "blue"
        self.buttons[position].config(text=mark, fg=color)
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def _get_ai_move(self) -> int:
        """Get AI's move based on difficulty level."""
        if self.difficulty == Difficulty.EASY:
            return self._get_easy_move()
        elif self.difficulty == Difficulty.MEDIUM:
            return self._get_medium_move()
        else:
            return self.ai.get_best_move(self.board)
    
    def _get_easy_move(self) -> int:
        """Get random available move."""
        available = self.board.get_available_moves()
        return random.choice(available)
    
    def _get_medium_move(self) -> int:
        """Get move with basic strategy."""
        available = self.board.get_available_moves()
        
        # Try to win
        for pos in available:
            test_board = self.board.copy()
            test_board.make_move(pos, self.ai_mark)
            if GameRules.check_winner(test_board) == self.ai_mark:
                return pos
        
        # Block opponent
        for pos in available:
            test_board = self.board.copy()
            test_board.make_move(pos, self.player_mark)
            if GameRules.check_winner(test_board) == self.player_mark:
                return pos
        
        # Take center
        if 4 in available:
            return 4
        
        return random.choice(available)
    
    def _check_game_end(self) -> bool:
        """Check if game has ended."""
        winner = GameRules.check_winner(self.board)
        
        if winner:
            self.game_active = False
            
            if self.board.is_full() and not winner:
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
            
            self._update_score()
            return True
        
        # Update status for next turn
        if self.game_active and self.current_player == self.player_mark:
            self.status_label.config(text="Your turn!", fg="blue")
        
        return False
    
    def _update_score(self) -> None:
        """Update score display."""
        self.score_label.config(
            text=f"Player (X): {self.player_wins}  |  AI (O): {self.ai_wins}  |  Draws: {self.draws}"
        )
    
    def _reset_game(self) -> None:
        """Reset the game for a new round."""
        self.board = Board()
        self.current_player = "X"
        self.game_active = True
        
        for btn in self.buttons:
            btn.config(text="", bg="#f0f0f0")
        
        self.status_label.config(text="Your turn!", fg="blue")
    
    def _cycle_difficulty(self) -> None:
        """Cycle through difficulty levels."""
        levels = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]
        current_idx = levels.index(self.difficulty)
        self.difficulty = levels[(current_idx + 1) % 3]
        self.difficulty_btn.config(text=f"Difficulty: {self.difficulty}")
        
        # Update AI with new difficulty
        if self.difficulty == Difficulty.HARD:
            self.ai = MinimaxAI(self.ai_mark)
        
        self._reset_game()


def main() -> None:
    """Main entry point for GUI version."""
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()