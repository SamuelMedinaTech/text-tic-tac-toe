from logo import logo

# VARIABLES
grid_data = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

player_pieces = {
    '1': {
        'piece': 'O',
        'winning_line': 'OOO'
    },
    '2': {
        'piece': 'X',
        'winning_line': 'XXX'
    }
}


# FUNCTIONS
def display_grid():
    print("\n")
    print(f' {grid_data[0][0]} | {grid_data[0][1]} | {grid_data[0][2]}')
    print("-----------")
    print(f' {grid_data[1][0]} | {grid_data[1][1]} | {grid_data[1][2]}')
    print("-----------")
    print(f' {grid_data[2][0]} | {grid_data[2][1]} | {grid_data[2][2]}')
    print("\n")


def check_row(player_piece):
    for row in grid_data:
        row_string = ''.join(row)
        if row_string == player_pieces[player_piece]['winning_line']:
            return True
        else:
            return False


def check_column(player_piece):
    for i in range(3):
        column_values = [grid_data[0][i], grid_data[1][i], grid_data[2][i]]
        column_string = ''.join(column_values)
        if column_string == player_pieces[player_piece]['winning_line']:
            return True
        else:
            return False


def check_winner(player_piece):
    if check_row(player_piece) or check_column(player_piece):
        return True
    else:
        return False


def input_player_move(player_piece):
    global grid_data

    row = int(input(f'Player {player_piece} Select a row (1 - 3): '))
    column = int(input(f'Player {player_piece} Select a column (1 - 3): '))

    if grid_data[row - 1][column - 1] != ' ':
        print('That spot has already been taken. Please choose another.')
        display_grid()
        input_player_move(player_piece)
    else:
        grid_data[row - 1][column - 1] = player_pieces[player_piece]['piece']


def show_winner(player_piece):
    print(f'Congratulations, Player {player_piece}. You won!')


if __name__ == '__main__':
    is_game_over = False

    while not is_game_over:
        print(logo)

        while True:
            display_grid()
            input_player_move('1')
            if check_winner('1'):
                show_winner('1')
                break
            display_grid()
            input_player_move('2')
            if check_winner('2'):
                show_winner('2')
                break

        continue_playing = input("Do you want to continue playing? (Y/N): ")
        if continue_playing != 'Y':
            is_game_over = True

    print("Thank you for playing!!")
