"""
Minimax Module - Implements the Minimax algorithm for Tic Tac Toe AI.

The Minimax algorithm is a recursive decision-making algorithm used in
two-player zero-sum games. It works by simulating all possible moves
and choosing the one that minimizes the maximum loss.

Author: Logesh Kannan
"""

from typing import Optional
from src.game.board import Board
from src.game.rules import GameRules


class MinimaxAI:
    """
    AI player using the Minimax algorithm for optimal decision making.
    
    The Minimax algorithm explores the entire game tree to find the optimal
    move. It assigns scores to terminal states:
    - +10 if AI wins
    - -10 if opponent wins
    - 0 for draw
    
    The AI always chooses the move that maximizes its minimum possible score,
    hence the name "minimax".
    
    Attributes:
        ai_mark: The AI player's mark ('X' or 'O')
        opponent_mark: The opponent's mark
    
    Example:
        >>> ai = MinimaxAI('O')
        >>> best_move = ai.get_best_move(board)
    """
    
    # Score constants
    WIN_SCORE = 10
    LOSE_SCORE = -10
    DRAW_SCORE = 0
    
    def __init__(self, ai_mark: str) -> None:
        """
        Initialize the Minimax AI.
        
        Args:
            ai_mark: The AI's mark ('X' or 'O')
        """
        self.ai_mark = ai_mark
        self.opponent_mark = 'X' if ai_mark == 'O' else 'O'
    
    def get_best_move(self, board: Board) -> int:
        """
        Get the best move using the Minimax algorithm.
        
        This method explores all possible moves and evaluates them using
        the minimax algorithm to find the optimal move.
        
        Args:
            board: Current game board
            
        Returns:
            The best position index (0-8) for the AI's move
        """
        best_score = float('-inf')
        best_move = None
        
        available_moves = board.get_available_moves()
        
        for move in available_moves:
            # Make the move on a copy of the board
            test_board = board.copy()
            test_board.make_move(move, self.ai_mark)
            
            # Get the minimax score for this move
            # Since we just made a move, it's now the opponent's turn (minimizing)
            score = self._minimax(test_board, depth=0, is_maximizing=False)
            
            # Update best move if this score is better
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        """
        Recursive Minimax algorithm with depth consideration.
        
        This method recursively evaluates all possible game states.
        When it's the AI's turn (is_maximizing=True), it tries to maximize
        the score. When it's the opponent's turn (is_maximizing=False),
        it tries to minimize the score.
        
        Args:
            board: Current game board state
            depth: Current depth in the game tree (used for optimization)
            is_maximizing: True if it's AI's turn, False if opponent's turn
            
        Returns:
            The score for this game state
        """
        # Check terminal states (win, lose, draw)
        winner = GameRules.check_winner(board)
        
        if winner == self.ai_mark:
            # AI wins - prefer faster wins
            return self.WIN_SCORE - depth
        elif winner == self.opponent_mark:
            # Opponent wins - prefer slower losses
            return self.LOSE_SCORE + depth
        elif board.is_full():
            # Draw
            return self.DRAW_SCORE
        
        # Recursive case - explore available moves
        if is_maximizing:
            # AI's turn - maximize score
            return self._maximize(board, depth)
        else:
            # Opponent's turn - minimize score
            return self._minimize(board, depth)
    
    def _maximize(self, board: Board, depth: int) -> int:
        """
        Maximize the score for AI's turn.
        
        Args:
            board: Current board state
            depth: Current depth
            
        Returns:
            Maximum score achievable
        """
        best_score = float('-inf')
        
        for move in board.get_available_moves():
            test_board = board.copy()
            test_board.make_move(move, self.ai_mark)
            
            score = self._minimax(test_board, depth + 1, is_maximizing=False)
            best_score = max(score, best_score)
        
        return best_score
    
    def _minimize(self, board: Board, depth: int) -> int:
        """
        Minimize the score for opponent's turn.
        
        Args:
            board: Current board state
            depth: Current depth
            
        Returns:
            Minimum score achievable
        """
        best_score = float('inf')
        
        for move in board.get_available_moves():
            test_board = board.copy()
            test_board.make_move(move, self.opponent_mark)
            
            score = self._minimax(test_board, depth + 1, is_maximizing=True)
            best_score = min(score, best_score)
        
        return best_score
    
    def evaluate_position(self, board: Board) -> int:
        """
        Evaluate the current board position for the AI.
        
        Useful for debugging and understanding the AI's perspective.
        
        Args:
            board: Current game board
            
        Returns:
            Score: positive if AI is winning, negative if losing, 0 if neutral
        """
        winner = GameRules.check_winner(board)
        
        if winner == self.ai_mark:
            return self.WIN_SCORE
        elif winner == self.opponent_mark:
            return self.LOSE_SCORE
        elif board.is_full():
            return self.DRAW_SCORE
        
        # For non-terminal states, evaluate based on potential
        return self._evaluate_partial_board(board)
    
    def _evaluate_partial_board(self, board: Board) -> int:
        """
        Evaluate a non-terminal board state.
        
        Gives a rough score based on potential winning lines.
        
        Args:
            board: Current game board
            
        Returns:
            Rough score indicating advantage
        """
        score = 0
        
        for line in Board.WINNING_LINES:
            marks = [board.cells[pos] for pos in line]
            ai_count = marks.count(self.ai_mark)
            opp_count = marks.count(self.opponent_mark)
            empty_count = marks.count("")
            
            # If no opponent marks in this line, it's promising for AI
            if opp_count == 0:
                if ai_count == 2 and empty_count == 1:
                    score += 3  # Almost winning
                elif ai_count == 1 and empty_count == 2:
                    score += 1  # Potential
            
            # If no AI marks in this line, it's dangerous
            if ai_count == 0:
                if opp_count == 2 and empty_count == 1:
                    score -= 3  # Must block
                elif opp_count == 1 and empty_count == 2:
                    score -= 1  # Opponent potential
        
        return score