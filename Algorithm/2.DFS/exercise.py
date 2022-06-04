import sys
input = sys.stdin.readline
m = int(input())
n = int(input())

graph = [[0] * (m+1) for _ in range(m+1) ]

for _ in range(n):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

visited = []


def dfs(computer):
    global visited
    if computer in visited:
        return
    visited.append(computer)
    for idx, i in enumerate(graph[computer]):
        if i == 1:
            dfs(idx)


dfs(1)
print(len(visited) -1 )
