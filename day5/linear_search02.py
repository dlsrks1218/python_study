from typing import Any

def linear_search(lst: list, val: Any) -> int:
    i = 0
    앞선 while 루프보다 빠름(while 루프에서 체크할 조건이 두개 이므로)
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    # for i in range(len(lst)-1, -1, -1):
    #     if lst[i] == val:
    #         return i

    return -1

if __name__ == '__main__':
    print(linear_search([2, 5, 1, -3], -3))