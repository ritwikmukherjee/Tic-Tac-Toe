from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        
        marker=input('Player1, choose between X and O:')
        player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)

def win_check(board, mark):
    return [board[1],board[2],board[3]].count(mark)==3 or [board[4],board[5],board[6]].count(mark)==3  or [board[7],board[8],board[9]].count(mark)==3 or [board[1],board[4],board[7]].count(mark)==3 or [board[2],board[5],board[8]].count(mark)==3 or [board[3],board[6],board[9]].count(mark)==3 or [board[1],board[5],board[9]].count(mark)==3 or [board[3],board[5],board[7]].count(mark)==3

def space_check(board, position):
    return ' ' in board[position]

def full_board_check(board):
    return board.count(' ')==1

def player_choice(board,player_marker):
    position=int(input('What is your move?'))
    if space_check(board,position):
        place_marker(board,player_marker,position)
    else:
        print('Cannot put there')
        player_choice(board,player_marker)
        
def replay():
    result=input('Play Again?')
    if result == 'Yes' or result == 'yes' or result == 'YES':
        board=[' ']*10        
        tic_tac_toe(board)
    elif result == 'No' or result == 'no' or result == 'NO':
        exit()
    else: 
        replay()
        
def place_marker(board,player_marker,position):
    board[position]=player_marker
    
def play(board,player1_marker,player2_marker,flag):
    print('Player1 play')
    player_marker=player1_marker
    player_choice(board,player_marker)
    if win_check(board,player_marker):
        display_board(board)
        print('Congratulations Player1 has won !')
        flag=1
        return flag
    if full_board_check(board):
        flag=-1
        return flag
    else:
        display_board(board)
    print('Player2 play')
    player_marker=player2_marker
    player_choice(board,player_marker)
    if win_check(board,player_marker):
        display_board(board)
        print('Congratulations Player2 has won !')
        flag=1
        return flag
    if full_board_check(board):
        flag=-1
        return flag
    else:
        display_board(board)
        
def tic_tac_toe(board):
    display_board(board)
    print('Welcome! Ready for a game of Tic-Tac-Toe?')
    (player1_marker,player2_marker)=player_input()
    print('Player 1 play')
    player_marker=player1_marker
    player_choice(board,player_marker)
    display_board(board)
    print('Player 2 play')
    player_marker=player2_marker
    player_choice(board,player_marker)
    display_board(board)
    flag=0
    while(True):
        flag=play(board,player1_marker,player2_marker,flag)
        if flag==1:
            break
        elif flag==-1:
            print('Tie!')
            break
        else:
            continue
    replay()
    

