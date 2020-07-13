from typing import Tuple
import random

def check_sb(com_num: str, user_num: str) -> Tuple[int, int]:
    strike, ball = 0, 0
    for i in range(len(com_num)):
        # 자리와 수 모두 일치하면 strike
        if com_num[i] == user_num[i]:
            strike += 1
        # 자리가 일치하지 않을 때, 수가 존재만 할 때 ball
        else:
            if com_num[i] in user_num:
                ball += 1
    return (strike,ball)

def generate_com_num() -> str:
    # 중복을 허용하지 않기 위해 셋 길이가 3이 될때까지 추가 
    num_set = set()
    while len(num_set) != 3:
        num_set.add(str(random.randrange(1, 10)))
    com_num = ''.join(list(num_set))
    return com_num
    
def check_user_num(user_num: str) -> bool:
    # input을 셋에 추가하여 길이가 3이 아니면 False 반환
    tmp_set = set()
    for ch in user_num:
        tmp_set.add(ch)
    if len(tmp_set) == 3:
        return True
    else:
        return False
    
def refine_user_num(user_num: str) -> str:
    # 문자열 정제 ex) 1,2,3 or 1 2 3 -> 123
    delimeters = [',', ' ']
    for delimeter in delimeters:
        if delimeter in user_num:
            user_num = user_num.replace(delimeter, '')
    return user_num

def print_result(cnt: int) -> None:
    # 정답 맞추는 데 소요된 횟수 출력
    print('{}번만에 맞추셨습니다.'.format(cnt))    
    if cnt >= 1 and cnt <= 5:
        print('천재입니다')
    elif cnt >= 6 and cnt <= 10:
        print('잘하셨습니다')
    elif cnt >= 11 and cnt <= 15:
        print('더 노력해야합니다')
    else:
        print('게임에 소질이 없습니다')

def number_baseball_start() -> None:
    com_num, user_num = '', '' 
    # 게임 시작
    print('숫자 야구 게임을 시작하겠습니다.')
    com_num = generate_com_num()
    print('컴퓨터가 3개의 숫자를 생각했습니다.')
    # 컴퓨터의 숫자와 사용자 숫자가 일치할 때까지 반복하며 횟수를 셈
    cnt = 0
    while com_num != user_num:
        # 사용자 입력값 예외 처리
        ## 3개 보다 많거나 적은 값 입력 or 중복된 입력
        try:
            print('='*71)
            user_num = input('3개의 숫자를 입력해주세요(중복 불가) ex) 123 또는 1,2,3 또는 1 2 3 -> ')
            user_num = refine_user_num(user_num)
            if check_user_num(user_num) == False:
                raise Exception
            cnt += 1
            # strike와 ball을 체크
            strike, ball = check_sb(com_num,user_num)
            print(com_num, user_num)
            print('{}을 입력하셨습니다.'.format(user_num))
            # print('스트라이크 : {}, 볼 : {}'.format(strike_ball[0], strike_ball[1]))
            print('스트라이크 : {}, 볼 : {}'.format(strike, ball))
        except Exception as ex:
            # print(ex)
            print('숫자를 정확히 입력해주세요.')
            continue

    # 정답 맞추는 데 소요된 횟수 출력
    print_result(cnt)

if __name__ == '__main__':
    number_baseball_start()

# 숫자 야구 게임
# 컴퓨터가 1~9사이의 임의의 숫자 3개를 발생한다. (중복을 허용하지 않는다)
# 사용자로부터 3개의 숫자를 입력 받는다.
# ex) 123 또는 1,2,3 또는 1 2 3
# 사용자가 입력한 숫자와 컴퓨터가 발생한 숫자가 일치하는지 검증한다.
# 사용자가 입력한 숫자가 컴퓨터가 발생한 숫자에 포함되어 있는지를 검증한다.
# 숫자의 위치(자리)까지 일치하면 "스트라이크"라고 판정
# 숫자의 위치를 다르지만, 해당 숫자가 포함되어 있으면 "볼"이라고 판정
# 전체 판정 결과를 스트라이크와 볼의 숫자로 표현한다.
# 해당 숫자가 아무것도 포함되어 있지 않으면, "노 스트라이크, 노 볼"이라고 판정
# 예) 컴퓨터 숫자 768, 사용자가 입력한 숫자 756 -> 1스트라이크, 1볼
# 예) 컴퓨터 숫자 456, 사용자가 입력한 숫자 149 -> 0스트라이크, 1볼
# 예) 컴퓨터 숫자 349, 사용자가 입력한 숫자 125 -> 0스트라이크, 0볼
# 총 몇번 동안 맞췄는지 결과를 출력해 준다.
# 1 ~ 5번 : 당신은 천재입니다.
# 6 ~ 10번 : 잘 하셨습니다.
# 11 ~ 15번 : 당신은 더 노력해야 합니다.
# 15번 ~ : 게임에 소질이 없습니다.