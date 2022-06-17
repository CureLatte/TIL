# DP 연습장
# 이전 에 푼 결과가 도움이 된다!

import sys
from collections import deque


input = sys.stdin.readline

N = int(input())


INF = sys.maxsize
all_case = [[INF, INF]] * 41
all_case[0] = [1, 0]
all_case[1] = [0, 1]


def pibo(N):
    global all_case

    for a in range(2, N+1):
        prev_1 = all_case[a-1]
        prev_2 = all_case[a-2]

        all_case[a] = [prev_1[0] + prev_2[0], prev_1[1] + prev_2[1]]


check = []
for _ in range(N):
    n = int(input())
    check.append(n)

pibo(max(check))

for value in check:
    print(all_case[value][0], all_case[value][1])



