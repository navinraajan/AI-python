# Define the game board and player symbols
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == PLAYER_X for cell in row):
            return PLAYER_X
        elif all(cell == PLAYER_O for cell in row):
            return PLAYER_O

    # Check columns
    for col in range(3):
        if all(board[row][col] == PLAYER_X for row in range(3)):
            return PLAYER_X
        elif all(board[row][col] == PLAYER_O for row in range(3)):
            return PLAYER_O

    # Check diagonals
    if all(board[i][i] == PLAYER_X for i in range(3)):
        return PLAYER_X
    elif all(board[i][2 - i] == PLAYER_X for i in range(3)):
        return PLAYER_X

    # Check for a draw
    if all(cell != EMPTY for row in board for cell in row):
        return 'Draw'

    return None

def alphabeta(board, depth, alpha, beta, maximizing_player):
    winner = check_winner(board)

    if winner:
        if winner == PLAYER_X:
            return 1
        elif winner == PLAYER_O:
            return -1
        else:
            return 0

    if maximizing_player:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    eval = alphabeta(board, depth + 1, alpha, beta, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    eval = alphabeta(board, depth + 1, alpha, beta, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = -float('inf')

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                eval = alphabeta(board, 0, -float('inf'), float('inf'), False)
                board[row][col] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)

    return best_move

def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    current_player = PLAYER_X

    print("Tic Tac Toe Game")

    while True:
        print_board(board)

        if current_player == PLAYER_X:
            row, col = find_best_move(board)
            board[row][col] = current_player
            print(f"Player X places {current_player} at ({row+1}, {col+1})")
        else:
            row, col = map(int, input(f"Player O, enter row and column (e.g., 1 2): ").split())
            if board[row - 1][col - 1] == EMPTY:
                board[row - 1][col - 1] = current_player
            else:
                print("That cell is already occupied. Try again.")
                continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    play_game()
