import board

def finish(ticTac):
    print("--------------")
    print("Final result: ")
    print(ticTac)

    if (ticTac.evaluate() == 0):
        print("The game is a tie!")
    elif (ticTac.evaluate() == -1):
        print("The game is won!")
    else:
        print("The game is lost!")

    if(str(input("Again(y/n): ")).strip() == 'y'):
        run()
    else:
        exit()

def run():
    symbol = str(input("Choose your symbol(x or o): ")).strip()
    if (symbol == 'x'):
        ai = 'o'
    else:
        ai = 'x'

    ticTac = board.TicTacToeBoard(symbol, ai)
    turn = 0

    while(True):
        if (turn == 0):
            print(ticTac)

        print("\nEnter location(x y): ")
        x, y = map(int, input().split())
        ticTac.place(x, y)
        print("Player turn:")
        print(ticTac)
        if (not ticTac.areMovesLeft() or ticTac.evaluate() == 1 or ticTac.evaluate() == -1):
            finish(ticTac)
            break
        
        ticTac.moveAI()
        print("\nAI turn:")
        print(ticTac)
        if (not ticTac.areMovesLeft() or ticTac.evaluate() == 1 or ticTac.evaluate() == -1):
            finish(ticTac)
            break
        turn += 1

run()
