import heapq
from collections import deque


def solution(jobs):
    # 시간 순으로 정렬
    jobs.sort()
    # count : 실행한 갯수
    # last : 마지막으로 끝난 시각
    count, last = 0, -1

    # wait 요청 시간이 지났지만 처리되지 않는 일들
    wait = []

    # time : 절대 시간
    time = jobs[0][0]
    length = len(jobs)
    answer = 0

    # 리스트에 있는 모든 일이 마칠 때까지
    while count < length:
        # jobs 를 순회하면서
        for s, t in jobs:
            # 앞의 일의 시작 시간 과 현재 시간 사이에 요청이 있다면
            if last < s <= time:
                # wait 목록에 추가
                heapq.heappush(wait, (t, s))
        # 만약 wait할 목록이 있다면
        if len(wait) > 0:
            # last = 시작 시간
            last = time
            # wait 에서 최소값 뽑기
            term, start = heapq.heappop(wait)
            # 진행한 일 뽑기
            count += 1
            # 경과 시간 이후
            time += term
            # 경과시간 더해주기
            answer += (time - start)

        else:
            time += 1

    return answer // length


def main():
    testcase = []
    test = [[0, 3], [1, 9], [2, 6]]
    result = 9
    testcase.append([test, result])

    for test in testcase:
        expect = solution(test[0])
        if expect == test[1]:
            print('Success')
        else:
            print('Fail')


if __name__ == "__main__":
    main()
