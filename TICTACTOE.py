import Game


def game1():
    print("WELCOME TO TICTACTOE GAME")

    player1 = input("\n\nEnter first player name ")
    player2 = input("\n\nEnter second player name ")

    board = ["-" for i in range(9)]

    def display_board():
        print("|", board[0], "|", board[1], "|", board[2], "|")
        print("|", board[3], "|", board[4], "|", board[5], "|")
        print("|", board[6], "|", board[7], "|", board[8], "|")

    firstplayer = "x"
    secondplayer = "o"

    print(player1 + " Your value is x")
    print(player2 + " Your value is o")

    def check_condition(player):
        conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for check in conditions:
            if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
                return 1
        else:
            return

    def start_game():
        display_board()
        while True:

            while True:
                player1_option = input(f"{player1}, Enter a value between(1-9)")

                if player1_option not in [str(i) for i in range(1, 10)]:
                    print("Invalid input, Enter again")
                    continue

                if board[int(player1_option) - 1] == "-":
                    board[int(player1_option) - 1] = firstplayer
                    display_board()

                    if check_condition(firstplayer):
                        return f"winner is: {player1}"

                    break
                else:
                    print("This place is OCCUPIED")

            while True:
                player2_option = input(f"{player2}, Enter a value between(1-9)")

                if player2_option not in [str(i) for i in range(1, 10)]:
                    print("Invalid input, Enter again")
                    continue

                if board[int(player2_option) - 1] == "-":
                    board[int(player2_option) - 1] = secondplayer
                    display_board()

                    if check_condition(secondplayer):
                        return f"winner is: {player2}"

                    break
                else:
                    print("This place is OCCUPIED")

            if len([i for i in board if i != "-"]) == 0:
                return ""

    print(start_game())

    while True:
        user_input = input("Enter \"P\"to PLAY AGAIN or Enter \"Q\"to QUIT")
        if user_input in "Pp":
            board = ["-" for i in range(9)]
            print(start_game())
        elif user_input in "qQ":
            print("Thanks for playing")
            Game.game()
            break
