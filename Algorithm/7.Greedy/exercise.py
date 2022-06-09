# 그리디 : 최소 값을 쫒다보면 답이 나온다!

import sys
from collections import deque


input = sys.stdin.readline

N = int(input())

array = []

negative_array = []

last_array=[]

for a in range(N):
    value = int(input())
    if value >0:
        array.append(value)
    else :
        negative_array.append(value)

array.sort(reverse=True)
negative_array.sort()


def sum_array(arrays):
    global last_array

    if len(arrays) == 0:
        return []
    new_array = []
    last = 0
    for idx in range(len(arrays) - 1):
        if arrays[idx] == '#':
            continue
        comp = arrays[idx] * arrays[idx + 1]
        temp_sum = arrays[idx] + arrays[idx + 1]

        if comp > temp_sum:
            new_array.append(comp)
            arrays[idx + 1] = '#'
        else:
            new_array.append(arrays[idx])

    if arrays[-1] != '#':
        last_array.append(arrays[-1])
    return new_array


a = sum_array(array)
b = sum_array(negative_array)


print(sum(a) + sum(b))
