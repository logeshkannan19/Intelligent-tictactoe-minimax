"""Tests for Tic Tac Toe package."""

import pytest
from tic_tac_toe import Board, HumanPlayer, AIPlayer, Game


class TestBoard:
    """Test cases for Board class."""

    def test_initial_board_empty(self):
        """Board should start empty."""
        board = Board()
        assert all(cell == "" for cell in board.board)

    def test_make_valid_move(self):
        """Valid move should be placed on board."""
        board = Board()
        assert board.make_move(0, "X")
        assert board.board[0] == "X"

    def test_make_invalid_move(self):
        """Invalid move (out of bounds) should fail."""
        board = Board()
        assert not board.make_move(9, "X")
        assert not board.make_move(-1, "X")

    def test_make_duplicate_move(self):
        """Duplicate move should fail."""
        board = Board()
        board.make_move(0, "X")
        assert not board.make_move(0, "O")

    def test_undo_move(self):
        """Undo move should clear position."""
        board = Board()
        board.make_move(0, "X")
        board.undo_move(0)
        assert board.board[0] == ""

    def test_get_available_moves(self):
        """Should return all empty positions."""
        board = Board()
        available = board.get_available_moves()
        assert set(available) == set(range(9))

    def test_get_available_moves_after_moves(self):
        """Should return only empty positions."""
        board = Board()
        board.make_move(0, "X")
        board.make_move(4, "O")
        available = board.get_available_moves()
        assert 0 not in available
        assert 4 not in available
        assert 1 in available

    def test_check_winner_row(self):
        """Should detect row win."""
        board = Board()
        board.board = ["X", "X", "X", "", "", "", "", "", ""]
        assert board.check_winner() == "X"

    def test_check_winner_column(self):
        """Should detect column win."""
        board = Board()
        board.board = ["X", "", "", "X", "", "", "X", "", ""]
        assert board.check_winner() == "X"

    def test_check_winner_diagonal(self):
        """Should detect diagonal win."""
        board = Board()
        board.board = ["X", "", "", "", "X", "", "", "", "X"]
        assert board.check_winner() == "X"

    def test_check_draw(self):
        """Should detect draw when board is full with no winner."""
        board = Board()
        board.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        assert board.check_winner() == "draw"

    def test_no_winner_yet(self):
        """Should return None when game is not over."""
        board = Board()
        board.board = ["X", "", "O", "", "X", "", "", "", ""]
        assert board.check_winner() is None

    def test_is_full(self):
        """Should detect full board."""
        board = Board()
        board.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        assert board.is_full() is True

    def test_is_not_full(self):
        """Should detect non-full board."""
        board = Board()
        assert board.is_full() is False


class TestAIPlayer:
    """Test cases for AIPlayer class."""

    def test_ai_easy_move(self):
        """Easy AI should return valid move."""
        board = Board()
        ai = AIPlayer("O", level="easy")
        move = ai.get_move(board)
        assert move in range(9)

    def test_ai_medium_blocks_win(self):
        """Medium AI should block opponent's winning move."""
        board = Board()
        board.board = ["X", "X", "", "", "", "", "", "", ""]
        ai = AIPlayer("O", level="medium")
        move = ai.get_move(board)
        assert move == 2

    def test_ai_medium_takes_center(self):
        """Medium AI should take center when available."""
        board = Board()
        available = board.get_available_moves()
        ai = AIPlayer("O", level="medium")
        move = ai.get_move(board)
        assert 4 in available
        assert move == 4

    def test_ai_hard_never_loses(self):
        """Hard AI should never lose (Minimax)."""
        board = Board()
        ai = AIPlayer("O", level="hard")
        move = ai.get_move(board)
        assert move in range(9)


class TestGame:
    """Test cases for Game class."""

    def test_game_initialization(self):
        """Game should initialize with correct players."""
        p1 = HumanPlayer("X")
        p2 = HumanPlayer("O")
        game = Game(p1, p2)
        assert game.player1.mark == "X"
        assert game.player2.mark == "O"
        assert game.current_player == p1

    def test_switch_player(self):
        """Switch player should alternate current player."""
        p1 = HumanPlayer("X")
        p2 = HumanPlayer("O")
        game = Game(p1, p2)
        assert game.current_player == p1
        game.switch_player()
        assert game.current_player == p2
        game.switch_player()
        assert game.current_player == p1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])