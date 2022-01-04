import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
total_min = float("inf")
total_max = -float("inf")
for i in range(n):
    for j in range(n):
        total_min = min(board[i][j], total_min)
        total_max = max(board[i][j], total_max)


def solution(n, board):
    s, e = 0, 200

    while s < e:
        mid = (s + e) // 2
        breaked = True
        for left in range(total_min, total_max + 1 - mid):
            breaked = False
            right = left + mid
            q = deque()
            q.append((0, 0, board[0][0], board[0][0]))
            visit = [[False] * n for _ in range(n)]
            visit[0][0] = True
            while q:
                r, c, mi, ma = q.popleft()
                if (r, c) == (n - 1, n - 1):
                    breaked = True
                    break
                for dr, dc in d:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < n and 0 <= nc < n:
                        new_mi = min(mi, board[nr][nc])
                        new_ma = max(ma, board[nr][nc])
                        if visit[nr][nc] == True:
                            continue
                        if new_ma > right or new_mi < left:
                            continue
                        q.append((nr, nc, new_mi, new_ma))
                        visit[nr][nc] = True
            if breaked:
                break

        if breaked:
            e = mid
        else:
            s = mid + 1

    return s


print(solution(n, board))
