from typing import List, Dict

# graph = {
#     'A' : {'B': 1, 'C': 2, 'F': 4},
#     'B' : {'D': 2, 'E': 1},
#     'C' : {'D': 2},
#     'D' : {'G': 1, 'K': 2},
#     'E' : {'H': 1},
#     'F' : {'G': 3},
#     'G' : {'H': 1, 'I': 2, 'J': 3},
#     'H' : {'J': 1, 'K': 2},
#     'I' : {'J': 2},
#     'J' : {},
#     'K' : {}
# }

graph = { 
    "집": {"미용실":5, "슈퍼마켓":10, "학원":9}, 
    "미용실": {"집":5, "슈퍼마켓": 3, "은행":11}, 
    "슈퍼마켓": {"집":10, "미용실":3, "레스토랑":3, "은행":10, "학원":7}, 
    "학원": {"집":9, "슈퍼마켓":7, "커피숍":8}, 
    "은행": {"미용실":11, "슈퍼마켓":10, "커피숍":5}, 
    "레스토랑": {"슈퍼마켓":3, "커피숍":3}, 
    "커피숍": {"레스토랑":3, "은행":5, "학원":8} 
}

def dfs_paths(start: str, goal: str) -> List:
    stack = [(start, [start])]
    paths = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            paths.append(path)
        else:
            for m in set(graph[n].keys()) - set(path):
            # for m in set(graph[n].keys()):    
                stack.append((m, path + [m]))

    return paths

def get_cost_of_paths(paths: List) -> List:
    result = []
    for path in paths:
        cost = 0
        for i in range(len(path)-1):
            # print(graph[path[i]][path[i+1]])
            cost += graph[path[i]][path[i+1]]
        result.append(cost)
    return result

if __name__ == '__main__':
    """
    * src -> dest로 가는 모든 경우의 수와 그에 대한 비용 구하기
    """
    # paths = dfs_paths(graph, 'A', 'D')
    paths = dfs_paths('집', '은행')
    # print(paths)

    # for path in paths:
    #     print(path)
    # print('*'*30)
    costs = get_cost_of_paths(paths)
    # print(costs)
    min_cost_index = costs.index(min(costs))
    print('최단 경로 : {}, 비용 : {}'.format(paths[min_cost_index], min(costs)))