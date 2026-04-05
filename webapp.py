"""
Web App - Streamlit-based Tic Tac Toe

A simple web interface for playing Tic Tac Toe against the AI.

To run: streamlit run webapp.py
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
from game.board import Board
from game.rules import GameRules
from ai.minimax import MinimaxAI
import random

# Page config
st.set_page_config(page_title="Tic Tac Toe AI", page_icon="🎮")

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = Board()
if 'game_active' not in st.session_state:
    st.session_state.game_active = True
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = "hard"
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'player_mark' not in st.session_state:
    st.session_state.player_mark = "X"
if 'ai_mark' not in st.session_state:
    st.session_state.ai_mark = "O"


def reset_game():
    """Reset the game state."""
    st.session_state.board = Board()
    st.session_state.game_active = True
    st.session_state.winner = None


def get_ai_move():
    """Get AI move based on difficulty."""
    board = st.session_state.board
    ai_mark = st.session_state.ai_mark
    difficulty = st.session_state.difficulty
    
    if difficulty == "easy":
        available = board.get_available_moves()
        return random.choice(available) if available else None
    elif difficulty == "medium":
        available = board.get_available_moves()
        # Try to win
        for pos in available:
            test_board = board.copy()
            test_board.make_move(pos, ai_mark)
            if GameRules.check_winner(test_board) == ai_mark:
                return pos
        # Block opponent
        player_mark = st.session_state.player_mark
        for pos in available:
            test_board = board.copy()
            test_board.make_move(pos, player_mark)
            if GameRules.check_winner(test_board) == player_mark:
                return pos
        # Take center
        if 4 in available:
            return 4
        return random.choice(available)
    else:  # hard
        ai = MinimaxAI(ai_mark)
        return ai.get_best_move(board)


# Title
st.title("🎮 Tic Tac Toe - AI Challenge")
st.markdown("---")

# Difficulty selector
col1, col2 = st.columns([1, 2])
with col1:
    st.session_state.difficulty = st.select_slider(
        "Difficulty",
        options=["easy", "medium", "hard"],
        value=st.session_state.difficulty,
        format_func=lambda x: x.capitalize()
    )
with col2:
    if st.button("🔄 New Game", use_container_width=True):
        reset_game()

st.markdown("---")

# Display board
def render_board():
    """Render the game board."""
    board = st.session_state.board
    cells = board.cells
    
    # Create 3x3 grid
    cols = st.columns(3)
    for i in range(9):
        row, col = i // 3, i % 3
        with cols[col]:
            # Determine button style
            if cells[i]:
                # Occupied cell
                color = "🔴" if cells[i] == "X" else "🔵"
                st.markdown(f"<h1 style='text-align: center; font-size: 48px;'>{color} {cells[i]}</h1>", unsafe_allow_html=True)
            else:
                # Empty cell - clickable
                if st.session_state.game_active:
                    if st.button(f"　　{i+1}　　", key=f"cell_{i}", use_container_width=True):
                        if board.is_position_empty(i):
                            board.make_move(i, st.session_state.player_mark)
                            # Check for player win
                            if GameRules.check_winner(board):
                                st.session_state.winner = st.session_state.player_mark
                                st.session_state.game_active = False
                            elif board.is_full():
                                st.session_state.winner = "draw"
                                st.session_state.game_active = False
                            else:
                                # AI turn
                                ai_move = get_ai_move()
                                if ai_move is not None:
                                    board.make_move(ai_move, st.session_state.ai_mark)
                                    if GameRules.check_winner(board):
                                        st.session_state.winner = st.session_state.ai_mark
                                        st.session_state.game_active = False
                                    elif board.is_full():
                                        st.session_state.winner = "draw"
                                        st.session_state.game_active = False
                                st.rerun()

render_board()

# Game status
st.markdown("---")
if st.session_state.winner:
    if st.session_state.winner == "draw":
        st.error("🤝 It's a Draw!")
    elif st.session_state.winner == st.session_state.player_mark:
        st.success("🎉 You Win!")
    else:
        st.error("🤖 AI Wins!")
else:
    st.info(f"Your turn: {st.session_state.player_mark}")

# Instructions
st.markdown("---")
with st.expander("ℹ️ How to Play"):
    st.markdown("""
    1. Select difficulty level (Easy/Medium/Hard)
    2. Click on an empty cell to place your mark (X)
    3. The AI will respond with its move (O)
    4. Get 3 in a row to win!
    
    **Difficulty Levels:**
    - **Easy**: Random moves
    - **Medium**: Blocks and takes wins
    - **Hard**: Unbeatable Minimax AI
    """)