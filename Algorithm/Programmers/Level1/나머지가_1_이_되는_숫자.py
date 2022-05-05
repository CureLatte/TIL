def solution(n):
    for a in range(2, n):
        if (n-1) % a == 0:
            return a
