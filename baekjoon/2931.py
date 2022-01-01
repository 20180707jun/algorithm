import sys

input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == "M":
            cor_m = (i, j)
        if board[i][j] == "Z":
            cor_z = (i, j)

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find_next_d(pre_d, pipe_type):
    if pre_d in [(0, 1), (0, -1)] and pipe_type == "-":
        return pre_d
    elif pre_d in [(1, 0), (-1, 0)] and pipe_type == "|":
        return pre_d
    elif pipe_type == "+":
        return pre_d
    elif pipe_type in ["1", "2", "3", "4"]:
        if pre_d == (1, 0):
            if pipe_type == "2":
                return (0, 1)
            elif pipe_type == "3":
                return (0, -1)
        elif pre_d == (-1, 0):
            if pipe_type == "1":
                return (0, 1)
            elif pipe_type == "4":
                return (0, -1)
        elif pre_d == (0, 1):
            if pipe_type == "3":
                return (-1, 0)
            elif pipe_type == "4":
                return (1, 0)
        elif pre_d == (0, -1):
            if pipe_type == "1":
                return (1, 0)
            elif pipe_type == "2":
                return (-1, 0)
    return None


pre_d_list = []
cor_list = []
pipe_type_list = []
for dr, dc in d:
    nr, nc = dr + cor_m[0], dc + cor_m[1]
    if (
        0 <= nr < R
        and 0 <= nc < C
        and board[nr][nc] in ["|", "-", "+", "1", "2", "3", "4"]
    ):
        pre_d_list.append((dr, dc))
        cor_list.append((nr, nc))
        pipe_type_list.append(board[nr][nc])
is_breaked = False
for i in range(len(pre_d_list)):
    pre_d = pre_d_list[i]
    cor = cor_list[i]
    pipe_type = pipe_type_list[i]
    while pipe_type not in [".", "Z"]:
        pre_d = find_next_d(pre_d, pipe_type)
        if pre_d == None:
            is_breaked = True
            break
        cor = (pre_d[0] + cor[0], pre_d[1] + cor[1])
        pipe_type = board[cor[0]][cor[1]]
    if is_breaked == False:
        break
ans_cor = cor
ans_pre_d = pre_d
for pipe_type in ["|", "-", "+", "1", "2", "3", "4"]:
    ans_pipe = pipe_type
    pre_d = ans_pre_d
    cor = ans_cor
    board[cor[0]][cor[1]] = pipe_type
    while pipe_type not in ["Z"]:
        pre_d = find_next_d(pre_d, pipe_type)
        if pre_d == None:
            break
        cor = (pre_d[0] + cor[0], pre_d[1] + cor[1])
        if not (0 <= cor[0] < R and 0 <= cor[1] < C):
            break
        pipe_type = board[cor[0]][cor[1]]

    if pipe_type == "Z":
        print(ans_cor[0] + 1, ans_cor[1] + 1, ans_pipe)
        break
