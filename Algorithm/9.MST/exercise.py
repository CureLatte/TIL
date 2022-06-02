# MST 연습장
# Minimum Spanning Tree

import sys
from collections import deque
import heapq


def main():
    input = sys.stdin.readline
    m, n = map(int, input().split())

    graph = [[] for _ in range(m+1)]

    for a in range(n):
        n1, n2, value = map(int,input().split())
        graph[n1].append([value, n2])
        graph[n2].append([value, n1])

    visited = [0] * (m+1)

    node_list = [(0, 1)]

    all_cost = 0

    while node_list:
        cost, node = heapq.heappop(node_list)
        if visited[node] == 1:
            continue
        all_cost += cost
        visited[node] = 1
        for n_cost, n_num in graph[node]:
            if visited[n_num] == 0:
                heapq.heappush(node_list, (n_cost, n_num))
        # print(' node_list : ', node_list)
        # print('visited: ', visited)

    print(all_cost)


if __name__ == '__main__':
    main()