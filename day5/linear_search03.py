from typing import Any

def linear_search(lst: list, val: Any) -> int:
    # 센티널 설정 -> 1번 while루프 구현에서 if 조건문을 제거하기 위해
    lst.append(val)
    i = 0
    
    while lst[i] != val:
        i += 1
    lst.pop()
    # if 문은 cost를 발생시킨다
    if i == len(lst):
        return -1
    else:
        return i
    
    # new_lst = [val]
    # new_lst.extend(lst)
    
    # i = len(new_lst) - 1
    # while new_lst[i] != val:
    #     i -= 1
        
    # new_lst.pop(0)
    
    # if i == 0:
    #     return -1
    # else:
    #     return i - 1

if __name__ == '__main__':
    print(linear_search([2, 5, 1, -3], 2))