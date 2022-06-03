# 투포인터 연습장

import sys


def main():
    # sys.stdin = open('input.txt', 'r')
    # input = sys.stdin.readline

    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    len_list = []
    check_sum = 0
    start_idx = 0

    for idx in range(len(num_list)):
        check_sum += num_list[idx]
        # print('check_num(first) : ', check_sum)
        if check_sum >= m:
            while check_sum >= m:
                # print('check_sum: ', check_sum)
                # print('start_idx : ' , start_idx)
                # print('idx: ', idx)
                len_list.append(idx - start_idx + 1)

                check_sum -= num_list[start_idx]
                start_idx += 1

        if check_sum < m:
            continue
    # print('len_list: ', len_list)
    if len(len_list) == 0:
        print(0)
    else:
        print(min(len_list))


if __name__ == '__main__':
    main()
