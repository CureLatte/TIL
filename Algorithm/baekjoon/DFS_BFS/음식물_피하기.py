import time
from collections import deque

# my_file = open('input.txt')
row_cnt, col_cnt, all_count = map(int, input().split())


graph = []
left_target = []
answer = []

for i in range(row_cnt):
    graph.append([0]*col_cnt)

for i in range(all_count):
    row, col = map(int,  input().split())
    left_target.append((row-1, col-1))
    graph[row-1][col-1] = 1


d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]

while len(left_target) != 0:
    stack = deque([left_target.pop()])
    visited = []

    while len(stack) != 0:
        curr_pos = stack.pop()
        if curr_pos in visited:
            continue
        visited.append(curr_pos)
        curr_row, curr_col = curr_pos
        for i in range(4):
            next_row = curr_row + d_row[i]
            next_col = curr_col + d_col[i]
            if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt and graph[next_row][next_col] == 1 and (next_row, next_col) not in visited:
                stack.append((next_row, next_col))
    answer.append(len(visited))
    left_target = list(set(left_target) - set(visited))


print(max(answer))





