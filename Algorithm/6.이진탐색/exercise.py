# 이진탐색 연습장
# 외우기 코드!

import sys
from collections import deque


def search(nums, st, en, target):
    # 함수 종료 조건
    if st == en:
        # 맞 았을때
        if nums[st] == target:
            print(1)
        # 맞지 않았을 때
        else:
            print(0)
        return
    mid = (st + en) // 2
    if nums[mid] < target:
        search(nums, mid + 1, en, target)
    else:
        search(nums, st, mid, target)


def solution(standard, check_list):
    ordered = sorted(standard)
    for check in check_list:
        search(ordered, 0, len(ordered)-1, check)


def main():
    # sys.stdin = open('input.txt', 'r')

    n = int(input())
    standard = list(map(int, input().split()))

    m = int(sys.stdin.readline())
    check_list = list(map(int, input().split()))

    solution(standard, check_list)


if __name__ == '__main__':
    main()