def solution(s):
    if len(s) % 2 ==1:
        return s[(len(s)-1)//2]
    else:
        start = (len(s))//2
        return s[start-1:start+1]


def main():
    testcase = []
    s = 'abcde'
    result = 'c'
    testcase.append([s, result])

    s = 'qwer'
    result = 'we'
    testcase.append([s, result])

    for test in testcase:
        result = solution(test[0])
        if result == test[1]:
            print('통과')
        else:
            print('실패')


if __name__ == '__main__':
    main()
