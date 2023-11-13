def generateDeck(s):
    deck = []
    for i in range(s):  
        deck.append([1]) # s kártyához hozzáadunk egy 1-est
        for j in range(s-1):
            deck[i].append((j+1)+(i*(s-1))+1) #1-el kezdődőekhez növekvő sorrendben a maradék számot
    for i in range(2, s+1): # i = 0, 1, 2
        for j in range(0, s-1): # j = 0, 1, 2
            deck.append([i]) # s-1 kártyához hozzáadjuk i-t, (2-től s-ig)
            for k in range(0, s-1):
                deck[-1].append(s + (s-1)*k + ((i-2)*k+j) % (s-1) + 1)
                #shiftelgetünk jobbra 
    print(s)
    i = 0
    while i < len(deck):
        print(str(i+1) + " - " + str(deck[i]))
        i += 1
    print()
def WRONGgenerateDeckWRONG(s):
    #with s = 5, cards 2 and 9 do not have a common element
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

        
with open('./dobble_generator/input.txt', 'r') as f:
    input = f.readline()
    while input:
        try:
            generateDeck(int(input))
        except ValueError:
            print(input, end="")
            print("invalid\n")
        input = f.readline()