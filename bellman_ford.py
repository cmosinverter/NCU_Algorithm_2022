adj = [(1, 2, 6), (1, 4, 3), (2, 4, 4), (4, 2, 2), (2, 3, 2),
       (4, 5, 5), (4, 3, 3), (5, 2, 1), (3, 5, 1), (5, 3, -5)] #(u, v, weight) u -> v
n = 5 #number of nodes
inf = float("inf")
D = [inf]*(n+1) #DP table
D[1] = 0

for i in range(n-1):
    for i in range(len(adj)):
        u, v, wei = adj[i]
        if D[u] + wei < D[v]:
            D[v] = D[u] + wei
    print(D[1:])

for i in range(len(adj)):
    u, v, wei = adj[i]
    if D[u] + wei < D[v]:
        D[v] = D[u] + wei
print('第n次: ', D[1:])
