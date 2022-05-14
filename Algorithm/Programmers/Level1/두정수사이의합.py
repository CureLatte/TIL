def solution(a, b):
    answer = 0
    if a > b :
        a,b = b,a
    for a in range(a,b+1):
        answer += a
    return answer