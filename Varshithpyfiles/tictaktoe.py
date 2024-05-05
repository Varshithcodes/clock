import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, mark):
    for row in board:
        if all(spot == mark for spot in row):
            return True
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(spot != ' ' for spot in row) for row in board)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def make_move(board, row, col, mark):
    board[row][col] = mark

def player_move(board, mark):
    while True:
        try:
            move = input(f"Player {mark}, enter your move as row,col (1-3,1-3): ")
            row, col = map(int, move.split(','))
            if board[row-1][col-1] == ' ':
                make_move(board, row-1, col-1, mark)
                break
            else:
                print("This cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row,col as 1,1 or 2,2 etc.")

def computer_move(board, mark):
    opponent = 'X' if mark == 'O' else 'O'
    available_moves = get_available_moves(board)

    # Check for win or block opponent's win
    for row, col in available_moves:
        board[row][col] = mark
        if check_winner(board, mark):
            return
        board[row][col] = ' '  # Undo move

        board[row][col] = opponent
        if check_winner(board, opponent):
            make_move(board, row, col, mark)
            return
        board[row][col] = ' '  # Undo move

    # If no immediate win or block, choose a random move
    row, col = random.choice(available_moves)
    make_move(board, row, col, mark)

def tic_tac_toe_game(mode='PVP'):
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_mark = 'X'

    while True:
        print_board(board)
        if current_mark == 'O' and mode == 'PVC':
            computer_move(board, 'O')
        else:
            player_move(board, current_mark)

        if check_winner(board, current_mark):
            print_board(board)
            print(f"Player {current_mark} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_mark = 'O' if current_mark == 'X' else 'X'

def main():
    while True:
        mode = input("Enter game mode (PVP or PVC): ").upper()
        if mode in ['PVP', 'PVC']:
            tic_tac_toe_game(mode)
        else:
            print("Invalid mode. Please choose PVP for Player vs Player or PVC for Player vs Computer.")
            continue

        if input("Play again? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()