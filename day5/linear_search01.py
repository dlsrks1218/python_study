from typing import Any

def linear_search(lst: list, val: Any) -> int:
    i = 0
    # 끝까지 가거나 값을 찾을때까지 반복
    while i != len(lst) and lst[i] != val:
        i += 1
    
    if i == len(lst):
        return -1
    else:
        return i

    # i = len(lst) - 1
    # while i != 0 and lst[i] != val:
    #     i -= 1
    # if i == -1:
    #     return -1
    # else:
    #     return i

if __name__ == '__main__':
    print(linear_search([2, 5, 1, -3], -3))