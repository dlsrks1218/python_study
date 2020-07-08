import random

def game():
    """
    1. 맞춘 count 세기
    2. count에 따른 등급 표시
        1~3 : 천재
        4~7 : 보통
        8~  : 바보
    """
    cnt = 0
    # 범위 내의 난수
    com_num = random.randrange(1, 100)
    # print(com_num)
    while True:
        cnt+=1
        user_num = int(input('숫자를 입력하세요(1~100) : '))
        if user_num < 1 or user_num > 100:
            print('1~100 사이 숫자만 입력해주세요.')
        else:
            if com_num > user_num:
                print('{}보다 큰 숫자를 입력해주세요.'.format(user_num))
            elif com_num < user_num:
                print('{}보다 작은 숫자를 입력해주세요.'.format(user_num))
            else:
                print('='*30)
                print('Computer\'s number is {}'.format(com_num))
                if cnt >= 1 and cnt <= 3:
                    print('우왕... 천재..!'.center(30))
                elif cnt >= 4 and cnt <= 7:
                    print('적당하네.'.center(30))
                else:
                    print('바보.. ㅎㅎ'.center(30))
                print('{}번 시도 만에 정답입니다!'.format(cnt).center(30))
                break
        
if __name__ == '__main__':
    game()
