# Name : app.py
# Desc : read the txt file (fileInput), then make object nything.

class nything:
    'class nything is a class that solve NythingProblem from fileInput'
    # attribute
    nWhiteKnight = 0
    nWhiteBishop = 0
    nWhiteRook = 0
    nWhiteQueen = 0
    nBlackKnight = 0
    nBlackBishop = 0
    nBlackRook = 0
    nBlackQueen = 0

    # method
    def __init__(self, fileInput):
        # put information in fileInput (in .txt) to attribute

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
                elif words[1] == "BISHOP":
                    self.nWhiteBishop = int(words[2])
                elif words[1] == "ROOK":
                    self.nWhiteRook = int(words[2])
                elif words[1] == "QUEEN":
                    self.nWhiteQueen = int(words[2])
            elif words[0] == "BLACK":
                if words[1] == "KNIGHT":
                    self.nBlackKnight = int(words[2])
                elif words[1] == "BISHOP":
                    self.nBlackBishop = int(words[2])
                elif words[1] == "ROOK":
                    self.nBlackRook = int(words[2])
                elif words[1] == "QUEEN":
                    self.nBlackQueen = int(words[2])
            # if it is not white nor black, it is ignored

    def solve(self):
        print("1. hillClimbing")
        print("2. simulatedAnnealing")
        print("3. geneticAlgorithm")
        x = int(input("Which algorithm do you want to choose? "))
        while (x < 1) or (x > 3):
            print("input = 1, 2, 3")
            x = int(input("Which algorithm do you want to choose? "))
        if x == 1:
            self.hillClimbing()
        elif x == 2:
            self.simulatedAnnealing()
        else:
            self.geneticAlgorithm()

    def hillClimbing(self):
        # solve using hillClimbing
        print(1)

    def simulatedAnnealing(self):
        # solve using simulatedAnnealing
        print(2)

    def geneticAlgorithm(self):
        # solve using geneticAlgorithm
        print(3)

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

fileInput = input(str("Which file you want to open? "))
nyth = nything(fileInput)
nyth.printAttr()
nyth.solve()



# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print ("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print ("Name : ", self.name,  ", Salary: ", self.salary)
#
# #This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# #This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print ("Total Employee %d" % Employee.empCount)
