import heapq


def minCost(loc):

    n = len(loc)
    graph = {i: {} for i in range(n)}  # adjacency_list

    i, j = 0, 1
    heap = [(0, 0)]
    vis = set()  # Using set to keep track of visited node
    res = 0

    while j < n and i < j:  # Prim's algorithm
        node1 = loc[i]
        node2 = loc[j]

        dis = abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
        graph[i][j] = dis
        graph[j][i] = dis
        j += 1
        if j == n:
            i += 1
            j = i + 1

    while heap:  # Use min heap to keep track of the smallest distance and peform BFS
        cur_cost, cur_node = heapq.heappop(heap)

        if cur_node in vis:
            continue

        vis.add(cur_node)
        res += cur_cost

        nei = graph[cur_node]
        for neigh in nei:
            if neigh not in vis:  # Not visited before
                new_cost = nei[neigh]

                heapq.heappush(heap, (new_cost, neigh))  # Push into the heap

    return res


T = int(input())
for i in range(T):
    k = int(input())
    loc = []
    for i in range(k):
        x, y = map(int, input().split())
        loc.append([x, y])

    print(minCost(loc))
