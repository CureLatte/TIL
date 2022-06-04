# 이진탐색 연습장
# 외우기 코드!

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

table = list(range(1, n+1))

temp = []


def search(deep, result, t):
    if deep == m:
        temp.append(result)
        return result
    v = []
    for i in t:
        v.append(i)
        search(deep + 1, result + str(i), sorted(list(set(t) - set(v))))


search(0, '', table)

for a in temp:
    for _ in a:
        print(int(_), end=' ')
    print('')
# print(len(temp))