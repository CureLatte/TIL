


# 그리디 : 최소 값을 쫒다보면 답이 나온다!

import sys
from collections import deque


def main():
    # sys.stdin = open('input.txt', 'r')

    n = int(input())

    delivery_cnt = []
    for a in range(n // 5 + 1):
        rest = (n - a * 5)
        if rest % 3 == 0:
            delivery_cnt.append(a + rest//3)
    if len(delivery_cnt) == 0:
        print(-1)
    else:
        print(min(delivery_cnt))


if __name__ == '__main__':
    main()