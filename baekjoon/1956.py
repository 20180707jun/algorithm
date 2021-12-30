import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

v, e = map(int, input().split())
g = [[float("inf")] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a][b] = min(g[a][b], c)

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])
ans = float("inf")
for i in range(v + 1):
    ans = min(g[i][i], ans)

if ans != float("inf"):
    print(ans)
else:
    print(-1)
