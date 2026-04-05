"""
Game Rules Module - Handles win/draw detection and game state.

This module contains:
- GameRules: Checks for win, lose, draw conditions
- GameState: Enum for game states (IN_PROGRESS, WIN, DRAW)

Author: Logesh Kannan
"""

from enum import Enum
from typing import Optional, Tuple, List
from src.game.board import Board


class GameState(Enum):
    """Represents the current state of the game."""
    IN_PROGRESS = "in_progress"
    WIN = "win"
    DRAW = "draw"


class GameRules:
    """
    Handles game rules and win/draw detection.
    
    Provides static methods to check game state and determine winners.
    
    Example:
        >>> board = Board()
        >>> board.make_move(0, 'X')
        >>> board.make_move(1, 'X')
        >>> board.make_move(2, 'X')
        >>> state, winner = GameRules.check_game_state(board)
        >>> print(winner)  # 'X'
    """
    
    @staticmethod
    def check_winner(board: Board) -> Optional[str]:
        """
        Check if there is a winner on the board.
        
        Args:
            board: The game board
            
        Returns:
            'X' or 'O' if there's a winner, None otherwise
        """
        for line in Board.WINNING_LINES:
            if (board.cells[line[0]] and 
                board.cells[line[0]] == board.cells[line[1]] == board.cells[line[2]]):
                return board.cells[line[0]]
        return None
    
    @staticmethod
    def is_draw(board: Board) -> bool:
        """
        Check if the game is a draw.
        
        Args:
            board: The game board
            
        Returns:
            True if board is full with no winner, False otherwise
        """
        return board.is_full() and GameRules.check_winner(board) is None
    
    @staticmethod
    def is_game_over(board: Board) -> bool:
        """
        Check if the game has ended.
        
        Args:
            board: The game board
            
        Returns:
            True if game is over (win or draw), False otherwise
        """
        return GameRules.check_winner(board) is not None or board.is_full()
    
    @staticmethod
    def check_game_state(board: Board) -> Tuple[GameState, Optional[str]]:
        """
        Check the complete game state.
        
        Args:
            board: The game board
            
        Returns:
            Tuple of (GameState, winner_mark or None)
            - (GameState.WIN, 'X' or 'O') if someone won
            - (GameState.DRAW, None) if it's a draw
            - (GameState.IN_PROGRESS, None) if game is ongoing
        """
        winner = GameRules.check_winner(board)
        if winner:
            return GameState.WIN, winner
        
        if board.is_full():
            return GameState.DRAW, None
        
        return GameState.IN_PROGRESS, None
    
    @staticmethod
    def get_winning_line(board: Board) -> Optional[List[int]]:
        """
        Get the positions that form the winning line.
        
        Args:
            board: The game board
            
        Returns:
            List of 3 positions that form the winning line, or None
        """
        for line in Board.WINNING_LINES:
            if (board.cells[line[0]] and 
                board.cells[line[0]] == board.cells[line[1]] == board.cells[line[2]]):
                return line
        return None