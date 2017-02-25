class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#def solution(m):
    # o=len(m)
    # print o
    # for elem in range(o):
    #     for elem1 in range(o):
    #         l = []
    #         if m[elem][elem1] == 1:
    #             # below the element
    #             if (elem + 1) <= (o - 1):
    #                 if m[elem + 1][elem1] == 1:
    #                     l.append(str(elem + 1) + str(elem1))
    #             # above the element
    #             if (elem - 1) >= 0:
    #                 if m[elem - 1][elem1] == 1:
    #                     l.append(str(elem - 1) + str(elem1))
    #             # right of the element
    #             if (elem1 + 1) <= (o - 1):
    #                 if m[elem][elem1 + 1] == 1:
    #                     l.append(str(elem) + str(elem1 + 1))
    #             # left of the element
    #             if (elem1 - 1) >= 0:
    #                 if m[elem][elem1 - 1] == 1:
    #                     l.append(str(elem) + str(elem1 - 1))

#    return l
def solution(A):
    if not isValidMatrix(A):
        print "Provided matrix is not valid"
    searched_grids = []
    for row_num in xrange(A):
        for col_num in xrange(A[0]):
            if (row_num, col_num) in searched_grids:
                continue
            curr_country = A[row_num][col_num]
            gridsInCurrentCoutnry = Queue()
            gridsInCurrentCoutnry.enqueue((row_num, col_num))
            while !gridsInCurrentCoutnry.isEmpty():




def isValidMatrix(A):
    """Checks if matrix 'A' is valid or not"""
    if not A:
        return False;
    try:
        num_rows = len(A)
        num_col = len(A[0])
    except:
        print "Invalid Matrix: Cannot retrieve row and column number of the Matrix"
    if (1 > num_rows > 300000 or
                        1 > num_col > 300000):
        return False;
    # Check if the elements of the matrix are within the defined range
    for row in A:
        row_min = min(row)
        row_max = max(row)
        if (-1000000000 > row_min > 1000000000 or
                        -1000000000 > row_max > 1000000000):
            return False;
    return True





matrix = [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]]
print solution(matrix)
print sameCountriesGrid(matrix, (0,0))