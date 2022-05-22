# class to represent a possible game state.  Will be used for traversal by the minimax AI.
class State:
    def __init__(self):
        # whose turn is it?
        self.turn = ""

        # number of AI moves so far - used by the minmax algorithm
        self.depth = 0

        # current representation of board
        # 0 = blank space
        self.board = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]
        
        # current status of the game
        # start - before initial game configuration
        # active - game still active
        # X/O/draw - represent the winner after game ended
        self.result = "active"
    
    def updateState(self, old, move):
        # if old state has been passed in to generate this state, copy the state over.
        if old:
            for i in range(9):
                self.board[i] = old.board[i]

            self.depth = old.depth
            self.result = old.result
            self.turn = old.turn

        # if there's a move object, advance the turn to that move's turn and place it at the specified position
        if move:
            self.turn = move['turn']
            self.board[move['position']] = move['turn']

            if move['turn'] == 'O':
                self.depth += 1
            
            self.turn = 'O' if move['turn'] == 'X' else 'X'

    # find all empty cells in the state and return them
    def getEmptyCells(self):
        indexes = []
        for i in range(9):
            if self.board[i] == 0:
                indexes.append(i)
        
        return indexes
        
    def isGameOver(self):
        # check horizontally
        for i in range(0,7,3):
            if self.board[i] != 0 and\
                self.board[i] == self.board[i+1] and self.board[i+1] == self.board[i+2]:
                self.result = self.board[i]
                return True
        
        # check vertically
        for i in range(3):
            if self.board[i] != 0 and\
                self.board[i] == self.board[i+3] and self.board[i+3] == self.board[i+6]:
                self.result = self.board[i]
                return True

        # check diagonally
        if self.board[4] != 0 and \
            (self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]):
            self.result = self.board[4]
            return True
        
        # check for a draw
        available = self.getEmptyCells()
        if len(available) == 0:
            self.result = 'draw'
            return True
        else:
            return False
class AI:

    def __init__(self):
        # current game being played by the AI.
        self.game = {}

        # variable used to store the next move, determined by the recursive minimax function
        self.nextMove = ''

        # initialize the AI's symbol.
        self.AISymbol = 'O'

    def minimax(self, state:State):

        # if this particular state is a finished game, return the score of the current board.
        if state.isGameOver():
            return self.game.score(state)
        else:
            # store all scores (index will correspond to the array of moves)
            scores = []
            moves = state.getEmptyCells()

            # calculate the minmax value for every possible move.
            for i in range(len(moves)):
                # create a possible state for every possible move
                possibleState = State()
                possibleState.updateState(state, {'turn': state.turn, 'position':moves[i]})

                curScore = self.minimax(possibleState)

                # push that state's score
                scores.append(curScore)
            
            if state.turn == 'X':
                # print(f'scores = {scores}')
                # if it's the player's turn, find the maximum value.
                maxIndex = scores.index(max(scores))
                
                # store the move to be executed
                self.nextMove = moves[maxIndex]

                # return the maximum score
                return scores[maxIndex]
            
            else:
                # if it's the AI's turn, find the minimum value.                
                minIndex = scores.index(min(scores))

                # store the move to be executed
                self.nextMove = moves[minIndex]

                # return the minimum score
                return scores[minIndex]
    
    def plays(self, _game):
        self.game = _game

    def takeMove(self, _state:State):
        _state.turn = self.AISymbol
        # determine next move using minimax algorithm
        self.minimax(_state)

        newState = State()
        newState.updateState(_state, {'turn': self.AISymbol, 'position': self.nextMove})

        # updating game obj state
        self.game.advancedTo(newState)
        
class Game:
    def __init__(self, AI:AI):
        # initialize the AI
        self.ai = AI
        # initialize the game state
        self.currentState = State()
        # X plays first
        self.currentState.turn = 'X'
        # start game
        self.status = 'start'
    
    def advancedTo(self, _state):
        self.currentState = _state
    
    def start(self):
        if self.status == 'start':
            self.advancedTo(self.currentState)
            self.status = 'running'
    

    def updateBoard(self):
        boardToPrint = [sign if sign != 0 else ' ' for sign in self.currentState.board]
        print('''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        '''.format(*(boardToPrint)))

        if self.currentState.isGameOver():
            self.printResult()
    
    def printResult(self):
        if self.currentState.result == 'draw':
            print("Game result is draw")
        elif self.currentState.result == 'X':
            print("You Win!")
        else:
            print("You Lost!")
    
    def isValid(self, input):
        try:
            box = int(input)
        except ValueError:
                # Not an integer
                print('That\'s not a valid number, try again.\n')
                return False

        if box < 0 or box > 8:
            print('That number is out of range, try again.\n')
            return False
        
        elif self.currentState.board[box] != 0:
            print('That box is already marked, try again.\n')
            return False
        else:
            return True

    def score(self, _state:State):
        if _state.result != 'active':
            if _state.result == 'X':
                return 10 - _state.depth
            elif _state.result == 'O':
                return -10 + _state.depth
            else:
                return 0
