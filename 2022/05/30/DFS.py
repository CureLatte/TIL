import sys
from collections import deque


def dfs(node, visited, graph):
    if len(visited) == len(graph):
        return visited

    visited.append(node)
    if node not in graph:
        return visited
    temp = sorted(graph[node])
    for check in temp:
        if check not in visited:
            dfs(check, visited, graph)
    return visited


def bfs(start_node, graph):
    queue = deque([start_node])
    visited = [start_node]
    while len(queue) > 0:
        node = queue.popleft()
        if node not in graph:
            return visited
        temp = sorted(graph[node])
        for f in temp:
            if f not in visited:
                visited.append(f)
                queue.append(f)
    return visited


def main():
    # sys.stdin = open('input.txt', 'r')

    n, connect, start_node = map(int, input().split())

    graph = {}

    for i in range(connect):
        n1, n2 = map(int, input().split())
        if n1 not in graph:
            graph[n1] = [n2]
        else:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        else:
            graph[n2].append(n1)

    print(" ".join(str(a) for a in dfs(start_node, [], graph)))

    print(" ".join(str(a) for a in bfs(start_node, graph)))


if __name__ == '__main__':
    main()
