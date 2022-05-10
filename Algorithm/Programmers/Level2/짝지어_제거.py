from collections import deque


def solution(s):
    q = deque([])
    for letter in s:
        if len(q) == 0:
            q.append(letter)
        else:
            last_letter = q.pop()
            if last_letter != letter:
                q.append(last_letter)
                q.append(letter)

    if len(q) == 0 :
        return 1
    else:
        return 0


def main():
    testcase = []
    s = 'baabaa'
    result = 1
    testcase.append([s, result])

    s = 'cdcd'
    result = 0
    testcase.append([s, result])

    s = 'aabbcdcfadfadsfacefewvfdddeeff'
    result = 0
    testcase.append([s, result])

    for index, test in enumerate(testcase):
        print(index + 1, '번째 CASE')
        result = solution(test[0])
        if result == test[1]:
            print('통과')
        else:
            print('실패')
        print('--------------------')


if __name__ == '__main__':
    main()
