"""
Tic Tac Toe Package.

A complete Tic Tac Toe game with an intelligent AI opponent using
the Minimax algorithm with alpha-beta pruning optimization.

Modules:
    - board: Board management and game state
    - player: Human and AI player implementations
    - game: Main game loop and state management
    - gui: Tkinter graphical interface
    - main: Command-line interface

Example:
    >>> from tic_tac_toe import Game, HumanPlayer, AIPlayer
    >>> game = Game(HumanPlayer('X'), AIPlayer('O', level='hard'))
    >>> game.play()
"""

__version__ = "1.0.0"
__author__ = "AI Assistant"
__license__ = "MIT"

from tic_tac_toe.board import Board
from tic_tac_toe.player import Player, HumanPlayer, AIPlayer
from tic_tac_toe.game import Game

__all__ = ["Board", "Player", "HumanPlayer", "AIPlayer", "Game"]