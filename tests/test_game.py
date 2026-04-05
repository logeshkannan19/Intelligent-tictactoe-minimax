"""Tests for game logic (Board, Rules, Player)."""

import pytest
from src.game.board import Board
from src.game.rules import GameRules, GameState
from src.game.player import HumanPlayer, AIPlayer


class TestBoard:
    """Test cases for Board class."""
    
    def test_initial_board_empty(self):
        """Board should start empty."""
        board = Board()
        assert all(cell == "" for cell in board.cells)
    
    def test_make_valid_move(self):
        """Valid move should be placed on board."""
        board = Board()
        assert board.make_move(0, "X")
        assert board.cells[0] == "X"
    
    def test_make_invalid_position(self):
        """Invalid position should fail."""
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
        assert board.cells[0] == ""
    
    def test_get_available_moves_full_board(self):
        """Empty board should have all 9 positions available."""
        board = Board()
        available = board.get_available_moves()
        assert set(available) == set(range(9))
    
    def test_get_available_moves_partial(self):
        """Should return only empty positions."""
        board = Board()
        board.make_move(0, "X")
        board.make_move(4, "O")
        available = board.get_available_moves()
        assert 0 not in available
        assert 4 not in available
        assert 1 in available
    
    def test_is_full(self):
        """Should detect full board."""
        board = Board()
        board._cells = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        assert board.is_full() is True
    
    def test_is_not_full(self):
        """Should detect non-full board."""
        board = Board()
        assert board.is_full() is False
    
    def test_copy(self):
        """Copy should create independent board."""
        board = Board()
        board.make_move(0, "X")
        copy = board.copy()
        copy.make_move(1, "O")
        assert board.cells[1] == ""


class TestGameRules:
    """Test cases for GameRules class."""
    
    def test_check_winner_row(self):
        """Should detect row win."""
        board = Board()
        board._cells = ["X", "X", "X", "", "", "", "", "", ""]
        assert GameRules.check_winner(board) == "X"
    
    def test_check_winner_column(self):
        """Should detect column win."""
        board = Board()
        board._cells = ["X", "", "", "X", "", "", "X", "", ""]
        assert GameRules.check_winner(board) == "X"
    
    def test_check_winner_diagonal(self):
        """Should detect diagonal win."""
        board = Board()
        board._cells = ["X", "", "", "", "X", "", "", "", "X"]
        assert GameRules.check_winner(board) == "X"
    
    def test_check_winner_anti_diagonal(self):
        """Should detect anti-diagonal win."""
        board = Board()
        board._cells = ["", "", "X", "", "X", "", "X", "", ""]
        assert GameRules.check_winner(board) == "X"
    
    def test_check_no_winner(self):
        """Should return None when no winner."""
        board = Board()
        board._cells = ["X", "", "O", "", "X", "", "", "", ""]
        assert GameRules.check_winner(board) is None
    
    def test_is_draw(self):
        """Should detect draw."""
        board = Board()
        board._cells = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        assert GameRules.is_draw(board) is True
    
    def test_is_not_draw_when_winner(self):
        """Should not detect draw when there's a winner."""
        board = Board()
        board._cells = ["X", "X", "X", "O", "O", "", "", "", ""]
        assert GameRules.is_draw(board) is False
    
    def test_check_game_state_win(self):
        """Should return WIN state with winner."""
        board = Board()
        board._cells = ["X", "X", "X", "", "", "", "", "", ""]
        state, winner = GameRules.check_game_state(board)
        assert state == GameState.WIN
        assert winner == "X"
    
    def test_check_game_state_draw(self):
        """Should return DRAW state."""
        board = Board()
        board._cells = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        state, winner = GameRules.check_game_state(board)
        assert state == GameState.DRAW
        assert winner is None
    
    def test_check_game_state_in_progress(self):
        """Should return IN_PROGRESS state."""
        board = Board()
        state, winner = GameRules.check_game_state(board)
        assert state == GameState.IN_PROGRESS
        assert winner is None
    
    def test_get_winning_line(self):
        """Should return winning line positions."""
        board = Board()
        board._cells = ["X", "X", "X", "", "", "", "", "", ""]
        line = GameRules.get_winning_line(board)
        assert line == [0, 1, 2]


class TestHumanPlayer:
    """Test cases for HumanPlayer class."""
    
    def test_initialization(self):
        """Should initialize with correct mark."""
        player = HumanPlayer("X")
        assert player.mark == "X"
        assert player.name == "Player X"
    
    def test_stats_initialization(self):
        """Should initialize stats to zero."""
        player = HumanPlayer("X")
        assert player.wins == 0
        assert player.losses == 0
        assert player.draws == 0
    
    def test_add_win(self):
        """Should increment wins."""
        player = HumanPlayer("X")
        player.add_win()
        assert player.wins == 1
    
    def test_add_loss(self):
        """Should increment losses."""
        player = HumanPlayer("X")
        player.add_loss()
        assert player.losses == 1
    
    def test_add_draw(self):
        """Should increment draws."""
        player = HumanPlayer("X")
        player.add_draw()
        assert player.draws == 1


class TestAIPlayer:
    """Test cases for AIPlayer class."""
    
    def test_initialization_hard(self):
        """Should initialize with hard difficulty."""
        ai = AIPlayer("O", "hard")
        assert ai.mark == "O"
        assert ai.level.value == "hard"
    
    def test_initialization_easy(self):
        """Should initialize with easy difficulty."""
        ai = AIPlayer("O", "easy")
        assert ai.level.value == "easy"
    
    def test_get_move_easy(self):
        """Easy AI should return valid move."""
        board = Board()
        ai = AIPlayer("O", "easy")
        move = ai.get_move(board)
        assert move in range(9)
    
    def test_get_move_medium(self):
        """Medium AI should return valid move."""
        board = Board()
        ai = AIPlayer("O", "medium")
        move = ai.get_move(board)
        assert move in range(9)
    
    def test_get_move_hard(self):
        """Hard AI should return valid move."""
        board = Board()
        ai = AIPlayer("O", "hard")
        move = ai.get_move(board)
        assert move in range(9)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])