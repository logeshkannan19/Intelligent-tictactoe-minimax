"""
Board Module - Manages the Tic Tac Toe game board.

This module handles all board-related operations including:
- Initializing an empty 3x3 board
- Making and undoing moves
- Checking board state

Author: Logesh Kannan
"""

from typing import List, Optional


class Board:
    """
    Represents a Tic Tac Toe game board.
    
    The board is a 3x3 grid stored as a flat list of 9 positions.
    Positions are numbered 0-8 internally, corresponding to 1-9 for user input.
    
    Attributes:
        SIZE (int): Size of the board (3x3)
        WINNING_LINES (List[List[int]]): All possible winning combinations
    
    Example:
        >>> board = Board()
        >>> board.make_move(4, 'X')  # Place X in center
        >>> board.display()
    """
    
    SIZE = 3
    WINNING_LINES = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal top-left to bottom-right
        [2, 4, 6],  # Diagonal top-right to bottom-left
    ]
    
    def __init__(self) -> None:
        """Initialize an empty 3x3 board."""
        self._cells: List[str] = ["" for _ in range(9)]
    
    @property
    def cells(self) -> List[str]:
        """Return a copy of the board cells."""
        return self._cells.copy()
    
    def make_move(self, position: int, mark: str) -> bool:
        """
        Place a mark at the specified position.
        
        Args:
            position: Position index (0-8)
            mark: Player's mark ('X' or 'O')
            
        Returns:
            True if move was successful, False if position is invalid or occupied
        """
        if not self.is_valid_position(position):
            return False
        if self._cells[position] != "":
            return False
        
        self._cells[position] = mark
        return True
    
    def undo_move(self, position: int) -> bool:
        """
        Remove a mark from the specified position.
        
        Args:
            position: Position index (0-8)
            
        Returns:
            True if move was undone, False if position is invalid
        """
        if not self.is_valid_position(position):
            return False
        self._cells[position] = ""
        return True
    
    def is_valid_position(self, position: int) -> bool:
        """Check if position is within valid range (0-8)."""
        return 0 <= position < 9
    
    def is_position_empty(self, position: int) -> bool:
        """Check if a position is empty."""
        return self._cells[position] == ""
    
    def get_available_moves(self) -> List[int]:
        """
        Get list of all empty positions.
        
        Returns:
            List of available position indices (0-8)
        """
        return [i for i in range(9) if self._cells[i] == ""]
    
    def is_full(self) -> bool:
        """Check if board is completely filled."""
        return "" not in self._cells
    
    def copy(self) -> "Board":
        """
        Create a deep copy of the board.
        
        Returns:
            New Board instance with same state
        """
        new_board = Board()
        new_board._cells = self._cells.copy()
        return new_board
    
    def __repr__(self) -> str:
        """Return string representation of the board."""
        return f"Board(cells={self._cells})"