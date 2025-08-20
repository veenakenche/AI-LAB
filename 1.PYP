import math,random

def check(board):
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c] and board[a]!=" ":
            return board[a]
    return "draw" if " " not in board else None

def minimax(board,ismax):
    res=check(board)
    if res: return {"X":-1,"O":1,"draw":0}[res],None
    best=(-math.inf,None) if ismax else (math.inf,None)
    for i in range(9):
        if board[i]==" ":
            board[i]="O" if ismax else "X"
            score,_=minimax(board,not ismax)
            board[i]=" "
            if ismax and score>best[0]: best=(score,i)
            if not ismax and score<best[0]: best=(score,i)
    return best

board=[" "]*9
while not check(board):
    print("\n".join(["|".join(board[i:i+3]) for i in range(0,9,3)]))
    move=int(input("Your move (0-8):"))
    if board[move]!=" ":continue
    board[move]="X"
    if check(board):break
    _,ai=minimax(board,True)
    board[ai]="O"

print("\n".join(["|".join(board[i:i+3]) for i in range(0,9,3)]))
print("Result:",check(board))

