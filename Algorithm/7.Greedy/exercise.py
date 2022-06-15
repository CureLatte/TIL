# 그리디 : 최소 값을 쫒다보면 답이 나온다!

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

money_list = list(map(int, input().split()))
#
# print(money_list)

sorted_money_list = sorted(money_list)

# print(sorted_money_list)
#
answer = 0

for idx in range(len(sorted_money_list)):
    answer += sum(sorted_money_list[:idx+1])

print(answer)