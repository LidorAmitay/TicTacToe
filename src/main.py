import time
from ticTacToe import AI, Game, State


def playGame():
    play = True
    while play:
        # initializing game objects
        myAI = AI()
        myGame = Game(myAI)
        myAI.plays(myGame)

        # simple guide
        printGuide()
        # second to read
        time.sleep(1)

        # print initial board
        myGame.updateBoard()
        while not myGame.currentState.isGameOver():
            # user's turn
            print("Your turn")
            user_move = input("Enter square id(0-8) \n")
            # input validation 
            while not myGame.isValid(user_move):
                user_move = input()
            
            # update state and game according to the user's move
            newState = State()
            newState.updateState(myGame.currentState, {"turn": 'X', "position": int(user_move)})
            myGame.advancedTo(newState)
            myGame.updateBoard()

            if myGame.currentState.isGameOver():
                break
            
            # AI's turn
            print("AI turn")
            myGame.ai.takeMove(myGame.currentState)
            myGame.updateBoard()
        
        # replay option
        keepPlay = input("Another game? press y or anything else to exit")
        play = True if keepPlay == 'y' or keepPlay == 'Y' else False

def printGuide():
    print("Game board example:")
    print('''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        '''.format(*([id for id in range(9)])))
    print('''Each cell has id in range 0-8
When it is your turn, press the id of the relevant cell.\nEnjoy!
=====================================''')

playGame()