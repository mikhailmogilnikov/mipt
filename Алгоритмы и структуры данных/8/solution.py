import itertools

graph = {
    1: {2: 10, 3: 15, 4: 20},
    2: {1: 10, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 4: 30},
    4: {1: 20, 2: 25, 3: 30},
}

start = 3
vertices = [v for v in graph.keys() if v != start]

min_cost = float("inf")
optimal_path = None

for perm in itertools.permutations(vertices):
    path = (start,) + perm + (start,)
    cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
    if cost < min_cost:
        min_cost = cost
        optimal_path = path

print("Минимальная стоимость:", min_cost)
print("Оптимальный маршрут:", optimal_path)
