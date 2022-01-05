import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for _ in range(t):
    h, w = map(int, input().split())
    board = ["." * (w + 2)]
    board.extend(["." + input() + "." for _ in range(h)])
    board.extend(["." * (w + 2)])
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ans = float("inf")

    info_idx = 0
    prisoners = []
    for r in range(h + 2):
        for c in range(w + 2):
            if board[r][c] == "$":
                prisoners.append((r, c))

    def bfs(start_point):
        q = deque()
        cost_board = [[float("inf")] * (w + 2) for _ in range(h + 2)]
        q.append(start_point)
        cost_board[start_point[0]][start_point[1]] = 0
        while q:
            r, c = q.popleft()
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h + 2 and 0 <= nc < w + 2 and board[nr][nc] != "*":
                    if board[nr][nc] == "#" and cost_board[nr][nc] > cost_board[r][c] + 1:
                        cost_board[nr][nc] = cost_board[r][c] + 1
                        q.append((nr, nc))
                    elif board[nr][nc] != "#" and cost_board[nr][nc] > cost_board[r][c]:
                        cost_board[nr][nc] = cost_board[r][c]
                        q.append((nr, nc))

        return cost_board

    costs1 = bfs(prisoners[0])
    costs2 = bfs(prisoners[1])
    costs3 = bfs((0, 0))

    from pprint import pprint

    # pprint(board)
    pprint("costs1")
    pprint(costs1)
    pprint("costs2")
    pprint(costs2)
    pprint("costs3")
    pprint(costs3)

    for i in range(h + 2):
        for j in range(w + 2):
            cost = costs1[i][j] + costs2[i][j] + costs3[i][j]

            if board[i][j] == "#":
                cost -= 2
            ans = min(cost, ans)
    print(ans)
