# Name : app.py
# Desc : read the txt file (fileInput), then make object nything.

import random
from copy import deepcopy
import math

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

def countTarget(n):
        return int((n*(n-1))/2)

def checkBoard(states,i,j):
    check = False
    for state in states:
        if (state[1] == i and state[2] == j):
            check = True
            break
    return check

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

def generatePopulation(Obj,nParent):
    population = []
    for i in range(nParent):
        Obj.randomize()
        population.append(Obj.chessLocator)
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
    currentff1 = 0
    currentff2 = 0
    currentff3 = 0
    currentff4 = 0

    for separator1 in range(totalPieces):
        for i in range(0,separator1):
            child1.append (population[0][i])
            child2.append (population[1][i])
        for i in range(separator1, totalPieces):
            child1.append (population[1][i])
            child2.append (population[0][i])
        if currentff1 < notAttackingPieces(child1):
            child1hasil = []
            currentff1 = notAttackingPieces(child1)
            child1hasil = deepcopy(child1)
        child1 = []
        if currentff2 < notAttackingPieces(child2):
            child2hasil = []
            currentff2 = notAttackingPieces(child2)
            child2hasil = deepcopy(child2)
        child2 = []
    for separator2 in range(totalPieces):
        for i in range(0,separator2):
            child3.append (population[1][i])
            child4.append (population[2][i])
        for i in range(separator2, totalPieces):
            child3.append (population[2][i])
            child4.append (population[1][i])
        if currentff3 < notAttackingPieces(child3):
            child3hasil = []
            currentff3 = notAttackingPieces(child3)
            child3hasil = deepcopy(child3)
        child3 = []
        if currentff4 < notAttackingPieces(child4):
            child4hasil = []
            currentff4 = notAttackingPieces(child4)
            child4hasil = deepcopy(child4)
        child4 = []
    return [child1hasil, child2hasil, child3hasil, child4hasil]

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

    def printChessBoard(self):
        for i in range(8):
            for j in range(8):
                print(self.chessBoard[i][j], end=' ')
            print()

    def printAttr(self):
        # print attribute
        print("\nWhiteKnight : " + str(self.nWhiteKnight))
        print("WhiteBishop : " + str(self.nWhiteBishop))
        print("WhiteRook : " + str(self.nWhiteRook))
        print("WhiteQueen : " + str(self.nWhiteQueen))
        print("BlackKnight : " + str(self.nBlackKnight))
        print("BlackBishop : " + str(self.nBlackBishop))
        print("BlackRook : " + str(self.nBlackRook))
        print("BlackQueen : " + str(self.nBlackQueen))
        print("List Bidak : ",self.chessPieces)
        print("\nSTATE AWAL")
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

    def hillClimbing(self):
        # solve board using hillClimbing algorithm
        hcurrent = notAttackingPieces(self.chessLocator)
        done = False
        n=0
        while not(done):
            n+=1
            for idx in range(len(self.chessLocator)):
                for i in range(8):
                    for j in range(8):
                        if not(checkBoard(self.chessLocator,i,j)):
                            state = deepcopy(self.chessLocator)
                            state[idx] = self.chessLocator[idx][0],i,j
                            if hcurrent < notAttackingPieces(state):
                                hcurrent = notAttackingPieces(state)
                                self.chessLocator = deepcopy(state)
                                self.setChessBoard(self.chessLocator)
            if (hcurrent == countTarget(len(self.chessLocator))):
                done = True
            elif(n % 2 == 0):
                self.randomize()
                hcurrent = notAttackingPieces(self.chessLocator)
        print("\niterasi : ",n)

    def hValue(self, board):
        # return height value of x position
        return 0

    def findHighestValueSucc(self, piece):
        # find highest h value of neighbors
        # return position of neighbors (piece are dot ('.'))
        return ('.', 0, 0)

    def matrixOfNextState(state):
    # Mengembalikan senarai yang berisi kumpulan state selanjutnya yang memungkinkan
        nextState = []  # Variabel untuk menyimpan state selanjutnya
        
        def isValid(Angka1, Angka2):
        # Periksa keabsahan koordinat di jangkauan
            return ((Angka1 >= 0) and (Angka1 <= 7) and (Angka2 >= 0) and (Angka2 <= 7))
        
        def isEmpty(state, row, col):
        # Mencari keberadaan suatu bidak di posisi row col
            Kosong = True
            for bidak in state:
                if ((state[bidak][1] == row) and (state[bidak][2] == col)):
                    Kosong = False
                    break
                    
            return Kosong
        
        def newStateExcept(state, bidakLama, bidakBaru):
        # Menjadikan suatu senarai yang berisi satu state, tapi membuang state yang ada di parameter
            stateBaru = [i for i in state if i != bidakLama] 
            stateBaru.append(bidakBaru)
            return stateBaru
        
        # BENTENG BERJALAN
        def Benteng(state, bidak):
        # Mengisi state yang memungkinkan si benteng untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            
            # Tahap Berjalan ke Kiri
            for col in range(Kol, 0):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('R', Brs, col) ))
                else:   # Ada penghalang, sehingga akhir dari perjalanan
                    break
            
            # Tahap Berjalan ke Kanan
            for col in range(Kol, 7):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('R', Brs, col) ))
                else:   # Ada penghalang
                    break
                    
            # Tahap Berjalan ke Atas
            for row in range(Brs, 0):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('R', row, Kol) ))
                else:   # Ada penghalang
                    break
            
            # Tahap Berjalan ke Bawah
            for row in range(Brs, 7):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('R', row, Kol) ))
                else:   # Ada penghalang
                    break
            
        # KUDA BERJALAN
        def Kuda(state, bidak):
        # Mengisi state yang memungkinkan si kuda untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            Gerak1 = [-2, 2]
            Gerak2 = [-1, 1]
            for i in range(0, 1):
                for j in range(0, 1):
                    Baris = Brs + Gerak1[i]
                    Kolom = Kol + Gerak2[j]
                    if (isValid(Baris, Kolom)):
                        if (isEmpty(state, Baris, Kolom)):
                            nextState.append(newStateExcept( state, bidak, ('K', Baris, Kolom) ))

        # MENTERI BERJALAN
        def Menteri(state, bidak):
        # Mengisi state yang memungkinkan si benteng untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            
            # Tahap Berjalan ke Kanan Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
                    
            # Tahap Berjalan ke Kanan Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
        # RATU BERJALAN
        def Ratu(state, bidak):
        # Mengisi state yang memungkinkan si ratu untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            
            # PERGERAKAN MENYERUPAI "BENTENG"
            # Tahap Berjalan ke Kiri
            for col in range(Kol, 0):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('Q', Brs, col) ))
                else:   # Ada penghalang, sehingga akhir dari perjalanan
                    break
            
            # Tahap Berjalan ke Kanan
            for col in range(Kol, 7):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('Q', Brs, col) ))
                else:   # Ada penghalang
                    break
                    
            # Tahap Berjalan ke Atas
            for row in range(Brs, 0):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('Q', row, Kol) ))
                else:   # Ada penghalang
                    break
            
            # Tahap Berjalan ke Bawah
            for row in range(Brs, 7):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('Q', row, Kol) ))
                else:   # Ada penghalang
                    break
            
            # PERGERAKAN MENYERUPAI "MENTERI"
            # Tahap Berjalan ke Kanan Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
                    
            # Tahap Berjalan ke Kanan Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
        # ALGORITME LOKAL
        for pieces in state:
            if (pieces[0] == 'R'):      # Memasukkan pergerakan Benteng
                Benteng(state, pieces)
            elif (pieces[0] == 'K'):    # Memasukkan pergerakan Kuda
                Kuda(state, pieces)
            elif (pieces[0] == 'B'):    # Memasukkan pergerakan Menteri
                Menteri(state, pieces)
            elif (pieces[0] == 'Q'):    # Memasukkan pergerakan Ratu
                Ratu(state, pieces)
            
        return nextState
    

    def simulatedAnnealing(self, suhu, pendinginan):
        # solve using simulatedAnnealing
        def PeluangKonstan():
        # Mengembalikan nilai peluang yang dipilih langsung (nilai boleh diubah selama berada di jangkauan 0.000...1 ~ 0.999...)
            return 0.1

        def PeluangMenurun(P, Temperature):
        # Mengembalikan niai peluang yang menurun secara perlahan
            return P * Temperature

        def PeluangBoltzmann(e, ei, suhu):
        # Mengembalikan nilai hasil dari distribusi Boltzmann
            return math.exp((ei - e) / suhu)

        def PeluangAcak():
        # Mengembalikan nilai peluang secara acak
            return random.random()
        
	# ALGORITME LOKAL
        # 1. Tahap Inisialisasi (penempatan bidak secara acak)
        X = self.chessLocator
        
        # 2. Tahap Menghitung Nilai Heuristik Pertama dengan nama 'E' berdasarkan slide
        E = 0
        for bidak in X:
            E += hValue(bidak)
        
        while (suhu > 1):
            # 3. Tahap Menghitung Jumlah Kemungkinan Pergerakan untuk Seluruh Bidak
            i = matrixOfNextState(X)  # MENUNGGU KABAR
            
            # 4. Tahap Menghitung Nilai Heuristik Kedua dengan nama 'Ei' berdasarkan slide
            Ei = 0
            NomorAcak = random.randint(0, len(i))
            for bidak in i[NomorAcak]:
                Ei += hValue(bidak)
                
            # 5. Membandingkan Nilai Heuristik Satu Sama Lain
            if (E <= Ei):
                E = Ei
                X = i[NomorAcak]
            else:   # Menggunakan Peluang Konstan (dapat diganti dengan Boltzmann atau Pengurangan)
                if (PeluangAcak() < PeluangKonstan()):
                    X = i[NomorAcak]
                    E = Ei
                    
            suhu *= pendinginan
            
        return X

    def geneticAlgorithm(self):
        # solve using geneticAlgorithm
        population = generatePopulation(self,4)
        done = False
        result = []
        n = 0
        while not(done):
            n+=1
            best3Parents = selectedParent(population)
            childs = crossOver(best3Parents,len(self.chessLocator))
            for child in childs:
                mutation(child,len(self.chessLocator))
            # print(childs)
            # print(len(self.chessLocator))
            population = childs
            for child in childs:
        		# print(notAttackingPieces(child))
                if n<30000:
                    if (notAttackingPieces(child) == countTarget(len(self.chessLocator))):
                        result = child
                        done = True
                        break
                elif n<40000:
                    if (notAttackingPieces(child) >= countTarget(len(self.chessLocator))-1):
                        result = child
                        done = True
                        break
                else:
                    if (notAttackingPieces(child) >= countTarget(len(self.chessLocator))-2):
                        result = child
                        done = True
                        break
       	self.setChessBoard(result)
        print("iterasi : ",n)

# main
def main():
    # read fileInput
    fileInput = input(str("Which file you want to open? "))
    nyth = nything(fileInput)
    # set matrix

    # solve nyth
    print("\n1. hillClimbing")
    print("2. simulatedAnnealing")
    print("3. geneticAlgorithm")
    x = int(input("\nWhich algorithm do you want to choose? "))
    while (x < 1) or (x > 3):
        print("input = 1, 2, 3")
        x = int(input("Which algorithm do you want to choose? "))
    if x == 1:
    	nyth.randomize()
    	nyth.printAttr()
    	nyth.hillClimbing()
    elif x == 2:
    	nyth.randomize()
    	nyth.printAttr()
    	nyth.simulatedAnnealing()
    else:
        nyth.geneticAlgorithm()
    # show chessBoard
    print("\nHASIL")
    nyth.printChessBoard()

if __name__ == '__main__':
    main()
