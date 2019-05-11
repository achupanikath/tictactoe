"""tictactoe game for 2 players"""
choices = []
# choices was not defined
for x in range (1, 10) :
    #range was filled in as 1-10, whereas index starts at 0, so we go from 1-9 with index positions from 0-8
    choices.append(x)

playerOneTurn = True
# assignment was done using the '==' comparison operator incorrectly
winner = False


def printBoard() :
    print( '\n -----')
    print( '|' + str(choices[0]) + '|' + str(choices[1]) + '|' + str(choices[2]) + '|')
    print( ' -----')
    print( '|' + str(choices[3]) + '|' + str(choices[4]) + '|' + str(choices[5]) + '|')
    print( ' -----')
    print( '|' + str(choices[6]) + '|' + str(choices[7]) + '|' + str(choices[8]) + '|')
    print( ' -----\n')


while winner != True :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue

    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        # 'choice-1' rightly determines the position. The initial code accesses the wrong index number
        # '=' instead of '==' was used to compare in the if statement above
        print("illegal move, please try again")
        continue

    if playerOneTurn :
        #character must be enclosed
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1  ] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        # indentation in the line above was incorrect.
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        # True instead of true for boolean value
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")