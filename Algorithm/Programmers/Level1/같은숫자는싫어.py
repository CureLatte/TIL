from collections import deque


def solution(arr):
    answer = ['a']

    for letter in arr:
        check = answer[-1]
        if check == letter:
            continue
        else:
            answer.append(letter)

    return answer[1:]