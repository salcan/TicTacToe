from __future__ import print_function
from IPython.display import clear_output

def player_input():
    
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('Player one: do you want to be X or O?')
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O','X')

def play_game():
    reset_board()
    global announce
    
    # Set marks
    X='X'
    O='O'
    while True:
        # Show board
        clear_output()
        display_board()
        
        # Player X turn
        game_state,announce = player_choice(X)
        print(announce)
        if game_state == False:
            break
            
        # Player O turn
        game_state,announce = player_choice(O)
        print(announce)
        if game_state == False:
            break
    
    # Ask player for a rematch
    rematch = raw_input('Would you like to play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print("Thanks for playing!")

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

def display_board(board):
 
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|- -|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|- -|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

board = ['empty','1','2','3','4','5','6','7','8','9']
display_board(board)
    
player_input()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, player):
    if (board[7]  ==  board[8] ==  board[9] == player) or \
        (board[4] ==  board[5] ==  board[6] == player) or \
        (board[1] ==  board[2] ==  board[3] == player) or \
        (board[7] ==  board[4] ==  board[1] == player) or \
        (board[8] ==  board[5] ==  board[2] == player) or \
        (board[9] ==  board[6] ==  board[3] == player) or \
        (board[1] ==  board[5] ==  board[9] == player) or \
        (board[3] ==  board[5] ==  board[7] == player):
        return True
    else:
        return False

def full_board_check(board):
    ''' Function to check if any remaining blanks are in the board '''
    if " " in board[1:]:
        return False
    else:
        return True

def ask_player(mark):
    ''' Asks player where to place X or O mark, checks validity '''
    global board
    req = 'Choose where to place your: ' + mark
    while True:
        try:
            choice = int(raw_input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("That space isn't empty!")
            continue

def player_choice(mark):
    global board,game_state,announce
    #Set game blank game announcement
    announce = ''
    #Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    #Check for player win
    if win_check(board,mark):
        clear_output()
        display_board()
        announce = mark +" wins! Congratulations"
        game_state = False
    
    #Show board
    clear_output()
    display_board()

    #Check for a tie 
    if full_board_check(board):
        announce = "Tie!"
        game_state = False
        
    return game_state,announce

