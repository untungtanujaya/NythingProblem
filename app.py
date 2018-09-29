# Name : app.py
# Desc : read the txt file (fileInput), then make object nything.

import random

def checkKnight(x1,y1,x2,y2):
    if ((x2 == x1 + 2) and ((y2 == y1 -1) or (y2 == y1 + 1))) or (x2 == x1 - 2 and ((y2 == y1 - 1) or (y2 == y1 + 1))) or ((y2 == y1 + 2) and ((x2 == x1 -1) or (x2 == x1 + 1))) or ((y2 == y1 - 2) and ((x2 == x1 - 1) or (x2 == x1 + 1))):
    		return True

def checkBishop(x1,y1,x2,y2):
	if (abs(x2-x1) == abs(y2-y1)):
		return True

def checkRook(x1,y1,x2,y2):
	if (x1 == x2) or (y1 == y2):
		return True

def checkQueen(x1,y1,x2,y2):
	return (checkRook(x1,y1,x2,y2) or checkBishop(x1,y1,x2,y2))

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

    def setChessBoard(self, input):
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
        for i in range(len(input)):
            piece = input[i][0]
            r = input[i][1]
            c = input[i][2]
            self.chessBoard[r][c] = piece
            self.chessLocator.append((piece, r, c))

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
            r = random.randint(0,7) # index 0 - 7
            c = random.randint(0,7)
            self.chessBoard[r][c] = piece
            self.chessLocator.append((piece, r, c))

    def changePiece(self, piece1, piece2):
        # change piece at chessBoard
        # piece1 and piece2 are tuple of piece, row index, and column index
        x, r1, c1 = piece1
        y, r2, c2 = piece2
        # x and y are unused

        # move piece on board
        temp = self.chessBoard[r1][c1]
        self.chessBoard[r1][c1] = self.chessBoard[r2][c2]
        self.chessBoard[r2][c2] = temp

    def hillClimbing(self):
        # solve using hillClimbing, return local maximum (make another attribute called res)
        for el in self.chessLocator:
            # start hill climbing
            current = el
            found = False
            while not found:
                neighbor = self.findHighestValueSucc(current)
                if self.hValue(neighbor) <= self.hValue(current):
                    found = True
                self.changePiece(current,neighbor)
                # change locator
                current = neighbors

    def hValue(self, piece):
        # return height value of x position
        return 0

    def findHighestValueSucc(self, piece):
        # find highest h value of neighbors
        # return position of neighbors (piece are dot ('.'))
        return ('.', 0, 0)

    def simulatedAnnealing(self):
        # solve using simulatedAnnealing
        print(2)

    def geneticAlgorithm(self):
        # solve using geneticAlgorithm
        population = generatePopulation(self,4)
        done = False
        result = []
        while not(done):
        	best3Parents = selectedParent(population)
        	childs = crossOver(best3Parents,len(self.chessLocator))
        	for child in childs:
        		mutation(child,len(self.chessLocator))
        	population = childs
        	for child in childs:
        		if (notAttackingPieces(child) == countTarget(len(self.chessLocator))):
        			result = child
        			done = True
        			break
        print(result)
       	self.setChessBoard(result)
        for i in range(8):
            for j in range(8):
                print(self.chessBoard[i][j], end=' ')
            print()

       
def countTarget(n):
    	return int((n*(n-1))/2)

def notAttackingPieces(chessLocator):
    ff = 0
    for idx,piece in enumerate(chessLocator):
        for idx2,piece2 in enumerate(chessLocator):
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
    
def generatePopulation(Obj,nParent):
    population = []
    for i in range(nParent):
        population.append(Obj.chessLocator)
        Obj.randomize()
    return population

def selectedParent(population):
    best3Parents = []
    for i in range(3):              #select 3 best Parents
        idxMax = 0
        for j in range (1, len(population)):
            if (notAttackingPieces(population[j]) > notAttackingPieces(population[idxMax])):
                idxMax = j

        best3Parents.append (population[idxMax])
        population.pop (idxMax)

    return best3Parents

def crossOver(population, totalPieces):
    child1 = []
    child2 = []
    child3 = []
    child4 = []

    separator1 = random.randint(0, totalPieces-1)
    for i in range(0,separator1):
        child1.append (population[0][i])
        child2.append (population[1][i])
    for i in range(separator1, totalPieces):
        child1.append (population[1][i])
        child2.append (population[0][i])

    separator2 = random.randint(0, totalPieces-1)
    for i in range(0,separator2):
        child3.append (population[1][i])
        child4.append (population[2][i])
    for i in range(separator2, totalPieces):
        child3.append (population[2][i])
        child4.append (population[1][i])

    return [child1, child2, child3, child4]

def mutation(chessLocator, totalPieces):
    idx = random.randint (0, totalPieces-1)
    while True:
        r = random.randint(0, 7)
        c = random.randint(0, 7)
        unique = True       #check if the mutation new position != other pieces position
        i = 0
        while (i<totalPieces) and (unique):
            if (r == chessLocator[i][1]) and (c == chessLocator[i][2]):
                unique = False
            else:
                i+=1
        if (unique):
            break
    temp = list(chessLocator[idx])
    temp[1] = r
    temp[2] = c
    chessLocator[idx] = tuple(temp)



# main
def main():
    # read fileInput
    fileInput = input(str("Which file you want to open? "))
    nyth = nything(fileInput)

    # set matrix
    nyth.randomize()
    nyth.printAttr()

    # solve nyth
    print("1. hillClimbing")
    print("2. simulatedAnnealing")
    print("3. geneticAlgorithm")
    x = int(input("Which algorithm do you want to choose? "))
    while (x < 1) or (x > 3):
        print("input = 1, 2, 3")
        x = int(input("Which algorithm do you want to choose? "))
    if x == 1:
        nyth.hillClimbing()
    elif x == 2:
        nyth.simulatedAnnealing()
    else:
        nyth.geneticAlgorithm()

    # # show chessBoard
    # for row in nyth.chessBoard:
    #     print(row)

if __name__ == '__main__':
    main()
