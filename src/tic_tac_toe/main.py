"""
Tic Tac Toe - Command-line interface.

This module provides the main entry point for the Tic Tac Toe game,
supporting both Player vs Player and Player vs AI modes with various
difficulty levels.
"""

import sys
from tic_tac_toe import Game, HumanPlayer, AIPlayer


def print_welcome() -> None:
    """Display welcome message and game instructions."""
    print("\n" + "=" * 50)
    print("         TIC TAC TOE - Python Edition")
    print("=" * 50)
    print("\nWelcome to Tic Tac Toe!")
    print("\nGame Rules:")
    print("  - The board is a 3x3 grid")
    print("  - Players take turns placing their mark (X or O)")
    print("  - First to get 3 in a row wins!")
    print("\nBoard positions are numbered 1-9:")
    print("  1 | 2 | 3")
    print("  ---+---+---")
    print("  4 | 5 | 6")
    print("  ---+---+---")
    print("  7 | 8 | 9")
    print("\n" + "=" * 50)


def get_game_mode() -> str:
    """Prompt user to select game mode."""
    print("\nSelect Game Mode:")
    print("  1. Player vs Player")
    print("  2. Player vs AI")
    print("  3. GUI Version (Tkinter)")
    print("  4. Exit")

    while True:
        choice = input("\nEnter choice (1-4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


def get_difficulty() -> str:
    """Prompt user to select AI difficulty level."""
    print("\nSelect Difficulty Level:")
    print("  1. Easy   (Random moves)")
    print("  2. Medium (Basic strategy)")
    print("  3. Hard   (Minimax - Unbeatable!)")

    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        if choice in {"1", "2", "3"}:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")


def main() -> None:
    """Main entry point for the Tic Tac Toe CLI game."""
    print_welcome()

    while True:
        mode = get_game_mode()

        if mode == "4":
            print("\nThanks for playing! Goodbye!\n")
            sys.exit(0)

        if mode == "3":
            print("\nLaunching GUI version...")
            try:
                from tic_tac_toe.gui import main as gui_main
                gui_main()
            except Exception as e:
                print(f"Error launching GUI: {e}")
            continue

        if mode == "1":
            player1 = HumanPlayer("X")
            player2 = HumanPlayer("O")
            game = Game(player1, player2)
        else:
            difficulty = get_difficulty()
            player1 = HumanPlayer("X")
            difficulty_map = {"1": "easy", "2": "medium", "3": "hard"}
            player2 = AIPlayer("O", level=difficulty_map[difficulty])
            game = Game(player1, player2)

        game.play()

        print("\n" + "=" * 50)
        while True:
            response = input("Play again? (y/n): ").strip().lower()
            if response in {"y", "yes"}:
                break
            if response in {"n", "no"}:
                print("\nThanks for playing! Goodbye!\n")
                sys.exit(0)
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()