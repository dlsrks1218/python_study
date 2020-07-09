def check_affordable(my_money: int) -> dict:
    # print('현재 가진 금액 : {}'.format(my_money))
    affordable_dict = {}
    for item in menu.items():
        if item[1] <= my_money:
            affordable_dict[item[0]] = item[1]
    return affordable_dict

def get_change_pattern(my_money: int):
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

def vending_machine_start():
    my_money = 0
    print('='*50)
    print('커피(300원), 생수(100원), 쥬스(700원), 우유(200)를 선택하실 수 있습니다.')
    print('='*50)

    affordable_dict = {}

    insert_coin = int(input('돈을 넣으세요 -> '))
    my_money += insert_coin
    
    while True:
        print()

        affordable_dict = check_affordable(my_money)

        if len(affordable_dict) == 0:
            insert_coin = int(input('돈이 부족합니다. 돈을 넣으세요. -> '))
            my_money += insert_coin
            continue

        cnt = 0
        for item in affordable_dict.items():
            cnt += 1
            print('{}) {}({}원)'.format(cnt, item[0], item[1]), end=' ')
        
        choice = int(input('음료를 선택하세요 ->'))
        tmp = list(affordable_dict.keys())[choice-1]
        my_money -= affordable_dict.pop(tmp)
        print('{}을 선택하셨습니다. 거스름돈은 {}원입니다'.format(tmp, my_money))
        
        if my_money >= 100:
            patterns = get_change_pattern(my_money)
            cnt = 0
            print('반환 가능한 거스름돈의 모든 경우의 수는 다음과 같습니다.')
            print('='*30)
            for pattern in patterns:
                cnt += 1
                print('{} - '.format(cnt), end='')
                for k, v in pattern.items():
                    if v != 0:
                        print('<{}원 {}개>'.format(k, v), end=' ')
                print()
            print('='*30)

        cmd = input('추가 주문을 하시겠습니까? (y/n) -> ')
        if cmd == 'n':
            print('\n안녕히 가세요~^^bb')
            break
        else:
            print('-----')
            continue
        print()

if __name__ == '__main__':
    menu = {}
    menu['coffee'] = 300
    menu['water'] = 100
    menu['juice'] = 700
    menu['milk'] = 200

    vending_machine_start()