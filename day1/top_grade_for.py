def get_top():
    grade_list = []

    for i in range(3):
        tmp_kor, tmp_eng, tmp_mat = float(input()), float(input()), float(input())
        tmp_sum = tmp_kor + tmp_eng + tmp_mat
        grade_list.append(tmp_sum)
    
    top = get_max(grade_list)
    print(top)

    return top

def get_max(num_list: list) ->float:
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
        
    return max_num

get_top()