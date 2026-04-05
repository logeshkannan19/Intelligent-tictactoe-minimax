"""
Player Module - Manages player types (Human and AI).

This module contains:
- Player: Abstract base class for players
- HumanPlayer: Handles user input for moves
- AIPlayer: Implements AI logic with various difficulty levels

Author: Logesh Kannan
"""

import random
from abc import ABC, abstractmethod
from typing import List
from src.game.board import Board
from src.ai.difficulty import Difficulty


class Player(ABC):
    """
    Abstract base class for game players.
    
    Attributes:
        mark: Player's mark ('X' or 'O')
        name: Player's name
    
    Example:
        >>> player = HumanPlayer('X')
        >>> print(player.mark)  # 'X'
    """
    
    def __init__(self, mark: str, name: str = None) -> None:
        """
        Initialize player with their mark.
        
        Args:
            mark: Player's mark ('X' or 'O')
            name: Optional player name
        """
        self.mark = mark
        self.name = name if name else f"Player {mark}"
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    @abstractmethod
    def get_move(self, board: Board) -> int:
        """
        Get the player's next move.
        
        Args:
            board: Current game board
            
        Returns:
            Position index (0-8) for the move
        """
        pass
    
    def add_win(self) -> None:
        """Record a win for this player."""
        self.wins += 1
    
    def add_loss(self) -> None:
        """Record a loss for this player."""
        self.losses += 1
    
    def add_draw(self) -> None:
        """Record a draw for this player."""
        self.draws += 1
    
    def get_stats(self) -> str:
        """Return player's statistics as a string."""
        return f"{self.name}: {self.wins}W {self.losses}L {self.draws}D"


class HumanPlayer(Player):
    """
    Human player that gets moves from user input.
    
    Handles input validation and provides helpful error messages.
    
    Example:
        >>> player = HumanPlayer('X')
        >>> move = player.get_move(board)
    """
    
    def __init__(self, mark: str) -> None:
        """Initialize human player."""
        super().__init__(mark, name=f"Player {mark}")
    
    def get_move(self, board: Board) -> int:
        """
        Get move from human player via terminal input.
        
        Continuously prompts for input until a valid move is provided.
        
        Args:
            board: Current game board
            
        Returns:
            Valid position index (0-8)
        """
        while True:
            try:
                user_input = input(f"\n{self.name} ({self.mark}), enter your move (1-9): ").strip()
                
                if not user_input:
                    print("Please enter a number between 1 and 9.")
                    continue
                
                position = int(user_input) - 1
                
                if not board.is_valid_position(position):
                    print("Invalid position. Enter a number between 1 and 9.")
                    continue
                
                if not board.is_position_empty(position):
                    print("That position is already taken. Try again.")
                    continue
                
                return position
                
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")


class AIPlayer(Player):
    """
    AI player with multiple difficulty levels.
    
    Difficulty levels:
    - Easy: Random moves (no strategy)
    - Medium: Basic blocking and winning logic
    - Hard: Minimax algorithm (unbeatable)
    
    Example:
        >>> ai = AIPlayer('O', level='hard')
        >>> move = ai.get_move(board)
    """
    
    def __init__(self, mark: str, level: str = "hard") -> None:
        """
        Initialize AI player.
        
        Args:
            mark: AI's mark ('X' or 'O')
            level: Difficulty level ('easy', 'medium', 'hard')
        """
        super().__init__(mark, name=f"AI ({level})")
        self.level = Difficulty(level)
    
    def get_move(self, board: Board) -> int:
        """
        Get AI's move based on difficulty level.
        
        Args:
            board: Current game board
            
        Returns:
            Selected position index (0-8)
        """
        if self.level == Difficulty.EASY:
            return self._get_easy_move(board)
        elif self.level == Difficulty.MEDIUM:
            return self._get_medium_move(board)
        else:
            return self._get_hard_move(board)
    
    def _get_easy_move(self, board: Board) -> int:
        """Get a random available move."""
        available = board.get_available_moves()
        return random.choice(available)
    
    def _get_medium_move(self, board: Board) -> int:
        """
        Get move with basic strategy.
        
        Strategy:
        1. Win if possible
        2. Block opponent's winning move
        3. Take center if available
        4. Take random available position
        """
        from src.ai.minimax import MinimaxAI
        
        available = board.get_available_moves()
        
        # Try to win
        for pos in available:
            test_board = board.copy()
            test_board.make_move(pos, self.mark)
            from src.game.rules import GameRules
            if GameRules.check_winner(test_board) == self.mark:
                return pos
        
        # Block opponent's win
        opponent = 'X' if self.mark == 'O' else 'O'
        for pos in available:
            test_board = board.copy()
            test_board.make_move(pos, opponent)
            if GameRules.check_winner(test_board) == opponent:
                return pos
        
        # Take center if available
        if 4 in available:
            return 4
        
        # Take random
        return random.choice(available)
    
    def _get_hard_move(self, board: Board) -> int:
        """
        Get move using Minimax algorithm (unbeatable).
        
        Uses the Minimax algorithm to find the optimal move by exploring
        all possible game states and choosing the one that leads to the best outcome.
        
        Args:
            board: Current game board
            
        Returns:
            Optimal position index (0-8)
        """
        from src.ai.minimax import MinimaxAI
        
        minimax = MinimaxAI(self.mark)
        return minimax.get_best_move(board)