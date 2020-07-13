def bubble_sort(lst: list) -> list:
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1], lst[j+1], lst[j]
    return lst

if __name__ == '__main__':
    print(bubble_sort([5,1,3,2,4]))