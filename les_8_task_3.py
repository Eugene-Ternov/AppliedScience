# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

# Функция поиска в глубину (граф задан списком смежности; 3-й параметр - лимит количества вершин,
# которые нужно посетить в общей сложности, < 1 - лимита нет)

def depth_first_search(graph, start, vertex_limit=0):
    length = len(graph)
    parent = [None for _ in range(length)]
    path = []
    vertex_cnt = 0

    stack = [start]

    while len(stack) > 0:
        current = stack.pop(-1)                         # извлечение из стека очередной вершины
        for vertex in graph[current]:
            if parent[vertex] is None and vertex != start and (vertex_limit < 1 or vertex_cnt < vertex_limit):
                parent[vertex] = current
                stack.append(vertex)
                vertex_cnt += 1
        path.append(str(parent[current]) + '-' + str(current))
    return path[1:]

# Список смежности невзвешенного ориентированного графа

g_lst = [[1, 3, 4], [2, 5], [1, 6], [1, 5, 7], [2, 6], [6], [5], [6]]

passed_vertex_lim = 0

for i in range(8):
    print(f'Старт: {i}, путь: {depth_first_search(g_lst, i, passed_vertex_lim)}')
