import random
import copy
notDrawn = list(range(1,92))

def clearScreen():
    print(chr(27) + "[2J") # Escape sequence to clear screen

def generateRandom(blacklist):
    while True:
        try:
            num = random.randint(1,91)
            blacklist.index(num)
        except ValueError:
            return num

def generateBoard():
    blacklist = list()
    board = [list(), list(), list(), list(),list()]
    for x in range(0,5):
        for y in range(0,5):
            num = generateRandom(blacklist)
            board[x].append(num)
            blacklist.append(num)
    board[2][2] = ' X'
    return board

def inBoard(num, board):
    for x in range(0,5):
        for y in range(0,5):
            if num == board[x][y]:
                board[x][y] = ' X'
                return True
    return False

def didWin(board):
    #check for horizontal win
    for x in range(0,5):
        count = 0
        for y in range(0,5):    
            if board[y][x] != ' X':
                break
            else:
                count += 1
        if count == 5:
            return True
    
    #check for vertical win
    for y in range(0,5):
        count = 0
        for x in range(0,5):   
            if board[y][x] != ' X':
                break
            else:
                count += 1
        if count == 5:
            return True

    #check for diagonal - top left to bottom right
    count = 0  
    for i in range(0,5):  
        if board[i][i] != ' X':
            break
        else:
            count += 1
    if count == 5:
        return True

    #check for diagnal - top right to bottom left
    count = 0  
    for x in range(0,5):    
        if board[4-x][x] != ' X':
            break
        else:
            count += 1
    if count == 5:
        return True

    return False

def printBoard(board, OG):
    for y in range(0,5):
        ogStr = ''
        for x in range(0,5):
            print(board[x][y],end=" ")
            ogStr += str(OG[x][y]) + ' '
        print('   ' + ogStr)

def draw(notDrawn):
    num = notDrawn[random.randint(0,len(notDrawn)-1)]
    notDrawn.remove(num)
    return num

board1 = generateBoard()
OG_BOARD1 = copy.deepcopy(board1)

clearScreen()
print('Press Enter to Draw Number. Enter q, then press enter to quit.')
printBoard(board1, OG_BOARD1)

# TO DO: Add check for win.
# TO DO: Print single digits in 2 digits, ex: 09
while True:
    userInput = input()
    print()
    clearScreen()
    if userInput == 'q':
        printBoard(board1, OG_BOARD1)
        print("Game Over")
        exit()
    else:
        curDraw = draw(notDrawn)
        found = inBoard(curDraw, board1)
        printBoard(board1, OG_BOARD1)
        if didWin(board1) == True:
            print('BINGO!!! --- YOU WIN!')
        else:
            if found == True:
                print("Found a match! (((o(*ﾟ▽ﾟ*)o))) --- Drew " + str(curDraw))
            else:
                print("Bad draw. No Match. (ノ°Д°）ノ︵ ┻━┻ --- Drew " + str(curDraw))













