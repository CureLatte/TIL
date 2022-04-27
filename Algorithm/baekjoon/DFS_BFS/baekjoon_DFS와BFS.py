def main():
    input_ = input()
    node_cnt = int(input_.split(' ')[0])
    line_cnt = int(input_.split(' ')[1])
    start_node = input_.split(' ')[2]

    if node_cnt == 1:
        print(start_node)
        print(start_node)
        return 0
    graph = {}

    for cnt in range(line_cnt):
        nodeandlinkednode = input()
        targetNode = nodeandlinkednode.split(' ')[0]
        linkedNode = nodeandlinkednode.split(' ')[1]

        if targetNode not in graph:
            graph[targetNode] = [linkedNode]
        else:
            graph[targetNode].append(linkedNode)

        if linkedNode not in graph:
            graph[linkedNode] = [targetNode]
        else:
            graph[linkedNode].append(targetNode)

    for key, value in graph.items():
        value.sort(reverse=True)

    # DFS
    answer_dfs = ''
    stack = [start_node]
    dfs_visited = []
    while len(stack) != 0:
        current_node = stack.pop()
        if current_node in dfs_visited:
            continue
        else:
            dfs_visited.append(current_node)
        answer_dfs += current_node + ' '
        for linked_node in graph[current_node]:
            if linked_node not in dfs_visited:
                stack.append(linked_node)

    # BFS

    for key, value in graph.items():
        value.sort(reverse=False)

    answer_bfs = ''
    queue = [start_node]
    temp_q = []
    bfs_visited = []
    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node in bfs_visited:
            continue
        else:
            bfs_visited.append(current_node)
        answer_bfs += current_node + ' '
        for linked_node in graph[current_node]:
            if linked_node not in bfs_visited and linked_node not in temp_q:
                temp_q.append(linked_node)

        if len(queue) == 0:
            queue = sorted(temp_q)
            temp_q = []

    print(answer_dfs[:-1])
    print(answer_bfs[:-1])


if __name__ == '__main__':
    main()