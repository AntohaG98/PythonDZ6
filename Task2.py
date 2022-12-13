def print_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[1]} | {board[2]} | {board[3]} ")


def is_win(board, player):
    # if board[1] == player and board[2] == player and board[3] == player:
    #     return True
    # elif board[4] == player and board[5] == player and board[6] == player:
    #     return True
    # elif board[7] == player and board[8] == player and board[9] == player:
    #     return True
    # elif board[1] == player and board[4] == player and board[7] == player:
    #     return True
    # elif board[2] == player and board[5] == player and board[8] == player:
    #     return True
    # elif board[3] == player and board[6] == player and board[9] == player:
    #     return True
    # elif board[1] == player and board[5] == player and board[9] == player:
    #     return True
    # elif board[3] == player and board[5] == player and board[7] == player:
    #     return True

    for i in range(3):
        if board[1 + i * 3] == player and board[2 + i * 3] == player and board[3 + i * 3] == player:
            return True

    for i in range(3):
        if board[1 + i] == player and board[4 + i] == player and board[7 + i] == player:
            return True

    for i in range(2):
        if board[1 + i * 2] == player and board[5] == player and board[9 - i * 2] == player:
            return True

    return False


def is_draw(board):
    for i in board:
        if board[i] == " ":
            return False
    return True


def input_num(player, board):
    while True:
        number_on_board = input(f"\nХод {player} ,выберете клетку: ")
        print()
        if number_on_board.isdigit():
            if 1 <= int(number_on_board) <= 9:
                if board[int(number_on_board)] == " ":
                    return int(number_on_board)
                else:
                    print("Клетка занята!")
            else:
                print("Неверное значение!")
        else:
            print("Это не число!")


dict_board_example = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
dict_board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
print_board(dict_board_example)
move_x = True

player_1 = "X"
player_2 = "O"

while not is_win(dict_board, player_1) and not is_win(dict_board, player_2) and not is_draw(dict_board):
    if move_x:
        num = input_num(player_1, dict_board)
        dict_board[num] = player_1
    else:
        num = input_num(player_2, dict_board)
        dict_board[num] = player_2
    move_x = not move_x
    print_board(dict_board)

if is_draw(dict_board):
    print("Ничья")
elif is_win(dict_board, player_1):
    print("Победил Х")
else:
    print("Победил O")