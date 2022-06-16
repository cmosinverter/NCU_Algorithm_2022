n, m = map(int, input().split())
inf = float("inf")
A = [[inf]*n for i in range(n)]

for i in range(n):
    A[i][i] = 0

for i in range(m):
    u, v, dis = input().split()
    u = ord(u) - 97
    v = ord(v) - 97
    dis = int(dis)

    A[u][v] = dis


# A = [[0, 3, inf, 7], [8, 0, 2, inf], [5, inf, 0, 1], [2, inf, inf, 0]]
# n = 4

for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])


for i in range(n):
    print(' '.join(map(str, A[i])))
