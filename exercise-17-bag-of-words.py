import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + np.abs(ai - bi)
    return sum

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            row_i = data[i]
            row_j = data[j]
            if (i == j):
                dist[i,j] = np.inf
            else:
                dist[i,j] = distance(row_i, row_j)

    #print(dist)
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
#print(len(data))
