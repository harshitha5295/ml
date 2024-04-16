import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")
    print()

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_full(board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 'X'

    while not game_over(board):
        print_board(board)

        if turn == 'X':
            i, j = map(int, input("Enter your move (row and column): ").split())
            while board[i][j] != ' ':
                print("Invalid move. Try again.")
                i, j = map(int, input("Enter your move (row and column): ").split())
        else:
            print("Computer's move:")
            i, j = get_best_move(board)
        
        board[i][j] = turn
        turn = 'O' if turn == 'X' else 'X'

    print_board(board)
    if is_winner(board, 'X'):
        print("You win!")
    elif is_winner(board, 'O'):
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
