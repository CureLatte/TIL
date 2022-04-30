import time
graph = []
from collections import deque

my_file = open('input.txt')
row_cnt, col_cnt = map(int, my_file.readline().split()) # N:세로, M:가로
for row in range(row_cnt):
    graph.append(list(my_file.readline())[:-1])


# row_cnt, col_cnt = map(int, input().split(' '))
#
# for i in range(row_cnt):
#     graph.append(list(input()))
#

d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]

# BFS 찾기


queue = deque()
queue.append((0, 0))
temp_q = deque()
answer = 0
target = (row_cnt -1, col_cnt -1)

while len(queue) != 0:
    curr_pos = queue.popleft()
    curr_row, curr_col = curr_pos


    # 4방향으로 탙색
    for dir_cnt in range(4):
        next_row = curr_row + d_row[dir_cnt]
        next_col = curr_col + d_col[dir_cnt]
        if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt and graph[next_row][next_col] == '1':
            graph[next_row][next_col] = '2'
            temp_q.append((next_row, next_col))

    if len(queue) == 0:
        answer += 1
        queue = temp_q
        temp_q = deque()

    if target in queue:
        break

print(answer + 1)

