"""
Helpers Module - Utility functions for the Tic Tac Toe game.

This module provides helper functions for input validation,
colored output, and other common utilities.

Author: Logesh Kannan
"""

import sys
from typing import Optional


def get_valid_input(
    prompt: str,
    valid_options: list,
    error_message: str = "Invalid input. Please try again."
) -> str:
    """
    Get and validate user input from a list of valid options.
    
    Args:
        prompt: The prompt to display to the user
        valid_options: List of valid input strings
        error_message: Error message to display for invalid input
        
    Returns:
        The validated input string
        
    Example:
        >>> choice = get_valid_input("Enter choice:", ["1", "2", "3"])
    """
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        print(f"\n⚠️  {error_message}")


def validate_position(position: str, board) -> Optional[int]:
    """
    Validate a position string and convert to board index.
    
    Args:
        position: Position string from user (1-9)
        board: Current game board
        
    Returns:
        Valid position index (0-8) or None if invalid
    """
    try:
        pos = int(position) - 1
        
        if not board.is_valid_position(pos):
            print("Invalid position. Enter a number between 1 and 9.")
            return None
        
        if not board.is_position_empty(pos):
            print("That position is already taken.")
            return None
        
        return pos
        
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        return None


def print_separator(char: str = "-", length: int = 40) -> None:
    """
    Print a separator line.
    
    Args:
        char: Character to use for the separator
        length: Length of the separator
    """
    print(char * length)


def confirm(message: str = "Continue?") -> bool:
    """
    Ask user for confirmation (y/n).
    
    Args:
        message: Confirmation message to display
        
    Returns:
        True if user confirms, False otherwise
    """
    while True:
        response = input(f"\n{message} (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            return True
        if response in ["n", "no"]:
            return False
        print("Please enter 'y' or 'n'.")


def exit_game() -> None:
    """Exit the game gracefully."""
    print("\nThanks for playing! Goodbye!\n")
    sys.exit(0)


def clear_screen() -> None:
    """Clear the terminal screen (cross-platform)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')