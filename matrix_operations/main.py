with open('./input.txt', 'r') as f:
  input = f.read()

print(input)

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

                    
                
        