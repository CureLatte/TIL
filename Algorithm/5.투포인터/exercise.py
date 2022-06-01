# 투포인터 연습장

import sys
from collections import deque


def solution(check_list, m):
    answer = 0
    check_value = 0
    start_idx = 0
    for idx in range(len(check_list)):
        check_value += check_list[idx]
        if check_value > m:
            # chekc_value가 m보다 작아질떄가지 작은수 빼기
            while check_value > m:
                check_value -= check_list[start_idx]
                start_idx += 1

        elif check_value < m:
            continue

        if check_value == m:
            answer += 1

    print(answer)


def main():
    # sys.stdin = open('input.txt', 'r')

    n, m = map(int, input().split())
    check_list = list(map(int, input().split()))

    solution(check_list, m)


if __name__ == '__main__':
    main()