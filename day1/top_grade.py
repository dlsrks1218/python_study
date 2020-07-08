def get_top():
    kor1, eng1, mat1 = float(input()), float(input()), float(input())
    kor2, eng2, mat2 = float(input()), float(input()), float(input())
    kor3, eng3, mat3 = float(input()), float(input()), float(input())

    sum1 = kor1 + eng1 + mat1
    sum2 = kor2 + eng2 + mat2
    sum3 = kor3 + eng3 + mat3
    
    top = get_max(sum1, sum2, sum3)

    print(top)

    return top

def get_max(num1: float, num2: float, num3: float) ->float:
    max_num = num1
    if num2 > max_num:
        max_num = num2
        if num3 > max_num:
            max_num = num3
    if num3 > max_num:
        max_num = num3
        if num2 > max_num:
            max_num = num2

    return max_num

get_top()