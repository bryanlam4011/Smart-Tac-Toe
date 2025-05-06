import math
from functools import lru_cache
from .game import TicTacToe

@lru_cache(maxsize=None)
def _cached_minimax(board_tuple: tuple, current_winner: str, player: str):
    """
    Classical minimax over terminal win/draw/loss,
    cached by exact board + current_winner + player to move.
    """
    # rebuild state
    state = TicTacToe()
    state.board = list(board_tuple)
    state.current_winner = current_winner

    max_player = 'O'
    other = 'X' if player == 'O' else 'O'

    # terminal: opponent has won
    if state.current_winner == other:
        return {'position': None,
                'score':  1 if other == max_player else -1}

    # draw
    moves = state.available_moves()
    if not moves:
        return {'position': None, 'score': 0}

    # choose best
    if player == max_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for move in moves:
        # simulate the move (no auto-clear)
        state.make_move(move, player, simulate=True)
        result = _cached_minimax(tuple(state.board), state.current_winner, other)

        # undo
        state.board[move] = " "
        state.current_winner = None

        score = result['score']
        if player == max_player:
            if score > best['score']:
                best = {'position': move, 'score': score}
        else:
            if score < best['score']:
                best = {'position': move, 'score': score}

    return best

def minimax(state: TicTacToe, player: str):
    return _cached_minimax(tuple(state.board), state.current_winner, player)
