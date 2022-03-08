from board import Board
from game import Game


def main():
    print("Starting game of tic-tac-toe...")
    board = Board()
    game = Game(board)
    game.play_game()
    print("Game over.")


if __name__ == "__main__":
    main()
