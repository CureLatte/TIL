import sys

# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

case = {}

for i in range(m):
    case[i+1] = [a for a in range(1, n+1)]

temp = []

def bt(index, result):
    if index == m+1:
        temp.append(result)
        return result
    index_cases = case[index]
    for index_case in index_cases:
        if str(index_case) not in result:
            bt(index+1, result + str(index_case) + ' ')

bt(1, '')
for a in temp:
    print(a[:-1])

