import sys

with open("Day11.txt") as f:
    environment = [list(row) for row in f.read().split('\n')]


# def state(grid):
#     r, c = len(grid), len(grid[0])
#     newGrid = [[grid[i][j] for j in range(c)] for i in range(r)]
#     changeHappen = False
#     for i in range(r):
#         for j in range(c):
#             if grid[i][j] == '.':
#                 continue
#
#             adj = 0
#             adj += i and j and grid[i - 1][j - 1] == '#'
#             adj += i and grid[i - 1][j] == '#'
#             adj += i and j + 1 < c and grid[i - 1][j + 1] == '#'
#             adj += j and grid[i][j - 1] == '#'
#             adj += j + 1 < c and grid[i][j + 1] == '#'
#             adj += i + 1 < r and j and grid[i + 1][j - 1] == '#'
#             adj += i + 1 < r and grid[i + 1][j] == '#'
#             adj += i + 1 < r and j + 1 < c and grid[i + 1][j + 1] == '#'
#
#             if grid[i][j] == 'L' and adj == 0:
#                 changeHappen = True
#                 newGrid[i][j] = '#'
#             elif grid[i][j] == '#' and adj >= 4:
#                 changeHappen = True
#                 newGrid[i][j] = 'L'
#     return newGrid, changeHappen
#
#
# changeHappen = True
# while changeHappen:
#     data, changeHappen = state(data)
#
# total = 0
# for row in data:
#     total += row.count('#')
# print(total)

def warOfSpecies(environment):
    neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]  # Define neighbours
    rows = len(environment)  # Rows of the matix
    columns = len(environment[0])  # Columns of the matix
    rowlists = []  # Define a new matix

    for row in range(rows):  # Traverse the matrix
        rowlist = []
        for letter in environment[row]:
            rowlist.append(letter)
        rowlists.append(rowlist)  # Copy a matrix to record the intermediate state
        for column in range(columns):
            stateX = 0
            statedot = 0
            stateO = 0
            for neighbour in neighbours:  # Record neighbours' state
                neighbourpoint = (row + neighbour[0], column + neighbour[1])  # Neighbour point
                if 0 <= neighbourpoint[0] < rows and 0 <= neighbourpoint[
                    1] < columns:  # If neighbour point is in the matix
                    if environment[neighbourpoint[0]][neighbourpoint[1]] == "X":
                        stateX += 1
                    elif environment[neighbourpoint[0]][neighbourpoint[1]] == ".":
                        statedot += 1
                    elif environment[neighbourpoint[0]][neighbourpoint[1]] == "O":
                        stateO += 1
            if environment[row][column] == ".":  # Change the intermediate state matrix
                if stateX >= 2 or stateO >= 2:  # rule one
                    if stateX == stateO:
                        rowlist[column] = "."
                    elif stateX > stateO:
                        rowlist[column] = "X"
                    elif stateO > stateX:
                        rowlist[column] = "O"
            else:
                if stateX + stateO > 6:  # rule two
                    rowlist[column] = "."
                if environment[row][column] == "X":  # rule three and rule four
                    if stateX < 3 or stateX < stateO:
                        rowlist[column] = "."
                else:
                    if stateO < 3 or stateO < stateX:
                        rowlist[column] = "."
    for row in range(rows):  # Return result
        environment[row] = ''.join(rowlists[row])
    return environment