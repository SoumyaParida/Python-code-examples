def solution(A):
    """
    :param A: Country map grid
    :return: Total number of countries in the map
    """
    country_num = 0
    visited_grids = set([])
    for i in xrange(len(A)):
        for j in xrange(len(A[0])):
            if (i, j) not in visited_grids:
                visited_grids.update(getCurrentCountryGrids(A, (i, j)))
                country_num += 1
    return country_num


def getCurrentCountryGrids(A, grid):
    """
    Returns: All the grids that belongs to the current country
    """
    current_country = A[grid[0]][grid[1]]
    current_country_grids = set([grid])
    visited, queue = set(), [grid]
    print "quue",queue
    #print "quue",queue
    while queue:
        current_grid = queue.pop(0)
        print "current_grid",current_grid
        if current_grid not in visited:
            visited.add(current_grid)
            print "visited", visited
            neighbors = get4neighbors(A, current_grid[0], current_grid[1])
            print "neighbors",neighbors
            print "current_country",current_country
            for neighbor in neighbors:
                if A[neighbor[0]][neighbor[1]] == current_country and \
                                neighbor not in visited:
                    print "neighbor",neighbor
                    queue.append(neighbor)
                    current_country_grids.add(neighbor)
                    print "queue",queue
                    print "current_country_grids",current_country_grids
    return set(current_country_grids)


def get4neighbors(A, row, col):
    """
    :param A: Country map
    :param row: row number of the target grid
    :param col: column number of the target grid
    :return: neighboring four neighbor grids of the target grid
    """
    neighbor_grids = []
    if row > 0:
        neighbor_grids.append((row - 1, col))
    if row < len(A) - 1:
        neighbor_grids.append((row + 1, col))
    if col > 0:
        neighbor_grids.append((row, col - 1))
    if col < len(A[0]) - 1:
        neighbor_grids.append((row, col + 1))
    return neighbor_grids


def getEightNeighbors(A, row, col):
    """
    :param A: Country map
    :param row: row number of the target grid
    :param col: column number of the target grid
    :return: neighboring four neighbor grids of the target grid
    """
    neighbor_grids = []
    width = len(A[0])
    height = len(A)
    if row > 0:
        neighbor_grids.append((row - 1, col))
    if row < height - 1:
        neighbor_grids.append((row + 1, col))
    if col > 0:
        neighbor_grids.append((row, col - 1))
    if col < len(A[0]) - 1:
        neighbor_grids.append((row, col + 1))
    if (row > 0) and (col > 0):
        neighbor_grids.append((row - 1, col - 1))
    if (row > 0) and (col < width - 1):
        neighbor_grids.append((row - 1, col + 1))
    if (row < height - 1) and (col > 0):
        neighbor_grids.append((row + 1, col - 1))
    if (row < height - 1) and (col < width - 1):
        neighbor_grids.append((row + 1, col + 1))
    return neighbor_grids


matrix = [[2, 5, 3, 3],
          [2, 5, 5, 3],
          [1, 1, 7, 3],
          [1, 4, 8, 8]]

country_map = [[5, 4, 4],
               [4, 3, 4],
               [3, 2, 4],
               [2, 2, 2],
               [3, 3, 4],
               [1, 4, 4],
               [4, 1, 1]]

#print get4neighbors(matrix, 1, 1)
#print  getCurrentCountryGrids(matrix, (0, 3))
# print  getCurrentCountryGrids(matrix, (1, 1))
#print getEightNeighbors(matrix, 1, 1)

# print solution(matrix)
print solution(country_map)