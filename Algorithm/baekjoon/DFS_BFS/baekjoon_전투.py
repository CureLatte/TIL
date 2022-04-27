def calculation_power(warrior_type):
    all_w_position = []

    # 모든 병사의 위치 찾기
    for x, row_ in enumerate(graph):
        for y, target in enumerate(row_):
            if target == warrior_type:
                all_w_position.append((x, y))

    answer = 0

    # 병사 포지션의 첫번째 부터 탐색
    for next_network in all_w_position:

        # 모든 병사 포지션이 사라지면 break
        if len(all_w_position) == 0:
            break
        # 새로 업데이트된 목록에 없다면 패스
        if next_network not in all_w_position:
            continue

        # 남은 포지션의 첫번재 인수 넣기
        stack = [next_network]

        # 방문 한곳 넣기
        visited = []
        while len(stack) != 0:
            curr_x, curr_y = stack.pop()
            if (curr_x, curr_y) in visited:
                continue
            visited.append((curr_x, curr_y))
            # 노트의 주변 확인
            # 아래 위치 확인
            if curr_x + 1 <= row and graph[curr_x + 1][curr_y] == warrior_type and (curr_x + 1, curr_y) not in visited:
                stack.append((curr_x + 1, curr_y))
            # 윗 방향 확인
            if curr_x - 1 >= 0 and graph[curr_x - 1][curr_y] == warrior_type and (curr_x - 1, curr_y) not in visited:
                stack.append((curr_x - 1, curr_y))

            # 오른쪽 방향 확인
            if curr_y + 1 <= col and graph[curr_x][curr_y + 1] == warrior_type and (curr_x, curr_y + 1) not in visited:
                stack.append((curr_x, curr_y + 1))

            # 왼족 방향 확인
            if curr_y - 1 >= 0 and graph[curr_x][curr_y - 1] == warrior_type and (curr_x, curr_y - 1) not in visited:
                stack.append((curr_x, curr_y - 1))

        # DFS 순회 끝 전투력 추가
        answer += len(visited) ** 2
        # 모든 병사 포지션 새로 고침
        all_w_position = list(set(all_w_position) - set(visited))
    return answer


# main 함수
input_data = input()

col = int(input_data.split(' ')[0]) - 1
row = int(input_data.split(' ')[1]) - 1
graph = []

for i in range(row + 1):
    a = input()
    graph.append(list(a))

# W 병사
print(calculation_power("W"))

# B 병사
print(calculation_power("B"))
