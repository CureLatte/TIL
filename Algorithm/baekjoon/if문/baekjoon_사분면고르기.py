# 14681번 사분면 고르기

x = input()
x = int(x)
y = input()
y = int(y)

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
    