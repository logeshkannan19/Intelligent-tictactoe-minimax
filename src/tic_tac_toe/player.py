"""
Player Module - Manages player types (Human and AI).

This module contains:
- HumanPlayer: Handles user input for moves
- AIPlayer: Implements AI logic with various difficulty levels
  including Minimax algorithm for unbeatable play

Author: AI Assistant
"""

import random
from tic_tac_toe.board import Board


class Player:
    """
    Base class for game players.
    
    Attributes:
        mark (str): Player's mark ('X' or 'O')
        name (str): Player's name
    """
    
    def __init__(self, mark, name=None):
        """Initialize player with their mark."""
        self.mark = mark
        self.name = name if name else mark
    
    def get_move(self, board):
        """
        Get the player's next move.
        
        Args:
            board (Board): Current game board
            
        Returns:
            int: Position index (0-8) for the move
        """
        raise NotImplementedError("Subclasses must implement get_move()")


class HumanPlayer(Player):
    """
    Human player that gets moves from user input.
    
    Handles input validation and provides helpful error messages.
    """
    
    def __init__(self, mark):
        """Initialize human player."""
        super().__init__(mark, name=f"Player {mark}")
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    def get_move(self, board):
        """
        Get move from human player via terminal input.
        
        Args:
            board (Board): Current game board
            
        Returns:
            int: Valid position index (0-8)
        """
        while True:
            try:
                user_input = input(f"\n{self.name}, enter your move (1-9): ").strip()
                
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
    
    Attributes:
        level (str): Difficulty level ('easy', 'medium', 'hard')
    """
    
    def __init__(self, mark, level='hard'):
        """
        Initialize AI player.
        
        Args:
            mark (str): AI's mark ('X' or 'O')
            level (str): Difficulty level ('easy', 'medium', 'hard')
        """
        super().__init__(mark, name=f"AI ({level})")
        self.level = level
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    def get_move(self, board):
        """
        Get AI's move based on difficulty level.
        
        Args:
            board (Board): Current game board
            
        Returns:
            int: Selected position index (0-8)
        """
        if self.level == 'easy':
            return self._get_easy_move(board)
        elif self.level == 'medium':
            return self._get_medium_move(board)
        else:
            return self._get_hard_move(board)
    
    def _get_easy_move(self, board):
        """Get a random available move."""
        available = board.get_available_moves()
        return random.choice(available)
    
    def _get_medium_move(self, board):
        """
        Get move with basic strategy.
        
        Strategy:
        1. Win if possible
        2. Block opponent's winning move
        3. Take center if available
        4. Take random available position
        """
        available = board.get_available_moves()
        
        # Try to win
        for pos in available:
            test_board = board.copy()
            test_board.make_move(pos, self.mark)
            if test_board.check_winner() == self.mark:
                return pos
        
        # Block opponent's win (opponent is X if AI is O, or vice versa)
        opponent = 'X' if self.mark == 'O' else 'O'
        for pos in available:
            test_board = board.copy()
            test_board.make_move(pos, opponent)
            if test_board.check_winner() == opponent:
                return pos
        
        # Take center if available
        if 4 in available:
            return 4
        
        # Take random corner or side
        return random.choice(available)
    
    def _get_hard_move(self, board):
        """
        Get move using Minimax algorithm (unbeatable).
        
        The Minimax algorithm recursively evaluates all possible game states
        to find the optimal move. It assumes both players play optimally.
        
        How Minimax works:
        1. For each possible move, simulate the game
        2. Recursively evaluate all outcomes from that move
        3. If it's AI's turn, maximize the score (favor AI wins)
        4. If it's opponent's turn, minimize the score (favor opponent losses)
        5. Return the move with the best guaranteed outcome
        
        Returns:
            int: Optimal position index (0-8)
        """
        # Determine if AI is X or O
        ai_mark = self.mark
        opponent_mark = 'X' if ai_mark == 'O' else 'O'
        
        best_score = float('-inf')
        best_move = None
        
        for move in board.get_available_moves():
            # Make the move
            test_board = board.copy()
            test_board.make_move(move, ai_mark)
            
            # Get the minimax value for opponent's response
            score = self._minimax(test_board, 0, False, ai_mark, opponent_mark)
            
            # Update best move
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _minimax(self, board, depth, is_maximizing, ai_mark, opponent_mark):
        """
        Minimax algorithm with Alpha-Beta pruning optimization.
        
        Args:
            board (Board): Current game board state
            depth (int): Current depth in game tree
            is_maximizing (bool): True if it's AI's turn, False if opponent's
            ai_mark (str): AI's mark
            opponent_mark (str): Opponent's mark
            
        Returns:
            int: Score for the current board state
                   +10 if AI wins, -10 if opponent wins, 0 for draw
        """
        # Terminal state evaluation
        winner = board.check_winner()
        
        if winner == ai_mark:
            return 10 - depth  # Prefer faster wins
        elif winner == opponent_mark:
            return depth - 10  # Prefer slower losses
        elif winner == 'draw':
            return 0
        
        # Recursive case
        if is_maximizing:
            # AI's turn - maximize score
            best_score = float('-inf')
            for move in board.get_available_moves():
                board.make_move(move, ai_mark)
                score = self._minimax(board, depth + 1, False, ai_mark, opponent_mark)
                board.undo_move(move)
                best_score = max(score, best_score)
            return best_score
        else:
            # Opponent's turn - minimize score
            best_score = float('inf')
            for move in board.get_available_moves():
                board.make_move(move, opponent_mark)
                score = self._minimax(board, depth + 1, True, ai_mark, opponent_mark)
                board.undo_move(move)
                best_score = min(score, best_score)
            return best_score