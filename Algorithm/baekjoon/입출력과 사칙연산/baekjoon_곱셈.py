# 2588번 곱셈

a = input()
b = input()
b=list(b)
b.reverse()
answer = 0
for i, k in enumerate(b):
    middle = int(a) * int(k)
    print(middle)
    answer += middle * 10 ** i
print(answer)
