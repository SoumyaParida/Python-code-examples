#import itertools
#mylist=[1,2,3,4,5]
#newlist=list(itertools.combinations(mylist,2))
#o

def solution(A,k):
    items = a
    values = [(items[i], items[j]) for i in range(len(items)) for j in range(i + 1, len(items))]
    n = len(a)
    result = set()
    if ((1 <= k) and (k <= 1000000000)) and (5 <= n and n<= 100000):
        for test in values:
            if ((test[1] - test[0] == k) or (test[0] - test[1] == k)):
                result.add(test)
        if len(result) > 0:
            return len(result)
        else:
            return 0
    else:
        return 0
def solution1(A):
    sorted_array = sorted(A)
    K = 2
    if not ValidData(A, K):
        return
    # print sorted_array
    pair_elements = []
    for i, item in enumerate(sorted_array):
        # print sorted_array[i+1:]
        for next_item in sorted_array[i+1:]:
            if (abs(item - next_item) > K):
                break
            if (item + K == next_item) and ((next_item, item) not in pair_elements):
                pair_elements.append((item, next_item))
    # print pair_elements
    return len(pair_elements)

def ValidData(A, K):
    if len(A) < 5 or len(A) > 100000:
        return False
    if K < 1 or K > 1000000000:
        return False
    for item in A:
        if item > 2000000000:
            return False
    return True



a=[1,5,3]
print solution1(a,2)