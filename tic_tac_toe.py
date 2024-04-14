import random


def print_board(board, cordinates):
    print("====WELCOME TO TIC-TAC-TOE====")
    print("")
    print("Game table")
    for row in board:
        print(row)
    print("")
    print("------------------------------------")
    print("")
    for cell in cordinates:
        print(cell)
    print("")


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def computer_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "O"
                if check_winner(board, "O"):
                    return
                board[row][col] = ""

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "X"
                if check_winner(board, "X"):
                    board[row][col] = "O"
                    return
                board[row][col] = ""

    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"


while True:
    tic_tac_toe = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    coordinates = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    game = True

    while game:
        print_board(tic_tac_toe, coordinates)
        user_x = int(input("Place X in specific coordinate: "))
        row_idx = (user_x - 1) // 3
        col_idx = (user_x - 1) % 3
        if tic_tac_toe[row_idx][col_idx] == "":
            tic_tac_toe[row_idx][col_idx] = "X"
        else:
            print("Cell already occupied. Try again.")
            continue

        if check_winner(tic_tac_toe, "X"):
            print_board(tic_tac_toe, coordinates)
            print("Congratulations! You won!")
            break

        computer_move(tic_tac_toe)

        if check_winner(tic_tac_toe, "O"):
            print_board(tic_tac_toe, coordinates)
            print("Sorry, you lost. Better luck next time!")
            break

        if all(tic_tac_toe[row][col] != "" for row in range(3) for col in range(3)):
            print_board(tic_tac_toe, coordinates)
            print("It's a tie!")
            break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Bye!")
        break
