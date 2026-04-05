"""
Board Module - Manages the Tic Tac Toe game board.

This module handles all board-related operations including:
- Initializing an empty 3x3 board
- Displaying the board
- Making moves
- Checking for win/draw conditions
- Getting available moves

Author: AI Assistant
"""

class Board:
    """
    Represents a Tic Tac Toe game board.
    
    The board is a 3x3 grid stored as a flat list of 9 positions.
    Positions are numbered 0-8 internally, corresponding to 1-9 for user input.
    
    Attributes:
        board (list): List of 9 elements, initially empty strings
        winning_lines (list): All possible winning combinations
    """
    
    def __init__(self):
        """Initialize an empty 3x3 board."""
        self.board = ['' for _ in range(9)]
        self.winning_lines = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal top-left to bottom-right
            [2, 4, 6],  # Diagonal top-right to bottom-left
        ]
    
    def display(self):
        """
        Display the current board state in the terminal.
        
        Shows the board with positions and marks (X or O).
        Empty positions show their position number (1-9).
        """
        print("\n")
        for i in range(3):
            row = []
            for j in range(3):
                pos = i * 3 + j
                mark = self.board[pos] if self.board[pos] else str(pos + 1)
                row.append(f" {mark} ")
            print("│".join(row))
            if i < 2:
                print("─" * 3 + "┼" + "─" * 3 + "┼" + "─" * 3)
        print("\n")
    
    def display_numbered(self):
        """
        Display a numbered board reference.
        
        Shows positions 1-9 for user reference when entering moves.
        """
        print("\n  Board positions:")
        print("  1 | 2 | 3")
        print("  ───┼───┼───")
        print("  4 | 5 | 6")
        print("  ───┼───┼───")
        print("  7 | 8 | 9\n")
    
    def make_move(self, position, mark):
        """
        Place a mark at the specified position.
        
        Args:
            position (int): Position index (0-8)
            mark (str): Player's mark ('X' or 'O')
            
        Returns:
            bool: True if move was successful, False if position occupied
        """
        if self.is_valid_position(position):
            if self.board[position] == '':
                self.board[position] = mark
                return True
        return False
    
    def undo_move(self, position):
        """
        Remove a mark from the specified position.
        
        Args:
            position (int): Position index (0-8)
        """
        if 0 <= position < 9:
            self.board[position] = ''
    
    def is_valid_position(self, position):
        """Check if position is within valid range (0-8)."""
        return 0 <= position < 9
    
    def is_position_empty(self, position):
        """Check if a position is empty."""
        return self.board[position] == ''
    
    def get_available_moves(self):
        """
        Get list of all empty positions.
        
        Returns:
            list: List of available position indices (0-8)
        """
        return [i for i in range(9) if self.board[i] == '']
    
    def is_full(self):
        """Check if board is completely filled."""
        return '' not in self.board
    
    def check_winner(self):
        """
        Check if there is a winner or if the game is over.
        
        Returns:
            str: 'X' or 'O' if there's a winner, 'draw' if board is full
                  with no winner, None if game is still in progress
        """
        for line in self.winning_lines:
            if self.board[line[0]] and self.board[line[0]] == self.board[line[1]] == self.board[line[2]]:
                return self.board[line[0]]
        
        if self.is_full():
            return 'draw'
        
        return None
    
    def is_game_over(self):
        """Check if the game has ended (win or draw)."""
        return self.check_winner() is not None
    
    def copy(self):
        """
        Create a deep copy of the board.
        
        Returns:
            Board: New Board instance with same state
        """
        new_board = Board()
        new_board.board = self.board.copy()
        return new_board
    
    def __str__(self):
        """String representation of the board."""
        return str(self.board)
    
    def __repr__(self):
        """Debug representation of the board."""
        return f"Board({self.board})"