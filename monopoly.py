from sys import argv
from random import randint

if len(argv) < 2:
    print("Usage: python3 monopoly.py [noIterations]")

iterations = int(argv[1])

# Initialise the board
board = [0 for i in range(40)]

# One in 16 chance of going to jail for both community and chance

# Ignoring both community and chance in monopoly.py version 0.0.1
doubles = 0
currentPos = 0
for i in range(iterations):
    # Roll two dies
    dices = [randint(1, 6) for i in range(2)]

    # Check for doubles
    if dices[0] == dices[1]:
        doubles += 1
        if (doubles) == 3:
            currentPos = 10

    # Check for out of boundary (i.e. finished one cycle)
    currentPos = (currentPos + sum(dices)) % 40

    # Check for jail
    if currentPos == 30:
        currentPos = 10

    board[currentPos] += 1

# Calculate Probability
board = [("%.3f" % (i / iterations)) for i in board]
print(board)