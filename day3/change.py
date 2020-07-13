def get_change_list(my_money: int):
    change_list = [50000, 10000, 5000, 1000, 500, 100]
    result = []

    while len(change_list) != 0:
        change_cnt = {}
        
        if len(change_list) == 1:
            change_cnt[100] = my_money // 100
            result.append(change_cnt)
            break
        
        # dict 초기화
        for change in change_list:
            change_cnt[change] = 0

        tmp_money = my_money

        for change, cnt in change_cnt.items():
            if tmp_money == 0:
                break
            tmp_cnt = tmp_money // change
            change_cnt[change] += tmp_cnt
            tmp_money %= change
        
        cnt = 0
        for change in change_list:
            if my_money // change > 0:
                change_list = change_list[cnt+1:]
                break
            cnt += 1
        
        result.append(change_cnt)
    
    return result

result = get_change_list(2000)

for item in result:
    for k, v in item.items():
        if v != 0:
            print('{}원 {}개'.format(k, v), end=' ')
    print()
