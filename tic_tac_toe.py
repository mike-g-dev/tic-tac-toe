from game import game_builder


def main():
    print("Starting game of tic-tac-toe...")
    game = game_builder()
    game.play_game()
    print("Game over.")


if __name__ == "__main__":
    main()
