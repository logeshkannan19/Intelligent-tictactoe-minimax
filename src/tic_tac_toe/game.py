"""
Game Module - Manages the game loop and game state.

This module handles:
- Running the main game loop
- Managing turns between players
- Checking game end conditions
- Displaying game results
- Score tracking

Author: AI Assistant
"""

from tic_tac_toe.board import Board


class Game:
    """
    Manages the overall game state and flow.
    
    Attributes:
        board (Board): The game board
        player1 (Player): First player (X)
        player2 (Player): Second player (O)
        current_player (Player): Player whose turn it is
    """
    
    def __init__(self, player1, player2):
        """
        Initialize a new game.
        
        Args:
            player1 (Player): Player using mark 'X'
            player2 (Player): Player using mark 'O'
        """
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
    
    def switch_player(self):
        """Switch the current player."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    def play(self):
        """
        Run the main game loop.
        
        Continues until a player wins or the board is full (draw).
        """
        print("\n" + "=" * 50)
        print("           NEW GAME STARTED!")
        print("=" * 50)
        
        # Show board positions reference
        self.board.display_numbered()
        
        # Main game loop
        while not self.board.is_game_over():
            # Display current board state
            self.board.display()
            
            # Display turn information
            print(f"\n{self.current_player.name}'s turn (playing as {self.current_player.mark})")
            
            # Get current player's move
            position = self.current_player.get_move(self.board)
            
            # Make the move
            self.board.make_move(position, self.current_player.mark)
            
            # Switch to other player for next turn
            self.switch_player()
        
        # Game over - display final board and result
        self.board.display()
        self._display_result()
    
    def _display_result(self):
        """
        Display the game result and update scores.
        
        Checks for winner or draw and displays appropriate message.
        """
        winner = self.board.check_winner()
        
        if winner == 'draw':
            print("\n" + "=" * 50)
            print("           IT'S A DRAW!")
            print("=" * 50)
            print("\nThe game ended in a tie. Good game!")
            
            # Update draw stats
            self.player1.draws += 1
            self.player2.draws += 1
            
        else:
            # Determine winner
            if winner == self.player1.mark:
                winner_player = self.player1
                loser_player = self.player2
            else:
                winner_player = self.player2
                loser_player = self.player1
            
            print("\n" + "=" * 50)
            print(f"      {winner_player.name} WINS!")
            print("=" * 50)
            print(f"\nCongratulations {winner_player.name}!")
            
            # Update win/loss stats
            winner_player.wins += 1
            loser_player.losses += 1
        
        # Display overall score (for AI mode)
        print("\n" + "-" * 40)
        print("        GAME STATISTICS")
        print("-" * 40)
        print(f"  {self.player1.name}: {self.player1.wins} wins, {self.player1.losses} losses, {self.player1.draws} draws")
        print(f"  {self.player2.name}: {self.player2.wins} wins, {self.player2.losses} losses, {self.player2.draws} draws")
        print("-" * 40)
    
    def reset(self):
        """Reset the game for a new round."""
        self.board = Board()
        self.current_player = self.player1