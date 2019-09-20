import random
board = [list(), list(), list(), list(),list()]
blacklist = list()

def generateRandom(blacklist):
    while True:
        try:
            num = random.randint(1,91)
            blacklist.index(num)
        except ValueError:
            return num


for x in range(0,5):
    for y in range(0,5):
        num = generateRandom(blacklist)
        board[x].append(num)
        blacklist.append(num)


for y in range(0,5):
    for x in range(0,5):
        print(board[x][y],end=" ")
    print()

