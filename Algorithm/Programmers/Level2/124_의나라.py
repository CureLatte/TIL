from itertools import product


def solution(n):
    answer = ''
    target = ['1', '2', '4']
    i = 1
    while True:
        n -= 3**i
        if n <= 0:
            n += 3**i
            break
        else:
            i += 1
    n -= 1
    for count in range(i):
        index = n % 3
        answer = target[index] + answer
        n = n//3

    return answer


def main():
    testcase = []

    n = 1
    result = '1'
    testcase.append([n, result])

    n = 2
    result = '2'
    testcase.append([n, result])

    n = 3
    result = '4'
    testcase.append([n, result])

    n = 4
    result = '11'
    testcase.append([n, result])

    n = 12
    result = '44'
    testcase.append([n, result])

    n = 13
    result = '111'
    testcase.append([n, result])

    for index, test in enumerate(testcase):
        print('*****************')
        print(index + 1, '번째')
        print('input: ', test[0])
        print('--Print--')
        result = solution(test[0])
        print('--result--')
        if test[1] == result:
            print(' Success!')
        else:
            print(' Fail!')


if __name__ == '__main__':
    main()