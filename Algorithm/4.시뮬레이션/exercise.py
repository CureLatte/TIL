# 시뮬레이션
#

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

nr, nc, s_d = map(int, input().split())

graph = []

for a in range(N):
    graph.append(list(map(int, input().split())))


d_row = [-1, 0, 1, 0]
d_col = [0, -1, 0, 1]
cnt = 0

queue = deque([nr, nc, s_d])
flag = 0
back = 0

def dfs(v, d):
    global cnt, flag, back
    row, col = v

    if graph[row][col] == 0:
        cnt += 1
        graph[row][col] = cnt
        for _ in range(4):
            if back == 1:
                d = (d + 3) % 4

            d = (d + 1) % 4
            new_row = row + d_row[d]
            new_col = col + d_col[d]
            if 0 <= new_row <= N-1 and 0 <= new_col <= M-1:
                if graph[new_row][new_col] == 0:
                    dfs([new_row, new_col], d)

            if _ == 3:
                back = 1

                return


dfs([nr, nc], s_d)

for a in graph:
    print(a)

print(cnt)


