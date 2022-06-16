import heapq
import sys
adj = [[[1, 0], [2, 0], [3, 0]], [[4, 0], [5, 0], [6, 0]],
       [[4, 0], [5, 0], [6, 0]], [[4, 0], [5, 0], [6, 0]],
       [[7, 0], [8, 0], [9, 0]], [[7, 0], [8, 0], [9, 0]],
       [[7, 0], [8, 0], [9, 0]], [[10, 0]], [[10, 0]], [[10, 0]]]  # [node, weight]


def astar(adj):

    # Initialize the root node
    hq = []
    hn = min([i[1] for i in adj[0]])
    heapq.heappush(hq, (hn + 0, 0, 0))  # (fn, gn, node)

    fns = [sys.maxsize for i in range(11)]
    fns[0] = hn
    tmp = []
    # Best-First-Search
    while hq:
        fn, gn, node = heapq.heappop(hq)

        for ch in adj[node]:
            if ch[0] == 10:
                hn = 0
                gnn = ch[1] + gn
                heapq.heappush(hq, (hn + gnn, gnn, ch[0]))
                tmp.append((hn + gnn, gnn, ch[0]))
                if hn + gnn < fns[ch[0]]:
                    fns[ch[0]] = hn + gnn
                return fns
            else:
                hn = min([i[1] for i in adj[ch[0]]])
                gnn = ch[1] + gn
                heapq.heappush(hq, (hn + gnn, gnn, ch[0]))
                tmp.append((hn + gnn, gnn, ch[0]))
                if hn + gnn < fns[ch[0]]:
                    fns[ch[0]] = hn + gnn


T = int(input())


for i in range(T):

    for k in adj:
        for j in k:
            j[1] = int(input())
    S = int(input())

    res = astar(adj)
    if S == 1:
        print(res[0])
    if S == 2:
        print(min(res[1:4]))
    if S == 3:
        print(min(res[4:7]))
    if S == 4:
        print(min(res[7:10]))
    if S == 5:
        print(res[-1])
