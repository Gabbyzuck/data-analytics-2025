# Step 1: Create the game board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


# Step 2: Display the game board
def display_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Step 3: Get player input
def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position. Choose numbers between 0 and 2.")
            elif board[row][col] != " ":
                print("That spot is already taken. Try again.")
            else:
                return row, col
        except ValueError:
            print("Please enter valid numbers.")


# Step 4: Check for a winner
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Step 5: Check for a tie
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


# Step 6: Main game loop
def play():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        row, col = player_input(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("🤝 It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Start the game
play()
