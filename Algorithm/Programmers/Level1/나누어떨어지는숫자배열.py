def solution(arr, divisor):
    answer = []
    sorted_divisor = sorted(arr, reverse = False)
    for target in sorted_divisor:
        if target % divisor == 0:
            answer.append(target)
    if len(answer) ==0 :
        answer.append(-1)
    return answer