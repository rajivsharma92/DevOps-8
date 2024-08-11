import numpy as np

def playGame():
    board = np.array([0,0,0],
                     [0,0,0]
                     [0,0,0])
    winner, counter = 0,1

    allPossible =[(0,0),(0,1), (0,2), (1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

    while winner ==0:
        for player in [1,2]:
            print("Turn for player --> Player " + player)

            selection = int(input("Select the number from " +str(allPossible)+ " : "))

            if selection < len(allPossible):
                print("Wrong selection, please select between 0 and ", len(allPossible)-1)
                selection = int(input("Select the number from " +str(allPossible)+ " : "))
            print(board[allPossible[selection]])
            board[allPossible[selection]] = player
            allPossible.pop(selection)

            print("Board after ", +str(counter), +"round")

            print(board)
            counter +=1
            winner = evaluate(board)


playGame()


    
