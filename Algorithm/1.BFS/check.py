import sys

# sys.stdin = open('input.txt', 'r')

map_size = int(input())

graph = []
for i in range(map_size):
    a = list(map(int, input().split()))
    graph.append(a)


# dfs 함수
def dfs(x, y):
    # 범위를 벗어나면 종료
    if x >= map_size or y >= map_size or x <= -1 or y <= -1:
        return False
    if graph[x][y] == '#':
        return False
    # 현재 방문한 노드
    if graph[x][y] != -1:
        move_point = graph[x][y]
        graph[x][y] = '#'
        if dfs(x + move_point, y):
            return True
        if dfs(x, y + move_point):
            return True
        return False
    else:
        return True

# 노드 움직이기
if dfs(0, 0) == True:
    print("HaruHaru")
else:
    print("Hing")
