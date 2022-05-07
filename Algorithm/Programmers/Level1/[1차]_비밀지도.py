# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for index in range(n):
        row = format(arr1[index] | arr2[index], 'b')
        while len(row) != n:
            row = '0' + row
        row = row.replace('0', ' ')
        row = row.replace('1', '#')

        answer.append(row)
    return answer