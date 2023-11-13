def pathToOutput(path):
    output = "S "
    i = len(path) - 1
    while i >= 0:
        output += path[i] + " "
        i -= 1
    output += "G"
    return output  

def createPath(mappedMaze, endPoint):
    row, col = endPoint
    length = mappedMaze[row][col]
    path = ""
    while length != 0: 
        if row + 1 < len(mappedMaze) and mappedMaze[row + 1][col] == length - 1:
            row = row + 1
            path += "U"
        if row - 1 >= 0 and mappedMaze[row - 1][col] == length - 1:
            row = row - 1
            path += "D"
        if col + 1 < len(mappedMaze[row]) and mappedMaze[row][col + 1] == length - 1:
            col = col + 1
            path += "L"
        if col - 1 >= 0 and mappedMaze[row][col - 1] == length - 1:
            col = col - 1
            path += "R"
        length = length - 1
    return pathToOutput(path)

def solveMaze(mazeInput):
    rows = item.split("\n")
    if rows[-1] == "":
        rows.pop()
    maze = []
    startingPoint = (0, 0)
    endPoint = (0, 0)
    for i in range(1, len(rows)):
        cells = rows[i].split(" ")
        row = []
        for j in range(len(cells)):
            if cells[j] == "#":
                row.append(-1)
            elif cells[j] == ".":
                row.append(0)
            elif cells[j] == "S":
                row.append(0)
                startingPoint = (i-1, j)
            else:
                row.append(0)
                endPoint = (i-1, j)
        maze.append(row)
    n = len(maze)
    m = len(maze[0])
    que = [(startingPoint[0], startingPoint[1], 0)]
    visited = [startingPoint]
    while len(que) != 0:
        row, col, length = que.pop(0)
        if not (row < 0 or col < 0 or row >= n or col >= m or maze[row][col] == -1):
            maze[row][col] = length
            if row == endPoint[0] and col == endPoint[1]:
                result = length
            if (row + 1, col) not in visited and row + 1 < n and maze[row + 1][col] != -1:
                que.append((row + 1, col, length + 1))
                visited.append((row + 1, col))
            if (row - 1, col) not in visited and row - 1 >= 0 and maze[row - 1][col] != -1:
                que.append((row - 1, col, length + 1))
                visited.append((row - 1, col))
            if (row, col + 1) not in visited and col + 1 < m and maze[row][col + 1] != -1:
                que.append((row, col + 1, length + 1))
                visited.append((row, col + 1))
            if (row, col - 1) not in visited and col - 1 >= 0 and maze[row][col - 1] != -1:
                que.append((row, col - 1, length + 1))
                visited.append((row, col - 1))
    path = createPath(maze, endPoint)
    print(rows[0])
    print(path)
    print()
    
with open('./input.txt', 'r') as f:
    input = f.read().split("\n\n")
for item in input:
    solveMaze(item)
            
