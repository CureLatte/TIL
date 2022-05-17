import heapq


def solution(operations):
    answer = []
    min_temp = []
    max_temp = []

    for operate in operations:

        if operate[0] == 'I':
            value = int(operate.split()[1])
            min_temp.append(value)
            max_temp.append(-value)

        elif operate[0] == 'D' and len(min_temp) >= 1 and len(max_temp) >= 1:
            if operate.split()[1] == "1":
                heapq.heapify(max_temp)
                x_value_max = heapq.heappop(max_temp)
                min_temp.remove(-x_value_max)
            elif operate.split()[1] == '-1':
                heapq.heapify(min_temp)
                x_value_min = heapq.heappop(min_temp)
                max_temp.remove(-x_value_min)
    if len(min_temp) >= 2:
        heapq.heapify(min_temp)
        heapq.heapify(max_temp)
        answer.append(-heapq.heappop(max_temp))
        answer.append(heapq.heappop(min_temp))
    elif len(min_temp) == 0:
        answer = [0, 0]
    return answer

def main():
    testcase = []
    test = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    result = [0, 0]
    testcase.append([test, result])

    for test in testcase:
        expect = solution(test[0])
        if expect == test[1]:
            print('Success')
        else:
            print('Fail')


if __name__ == "__main__":
    main()
