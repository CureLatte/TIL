# 이진탐색 연습장
# 외우기 코드!

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort(reverse=True)
# print(tree)
split_tree = 0
e = tree[0]
s = 0
answer = 0
cut = 0

while True:

    if s >= e:
        if split_tree < M:
            cut -= 1
        break
    split_tree = 0
    cut = (s + e) // 2
    # print(s, e)
    for each_tree in tree:
        if each_tree <= cut:
            break
        split_tree += each_tree - cut
    # print('split: ', split_tree, cut)

    if split_tree < M:
        e = cut
        continue
    elif split_tree == M:
        break
    else:
        s = cut + 1
        continue


print(str(cut))

