# Tic Tac Toe Game (Two Players)

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_conditions:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def check_draw():
    return all(space != " " for space in board)

def play_game():
    current_player = "X"
    while True:
        print_board()
        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Position already taken! Try again.")
            continue

        if check_win(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if check_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
