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
        s = queue.pop(0)
        print(s, end=" -> ")

        for neighbour in graph[s]:
            if neighbour not in explored:
                explored.append(neighbour)
                queue.append(neighbour)
    print("END")


bfs(graph, 'A')
