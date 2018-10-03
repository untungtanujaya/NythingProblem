# Name : app.py
# Desc : read the txt file (fileInput), then make object nything.

import random
from copy import deepcopy
import math

# cek apakah kuda di x1,y1 menyerang kotak x2,y2
def checkKnight(x1,y1,x2,y2):
    if ((x2 == x1 + 2) and ((y2 == y1 -1) or (y2 == y1 + 1))) or (x2 == x1 - 2 and ((y2 == y1 - 1) or (y2 == y1 + 1))) or ((y2 == y1 + 2) and ((x2 == x1 -1) or (x2 == x1 + 1))) or ((y2 == y1 - 2) and ((x2 == x1 - 1) or (x2 == x1 + 1))):
    		return True

# cek apakah bishop di x1,y1 menyerang kotak x2,y2
def checkBishop(x1,y1,x2,y2):
	if (abs(x2-x1) == abs(y2-y1)):
		return True

# cek apakah rook di x1,y1 menyerang kotak x2,y2
def checkRook(x1,y1,x2,y2):
	if (x1 == x2) or (y1 == y2):
		return True

# cek apakah queen di x1,y1 menyerang kotak x2,y2
def checkQueen(x1,y1,x2,y2):
	return (checkRook(x1,y1,x2,y2) or checkBishop(x1,y1,x2,y2))

#target ff untuk bidak sejumlah n
def countTarget(n):
        return int((n*(n-1))/2)

#cek apakah koordinat i,j di board ada bidaknya atau tidak
def checkBoard(states,i,j):
    check = False
    for state in states:
        if (state[1] == i and state[2] == j):
            check = True
            break
    return check

# fitness function atau heuristik algo
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

# generate populasi untuk genetic algorithm
def generatePopulation(Obj,nParent):
    population = []
    for i in range(nParent):
        Obj.randomize()
        population.append(Obj.chessLocator)
    return population

# memilih 3 parent dari populasi yang memiliki ff paling besar
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

# crossover dengan baris dimana terjadi crossover ditentukan oleh baris mana yang menghasilkan fitness function yang lebih besar
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

# mutasi 
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

#fitness funtion untuk bidak yang berbeda jenis
def notAttackingSamePieces(chessLocator):
    ff = 0
    for idx,piece in enumerate(chessLocator):
        for idx2,piece2 in enumerate(chessLocator):
            if idx < idx2:
                if (piece[0] == "k") and (piece2[0] == "b") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif ((piece[0] == "k") and (piece2[0] == "k")):
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "k") and (piece2[0] == "r") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "k") and (piece2[0] == "q") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                if (piece[0] == "K") and (piece2[0] == "B") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif ((piece[0] == "K") and (piece2[0] == "K")):
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "K") and (piece2[0] == "R") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "K") and (piece2[0] == "Q") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "k") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "b"):
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "r")  :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "q") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "K") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "B"):
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "R")  :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "Q") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "k"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "r"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "b"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "q"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "K"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "R"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "B"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "Q"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "k"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "b"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "r"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "q"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "K"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "B"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "R"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "Q"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
    return ff

#fitness funtion untuk bidak yang berbeda jenis
def notAttackingDiffPieces(chessLocator):
    ff = 0
    for idx,piece in enumerate(chessLocator):
        for idx2,piece2 in enumerate(chessLocator):
            if idx < idx2:
                if (piece[0] == "k") and (piece2[0] == "B") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif ((piece[0] == "k") and (piece2[0] == "K")):
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "k") and (piece2[0] == "R") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "k") and (piece2[0] == "Q") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                if (piece[0] == "K") and (piece2[0] == "b") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif ((piece[0] == "K") and (piece2[0] == "k")):
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "K") and (piece2[0] == "r") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "K") and (piece2[0] == "q") :
                    if not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "K") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "B"):
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "R")  :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "b") and (piece2[0] == "Q") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "k") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "b"):
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "r")  :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "B") and (piece2[0] == "q") :
                    if not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "K"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "R"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "B"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "r") and (piece2[0] == "Q"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "k"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "r"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "b"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "R") and (piece2[0] == "q"):
                    if not(checkRook(piece[1],piece[2],piece2[1],piece2[2])) and not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "K"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "B"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "R"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "q") and (piece2[0] == "Q"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "k"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkKnight(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "b"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkBishop(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "r"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])) and not(checkRook(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
                elif (piece[0] == "Q") and (piece2[0] == "q"):
                    if not(checkQueen(piece[1],piece[2],piece2[1],piece2[2])):
                        ff += 1
    return ff

# menghitung ada berapa seharusnya bidak yang sama yang tidak saling serang
def countTargetSamePieces(state):
    w = 0
    b = 0
    for piece in state:
        if piece[0] == "k" or piece[0] == "b" or piece[0] == "r" or piece[0] == "q":
            w += 1
        else:
            b += 1
    targetw = int(w*(w-1)/2)
    targetb = int(b*(b-1)/2)
    return targetw+targetb

# menghitung ada berapa seharusnya bidak yang sama yang tidak saling serang
def countTargetDiffPieces(state):
    return countTarget(len(state)) - countTargetSamePieces(state)



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
        #iterasi setiap bidak, pindahkan ke kotak yang nilai hcurrent paling besar
        while not(done) and (n != 70):
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
            #saat terjadi minimum lokal, random lagi susunan bidak
            elif(n % 2 == 1):
                self.randomize()
                hcurrent = notAttackingPieces(self.chessLocator)

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
        X = deepcopy(self.chessLocator)
        Xi = deepcopy(X)

        # 2. Tahap Menghitung Nilai Heuristik Pertama dengan nama 'E' berdasarkan slide
        E = countTarget(len(X)) - notAttackingPieces(X)

        # init change-able suhu
        chanSuhu = suhu
        while (chanSuhu > 1):
            # 3. Tahap Menghitung Jumlah Kemungkinan Pergerakan untuk Seluruh Bidak
        
            # 4. Tahap Menghitung Nilai Heuristik Kedua dengan nama 'Ei' berdasarkan slide
            NomorAcak = random.randint(0,len(Xi)-1)
            hcurrent = 9999
            for i in range(8):
                    for j in range(8):
                        if not(checkBoard(Xi,i,j)):
                            state = deepcopy(Xi)
                            state[NomorAcak] = Xi[NomorAcak][0],i,j
                            if hcurrent > countTarget(len(state)) - notAttackingPieces(state):
                                hcurrent = countTarget(len(state)) - notAttackingPieces(state)
                                Xi = deepcopy(state)
                                self.setChessBoard(Xi)
            Ei = hcurrent
            # 5. Membandingkan Nilai Heuristik Satu Sama Lain
            if (E <= Ei):
                E = Ei
                X = deepcopy(Xi)
            else:   # Menggunakan Peluang Konstan (dapat diganti dengan Boltzmann atau Pengurangan)
                if (PeluangAcak() < PeluangBoltzmann(E, Ei, chanSuhu)):
                    X = deepcopy(Xi)
                    E = Ei
            chanSuhu -= pendinginan
        self.setChessBoard(X)

    def geneticAlgorithm(self,batas):
        # solve using geneticAlgorithm
        # generate population
        population = generatePopulation(self,4)
        done = False
        result = []
        n = 0
        # saat belum optimal dan iterasi belum mencapai batas
        while not(done) and (n != batas):
            n+=1
            # pilih 3 parent yang ff nya paling besar
            best3Parents = selectedParent(population)
            # do crossover
            childs = crossOver(best3Parents,len(self.chessLocator))
            # mutasi setiap anak
            for child in childs:
                mutation(child,len(self.chessLocator))
            population = childs
            for child in childs:
                if (notAttackingPieces(child) == countTarget(len(self.chessLocator))):
                    result = child
                    done = True
                    self.setChessBoard(result)
                    break

# main
def main():
    # read fileInput
    fileInput = input(str("Which file you want to open? : "))
    nyth = nything(fileInput)
    # set matrix

    # solve nyth
    print("\n1. Hill Climbing")
    print("2. Simulated Annealing")
    print("3. Genetic Algorithm")
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
        suhu = int(input("Masukkan Suhu : "))
        pendingin = float(input("Masukkan pendingin : "))
        nyth.simulatedAnnealing(suhu, pendingin)
    else:
        batas = int(input("Masukkan batas iterasi : "))
        nyth.geneticAlgorithm(batas)
    # show chessBoard
    print("\nHASIL")
    nyth.printChessBoard()
    print((countTargetSamePieces(nyth.chessLocator) - notAttackingSamePieces(nyth.chessLocator)),(countTargetDiffPieces(nyth.chessLocator)- notAttackingDiffPieces(nyth.chessLocator)))

if __name__ == '__main__':
    main()