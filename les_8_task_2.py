# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

b_draw_graph = False            # если установить в True - в отдельном окне будет отрисован граф
                                # предварительно нужно установить пакеты networkx и matplotlib, если они не установлены
if b_draw_graph:
    import networkx as nx
    import matplotlib.pyplot as plt

# Матрица смежности исследуемого ориентированного графа

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

# Реализация алгоритма Дейкстры

def dijkstra(graph, start):
    length = len(graph)                 # длина графа (число вершин)
    is_visited = [False] * length       # посещённые вершины 0, 1, 2...
    cost = [float('inf')] * length      # стоимость путей до вершин 0, 1, 2... из вершины start

    shortest_way = {}                   # словарь "вершина: список промежуточных точек на кратчайшем пути к вершине
    cost[start] = 0                     # начальная стоимость пути из вершины start (в саму себя) равна 0
    min_cost = 0                        # минимальная стоимость
    begin = start                       # начальная вершина

    for i in range(length):             # формирование словаря промежуточных точек на кратчайшем пути к вершине
        shortest_way.update({i: []})    # "вершина: пустой список"

    while min_cost < float('inf'):      # пока не останется недоступных вершин или все не будут обойдены
        is_visited[start] = True        # начальную вершину будем пропускать, далее start может изменить своё значение

        for i, vertex in enumerate(graph[start]):       # все вершины в строке с индексом start (в т.ч. при изменении)

            if vertex != 0 and not is_visited[i]:       # доступная (vertex != 0) и непосещённая вершина
                if cost[i] > vertex + cost[start]:      # при 1-м обходе cost[i] = inf, cost[start (начального)] = 0
                    cost[i] = vertex + cost[start]      # начальная стоимость соответствует весу данной вершины
                    if len(shortest_way[start]) > 0:
                        shortest_way[i].clear()
                        shortest_way[i].extend(shortest_way[start])
                    shortest_way[i].append(start)

        min_cost = float('inf')                         # после 1-го и других обходов в поисках кратчайшего пути
                                                        # потенциально можно завершить поиск, но надо проверить,
                                                        # нет ли более короткого или доступного пути (см. ниже)

        # проходимся по всем строкам матрицы, при этом строку с индексом start пропустим (is_visited = True)
        # ищем непосещённую вершину с минимальной стоимостью не равной inf, чтобы её сделать стартовой и повторить цикл

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:    # при этом строку с индексом start пропустим (is_visited)
                min_cost = cost[i]                          # минимальная стоимость непосещённой вершины
                start = i                                   # далее будем смотреть растояния до других вершин из этой,
                                                            # т.е. в строке с индексом данной вершины - повтор цикла.

    # добавление конечных пунктов назначения к кратчайшим путям до доступных вершин, в т.ч. начальной (самих себя)
    for i in range(length):
        if i == begin or len(shortest_way[i]) > 0:
            shortest_way[i].append(i)

    return [cost, shortest_way]


print('\nМатрица смежности ориентированного графа:\n')      # Печать матрицы смежности
for i in range(7):
    print(*g[i])
print('')

try:
    start_vertex = int(input('Введите номер вершины, из которой найти кратчайшие пути до других вершин (от 0 до 7): '))
    if start_vertex < 0:
        start_vertex = 0
    elif start_vertex > 7:
        start_vertex = 7
except:
    start_vertex = 0

print(f'Будут определяться кратчайшие пути из {start_vertex}-й вершины к другим вершинам\n')

distance = dijkstra(g, start_vertex)
points_dict = distance[1].copy()
distance.pop(1)
distance = distance[0].copy()

print(f'Вершина    Кратчайший путь из {start_vertex}-й       Полный маршрут       ')
print(f'--------------------------------------------------------------')

for i in range(len(g)):
    if len(points_dict[i]) > 0:
        s = '-'.join(str(points_dict[i]).split(', '))[1:-1]
    else:
        s = "Нет пути"
    print(f"{i:^7}    {distance[i]:^22}    {s:^20}")

# Отрисовка графа (при b_draw_graph = True - см. выше)

if b_draw_graph:

    print('\nИсточник (с кодом для отрисовки графа): Мюллер Дж. П., Массарон Л. Алгоритмы для чайников: Пер. с англ. -'
      ' СПб: Диалектика, 2019. - С. 228-232')

    graph_dict = {}
    node_dict = {}
    length = len(g)         # длина графа (число вершин)

    for i in range(length):
        graph_dict.update({str(i):{}})
        for j in range(length):
            if g[i][j] != 0:
                graph_dict[str(i)].update({str(j):g[i][j]})

    Graph = nx.DiGraph()

    for node in graph_dict:
        Graph.add_nodes_from(node)
        for edge, weight in graph_dict[node].items():
            Graph.add_edge(node, edge, weight=weight)

    offset = 0.125 / 2

    pos = {'0': [0.00, 0.50], '1': [0.25, 0.75 - offset], '2': [0.25, 0.25 + offset], '3': [0.75, 0.75], '4': [0.75, 0.25],
           '5': [1.25, 0.75 - offset], '6': [1.25, 0.25 + offset], '7': [1.50, 0.50]}

    labels = nx.get_edge_attributes(Graph, 'weight')
    nx.draw(Graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels, label_pos=0.2)
    nx.draw_networkx(Graph, pos)
    plt.show()

# Конец отрисовки графа

