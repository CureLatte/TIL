def solution(rows, columns, queries):
    answer = []
    cnt = 0
    array = []
    for row in range(rows):
        row = []
        for column in range(columns):
            cnt += 1
            row.append(cnt)
        array.append(row)

    for case in queries:
        start_row = case[0] - 1
        start_col = case[1] - 1
        end_row = case[2] - 1
        end_col = case[3] - 1

        row_cnt = end_row - start_row
        col_cnt = end_col - start_col

        q = [array[start_row][start_col]]
        min_value = array[start_row][start_col]

        # 오른쪽 이동
        for i in range(col_cnt):
            newtarget = q.pop()
            target = array[start_row][start_col + i + 1]
            q.append(target)
            if min_value > target:
                min_value = target
            array[start_row][start_col + i + 1] = newtarget

        # 아래 이동
        for i in range(row_cnt):
            newtarget = q.pop()
            target = array[start_row + i + 1][end_col]
            q.append(target)
            if min_value > target:
                min_value = target
            array[start_row + i + 1][end_col] = newtarget

        # 왼쪽 이동
        for i in range(col_cnt):
            newtarget = q.pop()
            target = array[end_row][end_col - i - 1]
            q.append(target)
            if min_value > target:
                min_value = target
            array[end_row][end_col - i - 1] = newtarget
        # 위로 이동
        for i in range(row_cnt - 1):
            newtarget = q.pop()
            target = array[end_row - i - 1][start_col]
            q.append(target)
            if min_value > target:
                min_value = target
            array[end_row - i - 1][start_col] = newtarget
        array[start_row][start_col] = q.pop()

        answer.append(min_value)

    return answer