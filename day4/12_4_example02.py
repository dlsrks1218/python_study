from typing import List, Tuple

# def min_idx(lst: List[int]) -> Tuple[int, int]:
#     return (min(lst), lst.index(min(lst)))

# def max_idx(lst: List[int]) -> Tuple[int, int]:
#     return (max(lst), lst.index(max(lst)))

# def min_or_max_idx(lst: List[int], flag: bool) -> Tuple[int, int]:
#     if flag == True:
#         return min_idx(lst)
#     else:
#         return max_idx(lst)

# def min_idx(lst: List[int]) -> Tuple[int, int]:
#     min_val = lst[0]
#     min_idx = -1

#     for idx in range(1, len(lst)):
#         if lst[0] > lst[idx]:
#             lst[0], lst[idx] = lst[idx], lst[0]
#             print(lst)

lst = [3, 5, 2, 1, 4]

# for idx in range(1, len(lst)):
#     print(lst[idx])
print(min_idx(lst))
# print(min_or_max_idx(lst, 0))