__author__ = 'Andres'

def addpossibleneighbours(r, c):
    possibleNeighbours = []
    for x in range(r - 1, r + 2):
        for y in range(c - 1, c +2):
            if x >= 0 and y >= 0:
                possibleNeighbours.append((x,y))
    possibleNeighbours.remove((r, c))
    return possibleNeighbours

print addpossibleneighbours(0, 2)

def count_neighbours(grid, row, col):
    possibleNeighbours = addpossibleneighbours(row, col)
    Neighbours = 0
    for x in possibleNeighbours:
        try:
            if grid[x[0]][x[1]] == 1:
                Neighbours += 1
        except:
            print''
    return Neighbours

print count_neighbours(((1, 1, 1),
                        (1, 1, 1),
                        (1, 1, 1),), 0, 2) == 3, "Dense corner"
