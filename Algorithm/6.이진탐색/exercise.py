# 이진탐색 연습장
# 외우기 코드!

import sys
from collections import deque


def solution(num_list, start, end):
    target = num_list[start: end+1]
    if len(target) % 2 == 0:
        return print(0)

    mid = len(target)//2
    for idx in range(mid):
        if target[idx] != target[-idx]:
            return print(0)
    return print(1)


def main():
    # sys.stdin = open('input.txt', 'r')

    n = int(input())
    num_list = list(map(int, input().split()))

    m = int(sys.stdin.readline())
    for _ in range(m):
        start, end = list(map(int, input().split()))
        solution(num_list, start-1, end-1)


if __name__ == '__main__':
    main()