# This program shows the DP method of multistage stage shortest path algorithm
import sys


def find_shortest_path(adj, n, stages):

    cost = [0 for i in range(n)]
    D = [0 for i in range(n)]
    path = [0 for i in range(stages)]

    cost[n-1] = 0

    for i in range(n-2, -1, -1):
        min_cost = sys.maxsize
        for j in range(i+1, n):
            if adj[i][j] + cost[j] < min_cost and adj[i][j] != 0:
                min_cost = adj[i][j] + cost[j]
                D[i] = j
            cost[i] = min_cost

    path[0] = 0
    path[stages-1] = n-1
    for i in range(1, stages-1):
        path[i] = D[path[i-1]]
    return path, cost[0]


stages = 4  # Number of stages
n = 8  # Number of nodes
s = [(0, 1, 1), (0, 2, 2), (0, 3, 5), (1, 4, 4), (1, 5, 11), (2, 4, 9),
     (2, 5, 5), (2, 6, 16), (3, 6, 2), (4, 7, 18), (5, 7, 13), (6, 7, 2)]  # (u, v, cost) u -> V
adj = [[0]*n for i in range(n)]

for item in s:
    u, v, dis = item
    adj[u][v] = dis

min_path = []
min_cost = 0
min_path, min_cost = find_shortest_path(adj, n, stages)
print(min_path, min_cost)
