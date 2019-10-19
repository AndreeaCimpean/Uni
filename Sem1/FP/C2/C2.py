def get_board(board,x,y):               #not UI
    return board[3*x+y]

def init_board():                       #not UI
    '''
    x->1    human
    0->-1   computer
    '''
    return [0]*9

def print_board(board):                 #UI
    for i in range(3):
        res=''
        for j in range(3):
            sign = get_board(board,i,j)
            if sign == -1:
                res+='0'
            elif sign == 0:
                res+='*'
            elif sign == 1:
                res+='x'
        print(res)
    print(' ')

def move_board(board,x,y,sign):         #not UI
    '''
    Make a valid move on the board
    params
        board - the board
        x,y - coordinates 0<=x,y<=2
        sign - in {-1,1}
    output
        None - success
        error msg - otherwise
    '''
    if x not in [0,1,2] or y not in [0,1,2]:
        return 'not onboard'
    if get_board(board,x,y) != 0:
        return 'square taken'
    board[3*x+y] = sign
    return None

def read_move():                        #UI
    x = int(input('x='))
    y = int(input('y='))
    return (x,y)

def ai_move(board):                     #not UI
    for i in range(3):
        for j in range(3):
            if get_board(board,i,j) == 0:
                move_board(board,i,j,-1)
                return

def game_won(board):                    #not UI
    #lines
    for i in range(0,9,3):
        if sum(board[i:i+3]) in [-3,3]:
            return True
    #columns
    for i in range(3):
        if board[i]+board[i+3]+board[i+6] in [-3,3]:
            return True
    #diagonals
    if board[0]+board[4]+board[8] in [-3,3] or board[2]+board[4]+board[6] in [-3,3]:
        return True
    return False

def game_tie(board):
    for i in range(3):
        for j in range(3):
            sign = get_board(board,i,j)
            if sign == 0:
                return False
    return True

def start():                            #UI          
    b=init_board()
    print("Let's play tic-tac-toe")
    print_board(b)
    while True:
        move = read_move()
        res = move_board(b,move[0],move[1],1)
        while res != None:
            print(res)
            move = read_move()
            res = move_board(b,move[0],move[1],1)
        if game_won(b):
            print_board(b)
            print('yay')
            return
        if game_tie(b):
            print_board(b)
            print("oh it's a tie")
            return
        ai_move(b)
        print_board(b)
        if game_won(b):
            #print_board(b)
            print('nay')
            return
                
start()
