# 11021번 A+B-7
import sys
test_cnt = input()
test_cnt = int(test_cnt)

for k in range(1,test_cnt+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{k}: {a + b}')