
# 문제링크
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    all_month = [31, 29, 31, 30,
                 31, 30, 31, 31,
                 30, 31, 30, 31,
                 30, 31, 30, 31]
    data = 0

    for index in range(a - 1):
        data += all_month[index]
    data += b
    day_index = data % 7

    return days[day_index - 1]