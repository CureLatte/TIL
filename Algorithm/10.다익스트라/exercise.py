# 다익스트라 연습장
# Minimum Spanning Tree

import sys
from collections import deque
import heapq


def main():
    input = sys.stdin.readline
    INF = sys.maxsize

    n, e = map(int, input().split())
    k = int(input())

    edge = [[] for _ in range(n + 1)]
    dist = [INF] * (n + 1)

    for _ in range(e):
        u, v, w = map(int, input().split())
        edge[u].append([w, v])

    heap = [[0, k]]
    dist[k] = 0

    while heap:
        ew, ev = heapq.heappop(heap)
        if dist[ev] != ew:
            continue
        for nw, nv in edge[ev]:
            if dist[nv] > ew + nw:
                dist[nv] = ew + nw
                heapq.heappush(heap, [dist[nv], nv])

    for i in range(1, n + 1):
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])


if __name__ == '__main__':
    main()
