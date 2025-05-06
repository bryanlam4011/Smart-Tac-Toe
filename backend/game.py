class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_winner = None
        # separate histories for each player
        self.history = {"X": [], "O": []}

    def make_move(self, square: int, letter: str, simulate: bool = False) -> bool:
        """
        Place `letter` at `square`.
        If simulate=False and that player's history now exceeds 3,
        pop their oldest mark off the board immediately.
        """
        if self.board[square] != " ":
            return False

        self.board[square] = letter
        self.history[letter].append(square)

        # enforce max-3 live marks per player (skip during simulation)
        if not simulate and len(self.history[letter]) > 3:
            oldest = self.history[letter].pop(0)
            self.board[oldest] = " "

        # check for win
        if self.check_winner(letter):
            self.current_winner = letter

        return True

    def check_winner(self, letter: str) -> bool:
        b = self.board
        lines = [
            [0,1,2],[3,4,5],[6,7,8],   # rows
            [0,3,6],[1,4,7],[2,5,8],   # cols
            [0,4,8],[2,4,6]            # diags
        ]
        return any(all(b[i] == letter for i in line) for line in lines)

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v == " "]

    def clear_oldest_move(self, letter: str):
        """Manual clear if ever needed."""
        if self.history[letter]:
            o = self.history[letter].pop(0)
            self.board[o] = " "
            return o
        return None
