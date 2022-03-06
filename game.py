DEFAULT_BOARD_SIZE = 9
BOARD = {key: " " for key in range(1, DEFAULT_BOARD_SIZE + 1)}
X = "X"
O = "O"


def print_board(board):
    buildstr = ""
    for loc, move in board.items():
        buildstr += f"|{move}|\t"
        if not loc % 3:
            buildstr += f"\n"
    print(buildstr)


def make_move():
    def collect_input(msg):
        return int(input(msg))

    loc = collect_input("Enter move location:")
    while not loc in BOARD or not BOARD[loc]:
        loc = collect_input("Invalid move! Enter move location:")

    return loc


def is_winner(board):
    winning_indicies = [[1, 2, 3], [1, 4, 7], [3, 6, 9], [7, 8, 9], [1, 5, 9]]
    for combo in winning_indicies:
        filtered_board = [val for key, val in board.items() if key in combo]
        if all(move == X for move in filtered_board) or all(move == O for move in filtered_board):
            return True
    return False


def is_draw(board):
    return all(move in [X, O] for loc, move in board.items())


def check_result(board):
    if is_winner(board):
        return True, "Winner!"
    elif is_draw(board):
        return True, "Draw!"
    return False, ""


def play_game():
    print_board(BOARD)
    board = BOARD.copy()
    rounds = 1
    while True:
        move = make_move()
        board[move] = X if not rounds % 2 else O
        print_board(board)
        endgame, outcome = check_result(board)
        print(outcome)
        if endgame:
            break
        rounds += 1


def main():
    play_game()


if __name__ == "__main__":
    main()
