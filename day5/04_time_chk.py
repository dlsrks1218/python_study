import time
import linear_search01, linear_search02, linear_search03
from typing import Callable, Any

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float:
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()

    return (t2 - t1) *  1000.0

def print_times(v: Any, L: list) -> None:
    # list.index의 실행시간
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 -t1) * 1000.0

    while_time = time_it(linear_search01.linear_search, L, v)
    for_time = time_it(linear_search02.linear_search, L, v)
    sentinel_time = time_it(linear_search03.linear_search, L, v)

    print('{}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}'.format(
        v, while_time, for_time, sentinel_time, index_time))

if __name__ == '__main__':
    L = list(range(10000001))
    
    print_times(10, L)
    print_times(5000000, L)
    print_times(10000000, L)