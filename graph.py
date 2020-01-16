graph = {
    "A": ["C", "E"],
    "B": ["F"],
    "C": ["B", "D", "F"],
    "D": [],
    "E": [],
    "F": []
}


def bfs(graph, start):
    explored = [start]
    queue = [start]
    while queue:
        current = queue.pop(0)
        print(current, end=" -> ")

        for neighbour in graph[current]:
            if neighbour not in explored:
                explored.append(neighbour)
                queue.append(neighbour)
    print("END")


bfs(graph, 'A')
