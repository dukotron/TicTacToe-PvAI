class TicTacToeBoard:
    def __init__(self, playerChar, aiChar):
        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
        self.playerChar = playerChar
        self.aiChar = aiChar
        self.nullChar = '_'
        self.isPlayerTurn = True

    def evaluate(self):
        for wh in range(len(self.board[0])):
            if (self.board[wh][0] == self.board[wh][1] == self.board[wh][2]):
                return self.__compare(self.board[wh][0])
            elif (self.board[0][wh] == self.board[1][wh] == self.board[2][wh]):
                return self.__compare(self.board[0][wh])

        if (self.board[0][0] == self.board[1][1] == self.board[2][2]):
            return self.__compare(self.board[0][0])
        elif (self.board[0][2] == self.board[1][1] == self.board[2][0]):
            return self.__compare(self.board[0][2])

        return 0

    def miniMax(self, depth, isMax):
        score = self.evaluate()
        
        if (score == 1 or score == -1):
            return score

        if (not self.areMovesLeft()):
            return 0

        if (isMax):
            bestMove = -5
            
            for i in range(len(self.board[0])):
                for j in range(len(self.board[0])):
                    if (self.board[i][j] == '_'):
                        self.board[i][j] = self.aiChar
                        bestMove = max(bestMove, self.miniMax(depth + 1, not isMax))
                        self.board[i][j] = self.nullChar
        else:
            bestMove = 5

            for i in range(len(self.board[0])):
                for j in range(len(self.board[0])):
                    if (self.board[i][j] == '_'):
                        self.board[i][j] = self.playerChar
                        bestMove = min(bestMove, self.miniMax(depth + 1, not isMax))
                        self.board[i][j] = self.nullChar

        return bestMove

    def moveAI(self):
        if (not self.areMovesLeft()):
            return
        
        bestMove = -5
        
        for i in range(len(self.board[0])):
            for j in range(len(self.board[0])):
                if (self.board[i][j] == '_'):
                    self.board[i][j] = self.aiChar
                    newMove = self.miniMax(0, False)
                    self.board[i][j] = '_'

                    if (newMove > bestMove):
                        bestMove = newMove
                        x = i
                        y = j

        self.place(x, y)

    def place(self, x, y):
        if (self.board[x][y] != '_'):
            return

        if (self.isPlayerTurn):
            self.board[x][y] = self.playerChar
        else:
            self.board[x][y] = self.aiChar

        self.isPlayerTurn = not self.isPlayerTurn

    def areMovesLeft(self):
        for i in range(len(self.board[0])):
            for j in range(len(self.board[0])):
                if (self.board[i][j] == '_'):
                    return True
        return False

    def __compare(self, character):
        if (character == self.playerChar):
            return -1
        elif (character == self.aiChar):
            return 1

    def __str__(self):
        tmp = " _____"
        
        for i in range(len(self.board[0])):
            tmp += "\n|"
            for j in range(len(self.board[0])):
                tmp += self.board[i][j] + "|"

        tmp += "\n -----"
        
        return tmp      
