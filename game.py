import random
import copy

def clearScreen():
    print(chr(27) + "[2J") # Escape sequence to clear screen


def generateBoard():
    whitelist = list(range(1,92))
    board = [list(), list(), list(), list(),list()]
    for x in range(0,5):
        for y in range(0,5):
            i = random.randint(0,len(whitelist))
            num = whitelist[i]
            del whitelist[i]
            board[x].append(num)
    board[2][2] = ' X'
    return board

# checks board if contains num
def inBoard(num, board):
    for x in range(0,5):
        for y in range(0,5):
            if num == board[x][y]:
                board[x][y] = ' X'
                return True
    return False

# bool on if board meets win condition
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



# TO DO: Add check for win.
# TO DO: Print single digits in 2 digits, ex: 09

def playGame():
    notDrawn = list(range(1,92))
    board1 = generateBoard()
    OG_BOARD1 = copy.deepcopy(board1)

    clearScreen()
    print('Press Enter to Draw Number. Enter q, then press enter to quit.')
    printBoard(board1, OG_BOARD1)

    while True:
        userInput = input()
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
                while True:
                    clearScreen()
                    print('Winner! Enter "new" to start new game. Enter "q" to quit.')
                    printBoard(board1, OG_BOARD1)
                    print('BINGO!!! --- YOU WIN! --- Drew ' + str(curDraw))
                    userInput = input()
                    if userInput == 'q':
                        print("Game Over")
                        return False
                    elif userInput == 'new':
                        return True
            else:
                if found == True:
                    print("Found a match! (((o(*ﾟ▽ﾟ*)o))) --- Drew " + str(curDraw))
                else:
                    print("Bad draw. No Match. (ノ°Д°）ノ︵ ┻━┻ --- Drew " + str(curDraw))

runGame = True
while runGame == True:
    runGame = playGame()












