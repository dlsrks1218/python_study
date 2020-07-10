"""
추가 사항
1. 구매 후 돈을 더 넣을 수 있는 선택지 추가
2. 거스름돈 패턴에 빠진 경우의 수 존재함
"""

def check_affordable(my_money: int) -> dict:
    # print('현재 가진 금액 : {}'.format(my_money))
    affordable_dict = {}
    for item in menu.items():
        # 메뉴의 가격이 내가 가진 돈보다 작거나 같은 경우 살수있음
        if item[1] <= my_money:
            affordable_dict[item[0]] = item[1]
    return affordable_dict

def get_change_pattern(my_money: int):
    # 화폐 단위
    change_list = [50000, 10000, 5000, 1000, 500, 100]
    # 가능한 경우의 수를 담는 결과 리스트
    result = []

    while len(change_list) != 0:
        # 화폐 단위 별로 사용횟수를 세기 위한 딕셔너리
        change_cnt = {}
        
        # change_list 거스름돈 리스트가 비워져 100원만 남았을때
        if len(change_list) == 1:
            change_cnt[100] = my_money // 100
            result.append(change_cnt)
            break

        # dict 초기화
        for change in change_list:
            change_cnt[change] = 0

        tmp_money = my_money


        for change, cnt in change_cnt.items():
            # 가진 돈이 0면 종료
            if tmp_money == 0:
                break
            # 현재 돈을 화폐 단위로 나눈 몫을 횟수로, 나머지는 현재 돈에 대입
            tmp_cnt = tmp_money // change
            change_cnt[change] += tmp_cnt
            tmp_money %= change
        
        # 화폐 단위 별 사용 횟수가 처음 0보다 클 때 인덱스가 
        # cnt이며 change_list(화폐 단위) cnt인덱스 뒤부터 슬라이싱
        # -> 처음 사용된 단위보다 작은 화폐부터 거스름돈 패턴 찾기 작업을 하기 위함
        cnt = 0
        for change in change_list:
            if my_money // change > 0:
                change_list = change_list[cnt+1:]
                break
            cnt += 1
        
        # 가능한 경우의 수를 result에 추가
        result.append(change_cnt)
    
    return result

def vending_machine_start(menu: dict):
    my_money = 0
    print('='*50)
    print('커피(300원), 생수(100원), 쥬스(700원), 우유(200)를 선택하실 수 있습니다.')
    print('='*50)

    affordable_dict = {}

    # 초기 돈 입력
    insert_coin = int(input('돈을 넣으세요 -> '))
    my_money += insert_coin
    
    while True:
        print()

        affordable_dict = check_affordable(my_money)

        # 현재 가진 돈이 모자랄 때
        if len(affordable_dict) == 0:
            insert_coin = int(input('돈이 부족합니다. 돈을 넣으세요. -> '))
            my_money += insert_coin
            continue

        # 구매 가능한 목록 보여주기
        cnt = 0
        for item in affordable_dict.items():
            cnt += 1
            print('{}) {}({}원)'.format(cnt, item[0], item[1]), end=' ')
        
        # 음료 선택
        choice = int(input('음료를 선택하세요 ->'))
        tmp = list(affordable_dict.keys())[choice-1]
        my_money -= affordable_dict.pop(tmp)
        print('{}을 선택하셨습니다. 거스름돈은 {}원입니다'.format(tmp, my_money))
        
        # 남은돈이 100원 이상이면 거스름돈 패턴을 찾고 보여줌
        # 남은돈이 100원 이하면 패턴을 만들 수 없으므로 그냥 거스름돈 출력
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

        # 추가 주문을 위한 입력
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
    menu['커피'] = 300
    menu['물'] = 100
    menu['주스'] = 700
    menu['우유'] = 200

    vending_machine_start(menu)