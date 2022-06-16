# author: Kevin Liu
# email: kevin95120@gmail.com
# date: 2022/6/16

from collections import deque


def puzzle(board, final):
    s = ''.join(str(d) for row in board for d in row)
    f = ''.join(str(d) for row in final for d in row)
    dq, seen = deque(), {s}
    dq.append((s, s.index('0')))
    height, width = len(board), len(board[0])
    while dq:
        for _ in range(len(dq)):
            t, i = dq.popleft()

            x, y = i // width, i % width
            for r, c in (x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1):
                if height > r >= 0 <= c < width:
                    ch = [d for d in t]

                    ch[i], ch[r * width + c] = ch[r * width + c], '0'
                    s = ''.join(ch)
                    if s not in seen:
                        seen.add(s)
                        x1 = list(s[0:3])
                        x2 = list(s[3:6])
                        x3 = list(s[6:9])
                        print(' '.join(x1))
                        print(' '.join(x2))
                        print(' '.join(x3))
                        if s == f:
                            return
                        dq.append((s, r * width + c))

    return



board = [[] for i in range(3)]
final = [[] for i in range(3)]
for i in range(3):
    board[i] = list(map(int, input().split()))
for i in range(3):
    final[i] = list(map(int, input().split()))

for i in range(3):
    print(' '.join(map(str, board[i])))


puzzle(board, final)

