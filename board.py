from input_interface import InputInterface
DEFAULT_BOARD_SIZE = 9
X = "X"
O = "O"


class Board:
    def __init__(self, input_interface=InputInterface(), size=DEFAULT_BOARD_SIZE):
        self.input_interface = input_interface
        self.size = size
        self._board = {key: " " for key in range(1, DEFAULT_BOARD_SIZE + 1)}
        self._moves = []

    def __str__(self):
        representation = ""
        for loc, move in self._board.items():
            representation += f"|{move}|\t"
            if not loc % 3:
                representation += f"\n"
        return representation

    def _collect_input(self, msg: str):
        return self.input_interface.read_input(msg, cast=int)

    def _new_state(self, move: int):
        self._moves.append(move)
        board_copy = self._board.copy()
        board_copy[move] = X if not len(self._moves) % 2 else O
        self._board = board_copy

    def make_move(self):
        loc = self._collect_input("Enter move location:")
        while loc not in self._board:
            loc = self._collect_input("Invalid move! Enter move location:")
        while loc in self._moves:
            loc = self._collect_input("Move location already occupied! Enter move location:")
        self._new_state(loc)

    def _is_winner(self):
        winning_indicies = [[1, 2, 3], [1, 4, 7], [3, 6, 9], [7, 8, 9], [1, 5, 9]]
        for combo in winning_indicies:
            filtered_board = [val for key, val in self._board.items() if key in combo]
            if all(move == X for move in filtered_board) or all(move == O for move in filtered_board):
                return True
        return False

    def _is_draw(self):
        return all(move in [X, O] for loc, move in self._board.items())

    def check_result(self):
        if self._is_winner():
            return True, "Winner!"
        elif self._is_draw():
            return True, "Draw!"
        return False, ""
