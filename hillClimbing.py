import random

class nything:
    'class nything is a class that solve NythingProblem from fileInput'
    # attribute
    nNything = 0

    # method
    def __init__(self, fileInput):
        # put information in fileInput (in .txt) to attribute

        # init chess pieces counter and array of chess pieces
        self.nWhiteKnight = 0
        self.nWhiteBishop = 0
        self.nWhiteRook = 0
        self.nWhiteQueen = 0
        self.nBlackKnight = 0
        self.nBlackBishop = 0
        self.nBlackRook = 0
        self.nBlackQueen = 0
        self.chessPieces = []

        # read fileInput
        f = open("test/" + fileInput + ".txt", "r")
        lines = f.read().splitlines()
        # print(lines)
        f.close()

        # put into self attribute
        for line in lines:
            words = line.split(" ")
            if words[0] == "WHITE":
                if words[1] == "KNIGHT":
                    self.nWhiteKnight = int(words[2])
                    for i in range(self.nWhiteKnight):
                        self.chessPieces += "K"
                elif words[1] == "BISHOP":
                    self.nWhiteBishop = int(words[2])
                    for i in range(self.nWhiteBishop):
                        self.chessPieces += "B"
                elif words[1] == "ROOK":
                    self.nWhiteRook = int(words[2])
                    for i in range(self.nWhiteRook):
                        self.chessPieces += "R"
                elif words[1] == "QUEEN":
                    self.nWhiteQueen = int(words[2])
                    for i in range(self.nWhiteQueen):
                        self.chessPieces += "Q"
            elif words[0] == "BLACK":
                if words[1] == "KNIGHT":
                    self.nBlackKnight = int(words[2])
                    for i in range(self.nBlackKnight):
                        self.chessPieces += "k"
                elif words[1] == "BISHOP":
                    self.nBlackBishop = int(words[2])
                    for i in range(self.nBlackBishop):
                        self.chessPieces += "b"
                elif words[1] == "ROOK":
                    self.nBlackRook = int(words[2])
                    for i in range(self.nBlackRook):
                        self.chessPieces += "r"
                elif words[1] == "QUEEN":
                    self.nBlackQueen = int(words[2])
                    for i in range(self.nBlackQueen):
                        self.chessPieces += "q"
            # if it is not white nor black, it is ignored

        # add object counter
        nything.nNything += 1

    def printAttr(self):
        # print attribute
        print("nWhiteKnight : " + str(self.nWhiteKnight))
        print("nWhiteBishop : " + str(self.nWhiteBishop))
        print("nWhiteRook : " + str(self.nWhiteRook))
        print("nWhiteQueen : " + str(self.nWhiteQueen))
        print("nBlackKnight : " + str(self.nBlackKnight))
        print("nBlackBishop : " + str(self.nBlackBishop))
        print("nBlackRook : " + str(self.nBlackRook))
        print("nBlackQueen : " + str(self.nBlackQueen))
        print(self.chessPieces)
        for i in range(8):
            for j in range(8):
                print(self.chessBoard[i][j], end=' ')
            print()

    def randomize(self):
        # randomize chess pieces in matrix based on attributes

        # init chess' locator
        self.chessLocator = []

        # init chess board
        self.chessBoard = [
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]
        ]

        # put chess piece to board
        for piece in self.chessPieces:
            x = random.randint(0,7) # index 0 - 7
            y = random.randint(0,7)
            while (self.chessBoard[x][y] != "."):
                x = random.randint(0,7) # index 0 - 7
                y = random.randint(0,7)
            # get value x, y which place has no piece
            self.chessBoard[x][y] = piece
            self.chessLocator.append((piece, x, y))

    def changePiece(self, piece1, x, y):
        # change piece at chessBoard
        # piece1 and piece2 are tuple of piece, row index, and column index
        w, x0, y0 = piece1
        # w unused
        # move piece on board
        temp = self.chessBoard[x0][y0]
        self.chessBoard[x0][y0] = self.chessBoard[x][y]
        self.chessBoard[x][y] = temp
        # update chessLocator
        i = self.chessLocator.index(piece1)
        self.chessLocator[i] = (w, x, y)

    def notAttackingPieces(self):
    	ff = 0
    	for idx,piece in enumerate(self.chessLocator):
    		for idx2,piece2 in enumerate(self.chessLocator):
    			if idx < idx2:
    				if ((piece[0] == "k") or (piece[0] == "K")) and ((piece2[0] == "b") or (piece2[0] == "B")):
    					if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "k") or (piece[0] == "K")) and ((piece2[0] == "r") or (piece2[0] == "R")):
    					if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "k") or (piece[0] == "K")) and ((piece2[0] == "q") or (piece2[0] == "Q")):
    					if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "b") or (piece[0] == "B")) and ((piece2[0] == "k") or (piece2[0] == "K")) :
    					if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "b") or (piece[0] == "B")) and ((piece2[0] == "r") or (piece2[0] == "R")) :
    					if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "b") or (piece[0] == "B")) and ((piece2[0] == "q") or (piece2[0] == "Q")) :
    					if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "r") or (piece[0] == "R")) and ((piece2[0] == "k") or (piece2[0] == "K")):
    					if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "r") or (piece[0] == "R")) and ((piece2[0] == "b") or (piece2[0] == "B")):
    					if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "r") or (piece[0] == "R")) and ((piece2[0] == "q") or (piece2[0] == "Q")):
    					if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "q") or (piece[0] == "Q")) and ((piece2[0] == "k") or (piece2[0] == "K")):
    					if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "q") or (piece[0] == "Q")) and ((piece2[0] == "b") or (piece2[0] == "B")):
    					if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    				elif ((piece[0] == "q") or (piece[0] == "Q")) and ((piece2[0] == "r") or (piece2[0] == "R")):
    					if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
    						ff += 1
    	return ff

    def hillClimbing(self):
        # solve board using hillClimbing algorithm
        # move piece function
        def changePiece(board, locator, piece1, x, y):
            # change piece at chessBoard
            resLocator = locator.clone()
            resBoard = board.clone()
            # piece1 and piece2 are tuple of piece, row index, and column index
            w, x0, y0 = piece1
            # w unused
            # move piece on board
            temp = resBoard[x0][y0]
            resBoard[x0][y0] = resBoard[x][y]
            resBoard[x][y] = temp
            # update chessLocator
            i = locator.index(piece1)
            resLocator[i] = (w, x, y)
            return resBoard, resLocator
        # heuristic function
        def notAttackingPieces(chessLocator):
            ff = 0
            for idx,piece in enumerate(chessLocator):
                for idx2,piece2 in enumerate(chessLocator):
                    if idx < idx2:
                        if ((piece[0] == "k") or (piece[0] == "K")) and ((piece2[0] == "b") or (piece2[0] == "B")):
                            if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "k") or (piece[0] == "K")) and ((piece2[0] == "k") or (piece2[0] == "K")):
                            if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "k") or (piece[0] == "K")) and ((piece2[0] == "r") or (piece2[0] == "R")):
                            if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "k") or (piece[0] == "K")) and ((piece2[0] == "q") or (piece2[0] == "Q")):
                            if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "b") or (piece[0] == "B")) and ((piece2[0] == "k") or (piece2[0] == "K")) :
                            if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "b") or (piece[0] == "B")) and ((piece2[0] == "b") or (piece2[0] == "B")):
                            if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "b") or (piece[0] == "B")) and ((piece2[0] == "r") or (piece2[0] == "R")) :
                            if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "b") or (piece[0] == "B")) and ((piece2[0] == "q") or (piece2[0] == "Q")) :
                            if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "r") or (piece[0] == "R")) and ((piece2[0] == "k") or (piece2[0] == "K")):
                            if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "r") or (piece[0] == "R")) and ((piece2[0] == "r") or (piece2[0] == "R")):
                            if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "r") or (piece[0] == "R")) and ((piece2[0] == "b") or (piece2[0] == "B")):
                            if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "r") or (piece[0] == "R")) and ((piece2[0] == "q") or (piece2[0] == "Q")):
                            if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "q") or (piece[0] == "Q")) and ((piece2[0] == "k") or (piece2[0] == "K")):
                            if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "q") or (piece[0] == "Q")) and ((piece2[0] == "b") or (piece2[0] == "B")):
                            if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "q") or (piece[0] == "Q")) and ((piece2[0] == "r") or (piece2[0] == "R")):
                            if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
                        elif ((piece[0] == "q") or (piece[0] == "Q")) and ((piece2[0] == "q") or (piece2[0] == "Q")):
                            if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                                ff += 1
            return ff
        # mover function
        def mover(board, locator):
            # return alternative board and locator
            res = []
            for location in locator:
                checkSurrounding(board, location)
                piece, x, y = location
                # changePiece(board, locator, piece, x, y)

                newBoard = board.clone()
                newLocator = locator.clone()

        # recursive function
        def recHillClimbing(thisBoard, thisLocator):
            # return board with the smallest heuristic and its locator
            # make nextStates array
            nextStates = []
            nextStates += mover(thisBoard, thisLocator)
            # count heuristic value for state board and compare with every board in nextStates array
            vState = notAttackingPieces(thisBoard)
            vNextState = []
            for board, locator in nextStates:
                vNextStates += notAttackingPieces(locator)
            i = vNextStates.index(min(vNextStates))
            vNextState = vNextStates[i]
            if (vNextState >= vState):
                return self.chessBoard, self.chessLocator
            else
                recHillClimbing(nextStates[i])
        self.chessBoard, self.chessLocator = recHillClimbing(self.chessBoard, self.chessLocator).clone()



def main():
    # read fileInput
    fileInput = input(str("Which file you want to open? "))
    nyth = nything(fileInput)
    # set matrix
    nyth.randomize()
    # solve nyth
    print("1. hillClimbing")
    print("2. simulatedAnnealing")
    print("3. geneticAlgorithm")
    x = int(input("Which algorithm do you want to choose? "))
    while (x < 1) or (x > 3):
        print("input = 1, 2, 3")
        x = int(input("Which algorithm do you want to choose? "))
    for row in nyth.chessBoard:
        print(row)
    for tuple in nyth.chessLocator:
        print(tuple)

if __name__ == '__main__':
    main()
