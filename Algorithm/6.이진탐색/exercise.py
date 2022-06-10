# 이진탐색 연습장
# 외우기 코드!

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort(reverse=True)
# print(tree)
split_tree = 0


def check(s, e, arrays):
    global M, split_tree

    mid = (s + e) // 2
    # print(f'{s}, {mid}, {e}')

    if s == e:
        return s
    cut_high = arrays[mid]
    rest = 0
    for tree in arrays:
        if tree < cut_high:
            break
        rest += tree - cut_high
    # print('rest: ', rest)
    if rest < M:
        return check(mid + 1, e, arrays)
    elif rest > M:
        return check(s, mid, arrays)
    else:
        return mid


idx = check(0, len(tree)-1, tree)
# print(idx)

for cut in range(tree[idx], -1, -1):
    split_tree = 0

    for each_tree in tree[:idx+1]:
        split_tree += each_tree - cut
    # print(f'{cut}, {split_tree}')
    if split_tree >= M:
        print(cut)
        break
