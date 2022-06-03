"""
플로이드 연습장

1. 아이디어
 - 모든점 -> 모든점 : 플로이드
 - 비용배열 INF 초기화
 - 간선 비용 대입
 - 거쳐서 비용이 줄어들경우, 갱신(for문 3번)
 
2. 시간 복잡도
 - 플로이드 : O(V^3)
 - 1e6 가능
 
3. 변수
 - 비용 배열, int[][]
"""

import sys
from collections import deque
import heapq

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
rs =  [[]]

index_map = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    input_list = list(map(int, input().split()))
    rs.append(input_list)

print(index_map)


