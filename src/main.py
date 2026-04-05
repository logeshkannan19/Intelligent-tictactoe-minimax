"""
Main Module - Entry point for the Tic Tac Toe game.

This module provides the main game loop and handles user interaction.
Run this module to start the game.

Usage:
    python -m src.main

Author: Logesh Kannan
"""

import sys
from src.game.board import Board
from src.game.player import HumanPlayer, AIPlayer
from src.game.rules import GameRules, GameState
from src.utils.display import BoardDisplay, MessageDisplay
from src.utils.helpers import get_valid_input


class Game:
    """
    Main game controller that manages the game loop.
    
    Handles turn management, game state checking, and displaying results.
    
    Attributes:
        player1: First player (X)
        player2: Second player (O)
        current_player: Player whose turn it is
    
    Example:
        >>> game = Game(HumanPlayer('X'), AIPlayer('O', 'hard'))
        >>> game.play()
    """
    
    def __init__(self, player1, player2):
        """
        Initialize a new game.
        
        Args:
            player1: First player (X)
            player2: Second player (O)
        """
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
    
    def switch_player(self) -> None:
        """Switch the current player to the other player."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    def play(self) -> None:
        """
        Run the main game loop.
        
        Continues until a player wins or the game is a draw.
        """
        print("\n" + "=" * 50)
        print("           NEW GAME STARTED!")
        print("=" * 50)
        
        # Show board positions reference
        BoardDisplay.show_numbered_board()
        
        # Main game loop
        while not GameRules.is_game_over(self.board):
            # Display current board state
            BoardDisplay.show_board(self.board)
            
            # Display turn information
            MessageDisplay.show_turn(self.current_player)
            
            # Get current player's move
            position = self.current_player.get_move(self.board)
            
            # Make the move
            self.board.make_move(position, self.current_player.mark)
            
            # Switch to other player for next turn
            self.switch_player()
        
        # Game over - display final board and result
        BoardDisplay.show_winning_line(self.board)
        self._display_result()
    
    def _display_result(self) -> None:
        """Display the game result and update scores."""
        state, winner = GameRules.check_game_state(self.board)
        
        if state == GameState.DRAW:
            MessageDisplay.show_game_over()
            self.player1.add_draw()
            self.player2.add_draw()
            
        elif state == GameState.WIN:
            MessageDisplay.show_game_over(winner)
            
            if winner == self.player1.mark:
                self.player1.add_win()
                self.player2.add_loss()
            else:
                self.player2.add_win()
                self.player1.add_loss()
        
        # Display overall score
        MessageDisplay.show_stats([self.player1, self.player2])


def get_game_mode() -> str:
    """Prompt user to select game mode."""
    MessageDisplay.show_menu()
    return get_valid_input("\nEnter choice (1-3): ", ["1", "2", "3"])


def get_difficulty() -> str:
    """Prompt user to select AI difficulty level."""
    MessageDisplay.show_difficulty_menu()
    return get_valid_input("\nEnter choice (1-3): ", ["1", "2", "3"])


def main() -> None:
    """Main entry point for the Tic Tac Toe game."""
    # Display welcome message
    MessageDisplay.show_welcome()
    
    while True:
        mode = get_game_mode()
        
        if mode == "3":
            MessageDisplay.show_goodbye()
            sys.exit(0)
        
        if mode == "1":
            # Player vs Player mode
            player1 = HumanPlayer("X")
            player2 = HumanPlayer("O")
            game = Game(player1, player2)
            
        else:
            # Player vs AI mode
            difficulty = get_difficulty()
            difficulty_map = {"1": "easy", "2": "medium", "3": "hard"}
            
            player1 = HumanPlayer("X")
            player2 = AIPlayer("O", level=difficulty_map[difficulty])
            game = Game(player1, player2)
        
        # Run the game
        game.play()
        
        # Ask to play again
        print("\n" + "=" * 50)
        if not get_valid_input("\nPlay again? (y/n): ", ["y", "n", "yes", "no"], "Enter 'y' or 'n'"):
            MessageDisplay.show_goodbye()
            sys.exit(0)


if __name__ == "__main__":
    main()