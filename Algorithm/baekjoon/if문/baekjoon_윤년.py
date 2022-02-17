# 2753번 윤년

year = input()
year = int(year)

if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 400 == 0:
    print(1)
else:
    print(0)
    