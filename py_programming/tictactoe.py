

# O(N)
board = {str(i+1): str(i+1) for i in range(9)}

# O(1)
def print_board(board):
    print("\n")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + "\n")


# O(1)
def check_winner():
    return True if (
        (board['7'] == board['8'] == board['9']) or  # top
        (board['4'] == board['5'] == board['6']) or  # middle
        (board['1'] == board['2'] == board['3']) or  # bottom
        (board['1'] == board['4'] == board['7']) or  # left side
        (board['2'] == board['5'] == board['8']) or  # middle
        (board['3'] == board['6'] == board['9']) or  # right side
        (board['7'] == board['5'] == board['3']) or  # diagonal
        (board['1'] == board['5'] == board['9'])  # diagonal
    ) else False

# O(10)
def play():

    turn = 'X'

    for i in range(10):

        while True:
            print_board(board)
            print("It's your turn, " + turn)
            move = input()

            if str(move) not in board or board[str(move)] != str(move):
                print("Nuh uh, that doesn't work, try somewhere else. \n")
            else:
                break

        if board[move] == str(move):
            board[move] = turn
            print('\n')

        if check_winner():
            print_board(board)
            print("\nGame Over. " + turn + " won the game!")
            break

        if i == 9:
            print("\nGame Over, you tied. \n")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        move = None

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board:
            board[key] = key
        play()


if __name__ == "__main__":
    play()
