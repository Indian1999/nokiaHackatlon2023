class Matrix():
    def __init__(self, mtx):
        self.mtx = mtx
        self.rows = len(mtx)
        self.cols = len(mtx[0])
        
    def getElement(self, i, j):
        return self.mtx[i][j]
    
    def __add__(self, other):
        if self.cols == other.cols and self.rows == other.rows:
            outMtx = [[0 for i in range(self.cols)] for j in range(self.rows)]
            for i in range(len(self.mtx)):
                for j in range(len(self.mtx[0])):
                    outMtx[i][j] = self.getElement(i, j) + other.getElement(i, j)
            return Matrix(outMtx)
        else:
            raise Exception("InvalidMatrixSizeException")
        
    def __mul__(self, other):
        if self.cols == other.rows and self.rows == other.cols:
            outMtx = [[0 for i in range(other.cols)] for j in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    newValue = 0
                    for k in range(self.cols):
                        newValue += self.getElement(i, k) * other.getElement(k, j)
                    outMtx[i][j] = newValue
            return Matrix(outMtx)
        else:
            raise Exception("InvalidMatrixSizeException")
             
    def __str__(self):
        output = ""
        for row in self.mtx:
            for item in row:
                output += str(item) + " "
            output = output[:-1] #Cuts the space from the end of the string
            output += "\n"
        output = output[:-1] # Cuts the enter from the end of the string
        return output
      
with open('./input.txt', 'r') as f:
    input = f.read().split("\n\n")
 #['matrices', 'A\n2 1\n3 4', 'B\n1 0\n5 6', 'C\n2 1 0\n3 4 1\n1 0 2', 'D\n1 0 2\n5 6 4\n2 1 3', 'E\n1 2\n3 4\n5 6\n8 3', 'F\n1 2 3 4\n5 6 7 8', 'G\n1 2 3\n4 5 6\n7 8 9\n0 1 2', 'H\n1 2 3\n4 5 6\n7 8 9\n0 1 2', 'I\n1  2  3  4\n5  6  7  8\n9  10 11 12\n13 14 15 16', 'J\n16 15 14 13\n12 11 10 9\n8  7  6  5\n4  3  2  1', 'operations', 'A + B\nB + B + A\nC + D + D + C\nE * F + I * J\n']

mtxDict = {}
input.remove("matrices")
for matrix in input:
    if matrix == "operations":
        break
    rows = matrix.split("\n")
    mtx = []
    for i in range(1, len(rows)):
        mtx.append([int(x) for x in rows[i].split()])
    mtxDict[rows[0]] = Matrix(mtx)
operations = input[-1].split("\n") #['A + B', 'B + B + A', 'C + D + D + C', 'E * F + I * J']
operations.pop()

#E * F + I * J      i = 1
#temp1 + I * J      i = 1
#temp1 + I * J      i = 3
#temp1 + temp3      i = 2

for operation in operations:
    operationSplit = operation.split()
    i = 0
    while i < len(operationSplit):
        if operationSplit[i] == "*":
            mtxDict["temp" + str(i)] = mtxDict[operationSplit[i-1]] * mtxDict[operationSplit[i+1]]
            operationSplit[i] = "temp" + str(i)
            operationSplit.pop(i+1)
            operationSplit.pop(i-1)
            i -= 1
        i += 1
    i = 0
    while i < len(operationSplit):
        if operationSplit[i] == "+":
            mtxDict["temp" + str(i)] = mtxDict[operationSplit[i-1]] + mtxDict[operationSplit[i+1]]
            operationSplit[i] = "temp" + str(i)
            operationSplit.pop(i+1)
            operationSplit.pop(i-1)
            i -= 1
        i += 1
    print(operation)
    print(mtxDict[operationSplit[0]])
    print()
    
"""
newOperationList = []
for operation in operations:
    operationSplit = operation.split()
    i = 0
    while i < len(operationSplit):
        if operationSplit[i] == "*":
            mtxDict["mtx" + str(i)] = mtxDict[operationSplit[i-1]] * mtxDict[operationSplit[i+1]]
            
#E * F + I * J    i = 1
#temp + I * J     i = 1
#temp + I * J     i = 3
#temp + temp ááááá
for operation in operations:
    operationSplit = operation.split()
    i = 0
    while i < len(operationSplit):
        while operationSplit[i] == "*":
            mtxDict["temp"] = mtxDict[operationSplit[i-1]] * mtxDict[operationSplit[i+1]]
            operationSplit[i] = "temp"
            operationSplit.pop(i+1)
            operationSplit.pop(i-1)
        i += 1
"""
"""
for operation in operations:
    operationSplit = operation.split()
    operands = []
    operators = []
    for item in operationSplit:
        if item == "+" or item == "*":
            operators.append(item)
        else:
            operands.append(item)
    for operator in operators:
        if operator == "+":
            mtxDict["temp"] = mtxDict[operands[0]] + mtxDict[operands[1]]
            operands[1] = "temp"
        else:
            mtxDict["temp"] = mtxDict[operands[0]] * mtxDict[operands[1]]
            operands[1] = "temp"
        operands.pop(0)
    print(operation)
    print(mtxDict["temp"])
    print()
"""

"""
for key in mtxDict.keys():
    print(key)
    print(mtxDict[key])
    print()

myMatrix = Matrix([[1,2,3],[3,2,4],[1,2,1]])
myMatrix2 = Matrix([[0,5,2],[2,3,1],[3,2,4]])
print(myMatrix)
print()
print(myMatrix2)
print()
print(myMatrix + myMatrix2)
print()
myMatrix = Matrix([[2,3,1],[4,5,6]])
myMatrix2 = Matrix([[1,2], [1,1], [2,3]])
print(myMatrix * myMatrix2)
"""