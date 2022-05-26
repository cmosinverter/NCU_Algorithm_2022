
import pandas as pd

inf = float("inf")
A = [[0, 3, inf, 7], [8, 0, 2, inf], [5, inf, 0, 1], [2, inf, inf, 0]] # adjacency matrix
n = 4 # number of nodes

for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    print(pd.DataFrame(A))
    print()
