"""
Display Module - Handles CLI board display and formatting.

This module provides functions to display the game board and
status messages in the terminal.

Author: Logesh Kannan
"""

from typing import List
from src.game.board import Board
from src.game.player import Player


class BoardDisplay:
    """
    Handles the visual display of the Tic Tac Toe board in CLI.
    
    Provides methods to display the board with optional highlighting
    and position numbers.
    
    Example:
        >>> display = BoardDisplay()
        >>> display.show_board(board)
    """
    
    # Display characters
    HORIZONTAL_LINE = "───┼───┼───"
    VERTICAL_LINE = "│"
    
    @staticmethod
    def show_board(board: Board, highlight: List[int] = None) -> None:
        """
        Display the current board state.
        
        Args:
            board: The game board to display
            highlight: Optional list of positions to highlight
        """
        print()
        for row in range(Board.SIZE):
            row_cells = []
            for col in range(Board.SIZE):
                pos = row * Board.SIZE + col
                cell = board.cells[pos]
                
                # Show position number if cell is empty
                if cell == "":
                    display_cell = str(pos + 1)
                else:
                    display_cell = cell
                
                # Apply highlighting if specified
                if highlight and pos in highlight:
                    display_cell = f"[{display_cell}]"
                else:
                    display_cell = f" {display_cell} "
                
                row_cells.append(display_cell)
            
            print(BoardDisplay.VERTICAL_LINE.join(row_cells))
            
            if row < Board.SIZE - 1:
                print(BoardDisplay.HORIZONTAL_LINE)
        print()
    
    @staticmethod
    def show_numbered_board() -> None:
        """Display a numbered board reference for user guidance."""
        print("\n  Board positions:")
        print("  1 │ 2 │ 3")
        print("  ───┼───┼───")
        print("  4 │ 5 │ 6")
        print("  ───┼───┼───")
        print("  7 │ 8 │ 9\n")
    
    @staticmethod
    def show_winning_line(board: Board) -> None:
        """Display the board with the winning line highlighted."""
        from src.game.rules import GameRules
        
        winning_line = GameRules.get_winning_line(board)
        
        if winning_line:
            BoardDisplay.show_board(board, highlight=winning_line)
            print(f"Winning line: {', '.join(str(p + 1) for p in winning_line)}")
        else:
            BoardDisplay.show_board(board)


class MessageDisplay:
    """
    Handles displaying game messages and status updates.
    
    Example:
        >>> MessageDisplay.show_welcome()
        >>> MessageDisplay.show_turn(player)
    """
    
    @staticmethod
    def show_welcome() -> None:
        """Display welcome message and game rules."""
        print("\n" + "=" * 50)
        print("       TIC TAC TOE - Minimax AI Edition")
        print("=" * 50)
        print("\nWelcome to Intelligent Tic Tac Toe!")
        print("\nGame Rules:")
        print("  • The board is a 3x3 grid")
        print("  • Players take turns placing their mark (X or O)")
        print("  • First to get 3 in a row wins!")
    
    @staticmethod
    def show_menu() -> None:
        """Display the main menu options."""
        print("\n" + "-" * 40)
        print("Select Game Mode:")
        print("  1. Player vs Player")
        print("  2. Player vs AI")
        print("  3. Exit")
        print("-" * 40)
    
    @staticmethod
    def show_difficulty_menu() -> None:
        """Display difficulty selection menu."""
        print("\n" + "-" * 40)
        print("Select Difficulty Level:")
        print("  1. Easy   (Random moves)")
        print("  2. Medium (Basic strategy)")
        print("  3. Hard   (Minimax - Unbeatable!)")
        print("-" * 40)
    
    @staticmethod
    def show_turn(player: Player) -> None:
        """Display whose turn it is."""
        print(f"\n{player.name}'s turn ({player.mark})")
    
    @staticmethod
    def show_game_over(winner: str = None) -> None:
        """Display game over message."""
        print("\n" + "=" * 50)
        if winner:
            print(f"       {winner} WINS!")
        else:
            print("       IT'S A DRAW!")
        print("=" * 50)
    
    @staticmethod
    def show_stats(players: List[Player]) -> None:
        """Display player statistics."""
        print("\n" + "-" * 40)
        print("        GAME STATISTICS")
        print("-" * 40)
        for player in players:
            print(f"  {player.name}: {player.wins}W {player.losses}L {player.draws}D")
        print("-" * 40)
    
    @staticmethod
    def show_invalid_input(message: str) -> None:
        """Display error message for invalid input."""
        print(f"\n⚠️  {message}")
    
    @staticmethod
    def show_goodbye() -> None:
        """Display goodbye message."""
        print("\nThanks for playing! Goodbye!\n")