# DP 연습장
# 이전 에 푼 결과가 도움이 된다!

import sys
from collections import deque


def main():
    # sys.stdin = open('input.txt', 'r')

    n = int(input())

    case = [0] * (10**6 + 1)
    case[1] = 0
    case[2] = 1
    case[3] = 1
    for a in range(4, n + 1):
        temp = [case[a-1]]
        if a % 2 == 0:
            temp.append(case[a//2])
        if a % 3 == 0:
            temp.append(case[a//3])
        case[a] = min(temp) + 1
    print(case[n])


if __name__ == '__main__':
    main()