from sys import argv
from random import randint, shuffle

if len(argv) < 2:
    print("Usage: python3 monopoly.py [noIterations]")

iterations = int(argv[1])

# Initialise the board
board = [0 for i in range(40)]

# Initialise and Shuffle Chance and Treasure cards
chance = [0, 24, 11, "U", "R", -3, 10, 5, 39] + [None] * 7
treasure = [0, 10] + [None] * 14
shuffle(chance)
shuffle(treasure)

doubles = 0
currentPos = 0

rolls = [0 for i in range(12)]

for i in range(iterations):
    # Roll two dies
    dices = [randint(1, 6) for i in range(2)]

    # This is for calculating dice roll distribution
    rolls[sum(dices) - 1] += 1 

    # Check for doubles
    if dices[0] == dices[1]:
        doubles += 1
        if (doubles) == 3:
            currentPos = 10
            # Continue to the next iteration
            continue

    # Check for out of boundary (i.e. finished one cycle)
    currentPos = (currentPos + sum(dices)) % 40

    # Check for jail, treasure and chance
    if currentPos == 30:
        currentPos = 10

    # Treasure
    elif currentPos in (2, 17, 33):
        # Only two cards which are not nones, and they both teleports the player
        if treasure[0]:
            currentPos = treasure[0]

        # Discard the top card and chuck it at the bottom
        treasure.append(treasure.pop(0))

    # Chance
    elif currentPos in (7, 22, 36):

        if isinstance(chance[0], str):
            # Railroad or utility
            if chance[0] == "U":
                # Teleport to nearest utility (always go to the next one)
                currentPos = 12 if currentPos > 28 else 28
            else:
                # Teleport to nearest railroad (always go to the next one)
                if currentPos < 5 or currentPos > 35:
                    currentPos = 5
                elif 5 < currentPos < 15:
                    currentPos = 15
                elif 15 < currentPos < 25:
                    currentPos = 25
                else:
                    currentPos = 35

        elif isinstance(chance[0], int):
            # Teleport or moving backwards
            if chance[0] < 0:
                # One card that moves back
                currentPos -= chance[0]
            else:
                # Rest is teleporting somewhere
                currentPos = chance[0]

        chance.append(chance.pop(0))

    board[currentPos] += 1

# Dice Distribution
print("Dice Distribution:")
print(rolls)

# Calculate Probability
print("Raw Frequency:")
print(board)

#print("Percentage Based Frequency:")
# Precomputations for the next set of statistics
board = [round(i / iterations * 100, 4) for i in board]
print(board)


setTable = {
    "Brown": round(board[1] + board[3], 4),
    "Light Blues": round(board[6] + board[8] + board[9], 4),
    "Pinks": round(board[11] + board[13] + board[14], 4),
    "Oranges": round(board[16] + board[18] + board[19], 4),
    "Reds": round(board[21] + board[23] + board[24], 4),
    "Yellows": round(board[26] + board[27] + board[29], 4),
    "Greens": round(board[31] + board[32] + board[34], 4),
    "Dark Blues": round(board[37] + board[39], 4),
    "Stations": round(board[5] + board[15] + board[25] + board[35], 4),
    "Utilities": round(board[12] + board[28], 4),
    "Jail": round(board[10], 4),
}

"""
for k, v in setTable.items():
    print(f"{k}: {v}%")
"""

ladder = sorted(setTable, key=lambda item: setTable[item], reverse=True)
for i in range(len(ladder)):
    print(f"{i + 1}: {ladder[i]}, {setTable[ladder[i]]}%")

# TODO: Utilities need to record what dies led to them
# TODO: Money: Rent, Mortgage, Optimal Price and Upgrades
# TODO: Overall utility for a property (i.e. a score for each property)