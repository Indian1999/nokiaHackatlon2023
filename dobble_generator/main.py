def generateDeck(s):
    k = s*s - s + 1
    finiteProjectionPlane = [[[] for i in range(s-1)] for j in range(s-1)]
    #Filling the rows:
    for i in range(1, 1 + (s - 1)): #1,2,3
        for j in range(s-1):
            finiteProjectionPlane[i-1][j].append(i)
    #Filling the columns:
    for i in range(s, s + (s - 1)): #4,5,6
        for j in range(s-1):
            finiteProjectionPlane[j][i - s].append(i)
    #Filling the diagonals:
    for diagonalDifference in range(1, s-1):
        startNum = (1 + diagonalDifference) * (s - 1) + 1
        for i in range(startNum, startNum + (s - 1)):
            x = i - startNum 
            for j in range(s-1):
                finiteProjectionPlane[j][x].append(i)
                x += diagonalDifference
                x %= (s-1)
    #Vanishing points:
    vanishingPoints = []
    for i in range(0, s):
        vanishingPoint = []
        for j in range(1, s):
            vanishingPoint.append(i * (s - 1) + j)
        vanishingPoint.append(k)
        vanishingPoints.append(vanishingPoint)
    print(s)
    for i in range(len(finiteProjectionPlane)):
        for j in range(len(finiteProjectionPlane[i])):
            print(str(i * (s - 1) + j + 1) + " - " + str(finiteProjectionPlane[i][j]))
    for i in range(len(vanishingPoints)):
        print(str(i+1+(s-1)**2) + " - " + str(vanishingPoints[i]))
    print()
    
        
with open('./input.txt', 'r') as f:
    input = f.readline()
    while input:
        try:
            generateDeck(int(input))
        except ValueError:
            print(input, end="")
            print("invalid\n")
        input = f.readline()