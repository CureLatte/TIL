# 시뮬레이션
#

import sys
from collections import deque


def solution(n, target, wait_list):
    id_list = [(idx, priority) for idx, priority in enumerate(wait_list)]

    printer = deque(id_list)
    cnt = 0
    while printer:
        a = printer[0][1]
        if max(printer, key=lambda x: x[1])[1] == a:
            check = printer.popleft()
            cnt += 1
            if check[0] == target:
                print(cnt)
                break
        else:
            printer.rotate(-1)


def main():
    # sys.stdin = open('input.txt', 'r')

    case_cnt = int(input())

    all_case = []

    for _ in range(case_cnt):
        n, target = map(int, input().split())
        primary_list = list(map(int, sys.stdin.readline().split()))
        solution(n, target, primary_list)


if __name__ == '__main__':
    main()