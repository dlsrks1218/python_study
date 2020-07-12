from typing import List, Dict

graph = {
    'A' : {'B': 1, 'C': 2, 'F': 4},
    'B' : {'D': 2, 'E': 1},
    'C' : {'D': 2},
    'D' : {'G': 1, 'K': 2},
    'E' : {'H': 1},
    'F' : {'G': 3},
    'G' : {'H': 1, 'I': 2, 'J': 3},
    'H' : {'J': 1, 'K': 2},
    'I' : {'J': 2},
    'J' : {},
    'K' : {}
}

def dfs_paths(graph: Dict, start: str, goal: str) -> List:
    stack = [(start, [start])]
    paths = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            paths.append(path)
        else:
            # for m in set(graph[n].keys()) - set(path):
            for m in set(graph[n].keys()):    
                stack.append((m, path + [m]))

    return paths

def get_cost_of_paths(paths: List) -> List:
    result = []
    for path in paths:
        cost = 0
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        result.append(cost)
    return result

if __name__ == '__main__':
    """
    * src -> dest로 가는 모든 경우의 수와 그에 대한 비용 구하기
    """
    paths = dfs_paths(graph, 'A', 'E')
    print(paths)

    costs = get_cost_of_paths(paths)
    print(costs)