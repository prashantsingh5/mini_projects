import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] or
            board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
        return board[1][1]

    return None

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Player: X")
    print("Computer: O")

    # Initialize the board
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    player = "X"
    computer = "O"
    moves = 0

    while True:
        print_board(board)

        if player == "X":
            # Player's turn
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))

            if board[row][col] != " ":
                print("Invalid move! Try again.")
                continue

            board[row][col] = player
        else:
            # Computer's turn
            print("Computer's turn...")
            empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
            row, col = random.choice(empty_cells)
            board[row][col] = "O"

        moves += 1

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            if winner == player:
                print("Congratulations! You win!")
            else:
                print("Sorry! You lose!")
            break

        if moves == 9:
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player, computer = computer, player

if __name__ == '__main__':
    play_game()
