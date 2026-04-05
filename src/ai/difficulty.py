"""
Difficulty Module - Defines AI difficulty levels.

This module provides an enum for difficulty levels that can be
used to configure the AI player's behavior.

Author: Logesh Kannan
"""

from enum import Enum


class Difficulty(Enum):
    """
    Represents the difficulty level for the AI opponent.
    
    Attributes:
        EASY: Random moves, no strategy
        MEDIUM: Basic blocking and winning logic
        HARD: Minimax algorithm, unbeatable
    
    Example:
        >>> difficulty = Difficulty.HARD
        >>> print(difficulty.value)  # 'hard'
    """
    
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    
    @classmethod
    def from_string(cls, level: str) -> "Difficulty":
        """
        Create a Difficulty enum from a string.
        
        Args:
            level: String representation of difficulty ('easy', 'medium', 'hard')
            
        Returns:
            Corresponding Difficulty enum value
            
        Raises:
            ValueError: If the level string is not valid
        """
        level = level.lower().strip()
        
        for diff in cls:
            if diff.value == level:
                return diff
        
        raise ValueError(f"Invalid difficulty level: {level}. Must be 'easy', 'medium', or 'hard'.")
    
    def __str__(self) -> str:
        """Return string representation of difficulty."""
        return self.value.capitalize()