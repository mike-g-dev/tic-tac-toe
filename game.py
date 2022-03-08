from board import Board


class Game:
    def __init__(self, board: Board):
        self.board = board

    def play_game(self) -> None:
        print(self.board)
        while True:
            self.board.make_move()
            print(self.board)

            end, outcome = self.board.check_result()
            print(outcome)

            if end:
                break




