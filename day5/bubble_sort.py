def bubble_sort(li: list) -> list:
    # for i in range(len(li)-1):
    #     for j in range(len(li)-1):
    #         #만약 앞에 있는 값이 크다면 두 개를 교환
    #         if li[j] > li[j+1]:
    #             li[j], li[j+1] = li[j+1], li[j]
    
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            #만약 앞에 있는 값이 크다면 두 개를 교환
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

    return li

if __name__ == '__main__':
    print(bubble_sort([5,1,3,2,4]))