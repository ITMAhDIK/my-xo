from termcolor import colored

board = list(range(1, 10))
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))

moves = ((1, 7, 3, 9), (5,), (2, 4, 8, 6))


def print_board():
    j = 1
    for i in board:
        end = "  "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "O":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


player, computer = "X", "O"


def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve - 1] = mve
        return True, win
    return False, False


def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve - 1], int):
        return True
    return False


def is_winner(brd, plyr):
    for i in winners:
        if all(brd[j] == plyr for j in i):
            return True
    return False


def has_empty_space():
    return any(isinstance(x, int) for x in board)


def computer_move():
    mv = -1
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    if mv == -1:
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                mv = i
                break
    if mv == -1:
        for tup in moves:
            for i in tup:
                if mv == -1 and can_move(board, i):
                    mv = i
                    break

    return make_move(board, computer, mv)


print("player: X\ncomputer: O\n")
while has_empty_space():
    print_board()
    my_move = int(input("your move:\t"))
    moved, won = make_move(board, player, my_move)

    if not moved:
        print(colored("invalid!", "red"))
        continue
    if won:
        print(colored("you win!", "green").upper())
        break
    if computer_move()[1]:
        print_board()
        print(colored("you lose!", "yellow").upper())
        break

    if not has_empty_space():
        print_board()
        print(colored("it's a tie!", "yellow").upper())
        break

print_board()
