"""Intelligent TicTacToe - Main Package."""

__version__ = "1.0.0"
__author__ = "Logesh Kannan"
__license__ = "MIT"

from src.game.board import Board
from src.game.player import Player, HumanPlayer, AIPlayer
from src.game.rules import GameRules
from src.ai.minimax import MinimaxAI
from src.ai.difficulty import Difficulty

__all__ = [
    "Board",
    "Player",
    "HumanPlayer",
    "AIPlayer",
    "GameRules",
    "MinimaxAI",
    "Difficulty",
]