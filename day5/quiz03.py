from typing import List

graph = { 
    "집": {"미용실":5, "슈퍼마켓":10, "학원":9}, 
    "미용실": {"집":5, "슈퍼마켓": 3, "은행":11}, 
    "슈퍼마켓": {"집":10, "미용실":3, "레스토랑":3, "은행":10, "학원":7}, 
    "학원": {"집":9, "슈퍼마켓":7, "커피숍":8}, 
    "은행": {"미용실":11, "슈퍼마켓":10, "커피숍":5}, 
    "레스토랑": {"슈퍼마켓":3, "커피숍":3}, 
    "커피숍": {"레스토랑":3, "은행":5, "학원":8} 
}

def get_paths(start: str, goal: str) -> List[str]:
    """start에서 goal까지 가는 모든 경로 구하기

    Args:
        start (str): 시작 노드
        goal (str): 목적지 노드

    Returns:
        List[str]: 시작에서 목적지 노드까지 가는 모든 경로
    """
    # (현재 노드, 현재 까지 거친 경로)로 이루어진 튜플
    stack = [(start, [start])]
    paths = []

    while stack:
        current_node, path = stack.pop()
        # 순회중 현재 노드가 목적지와 같으면 이때껏 방문한 경로를 결과에 추가
        if current_node == goal:
            paths.append(path)
        else:
            # 현재 노드에서 갈 수 있는 곳들 중 방문한(path) 곳은 제외
            to_visit = set(graph[current_node].keys()) - set(path)
            for next_node in to_visit:
                stack.append((next_node, path + [next_node]))
    return paths


def get_cost_of_paths(paths: List[str]) -> List[int]:
    """get_paths(start, goal)를 통해 구한 모든 경로에서 거리(비용)를 구함
    Args:
        paths (List[str]): start에서 goal로 가는 모든 경로

    Returns:
        List[int]: 각 경로 별 사용된 코스트(거리)
    """
    result = []

    for path in paths:
        cost = 0
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        result.append(cost)
    return result


if __name__ == '__main__':
    for key, val in graph.items():
        if key == '집':
            continue
        paths = get_paths('집', key)
        costs = get_cost_of_paths(paths)

        # for path, cost in zip(paths, costs):
        #     print(path, cost)
            
        min_cost_index = costs.index(min(costs))
        print('='*50)
        print('<{}>에서 <{}> 까지의 최단 경로'.format(paths[min_cost_index][0], paths[min_cost_index][-1]))
        print('최단 경로 : {}\n비용 : {}'.format(paths[min_cost_index], min(costs)))

""" '집', '커피숍' 결과
['집', '슈퍼마켓', '레스토랑', '커피숍'] 16
['집', '슈퍼마켓', '학원', '커피숍'] 25
['집', '슈퍼마켓', '미용실', '은행', '커피숍'] 29
['집', '슈퍼마켓', '은행', '커피숍'] 25
['집', '학원', '슈퍼마켓', '레스토랑', '커피숍'] 22
['집', '학원', '슈퍼마켓', '미용실', '은행', '커피숍'] 35
['집', '학원', '슈퍼마켓', '은행', '커피숍'] 31
['집', '학원', '커피숍'] 17
['집', '미용실', '슈퍼마켓', '레스토랑', '커피숍'] 14
['집', '미용실', '슈퍼마켓', '학원', '커피숍'] 23
['집', '미용실', '슈퍼마켓', '은행', '커피숍'] 23
['집', '미용실', '은행', '슈퍼마켓', '레스토랑', '커피숍'] 32
['집', '미용실', '은행', '슈퍼마켓', '학원', '커피숍'] 41
['집', '미용실', '은행', '커피숍'] 21
최단 경로 : ['집', '미용실', '슈퍼마켓', '레스토랑', '커피숍'], 비용 : 14
"""

""" '집' '슈퍼마켓' 결과
['집', '슈퍼마켓'] 10
['집', '미용실', '슈퍼마켓'] 8
['집', '미용실', '은행', '슈퍼마켓'] 26
['집', '미용실', '은행', '커피숍', '레스토랑', '슈퍼마켓'] 27
['집', '미용실', '은행', '커피숍', '학원', '슈퍼마켓'] 36
['집', '학원', '슈퍼마켓'] 16
['집', '학원', '커피숍', '은행', '슈퍼마켓'] 32
['집', '학원', '커피숍', '은행', '미용실', '슈퍼마켓'] 36
['집', '학원', '커피숍', '레스토랑', '슈퍼마켓'] 23
최단 경로 : ['집', '미용실', '슈퍼마켓'], 비용 : 8
"""