import random

def user_choice():
    user = int(input('바위(0), 가위(1), 보(2) 중 하나를 골라주세요(0~2)'))
    if user == 0  or user == 1 or user == 2:
        return user
    else:
        print('다시 한번 선택해주십시요.')
        user_choice()

def regame():
    choice = input('계속 게임하시겠습니까? (y/n)')
    if choice == 'n':
        choice = 0
    elif choice == 'y':
        choice = 1
    else:
        print('다시 한번 선택해주십시요.')
        regame()
    return choice

def rcp():
    """ [바위(R) 가위(C) 보(P) 게임]
    1. 사용자로부터 가위, 바위, 보 입력
    2. 컴퓨터가 임의의 가위, 바위, 보 생성
    3. 사용자와 컴퓨터간의 가위, 바위, 보 판정 
    4. 사용자와 컴퓨터 중 누가 이겼는지 출력
    5. 게임 종료 시 게임을 중단할 지, 계속 할 지 물어보기
    """

    while True:
        print('='*50)
        print('가위 바위 보 게임을 시작하겠습니다')
        
        user = user_choice()
        com = random.randrange(0,3)

        if com == user:  # com과 user가 다를때
            if com == 0:
                com, user = '바위', '바위'
            elif com == 1:
                com, user = '가위', '가위'
            else:
                com, user = '보', '보'
            print('비겼습니다. \nuser = {} com = {}'.format(user, com))
        else:   # com과 user가 다를때
            if user == 0:   # 0, Rock
                if com == 1:  # Scissor
                    user, com = '바위', '가위'
                    print('user가 승리하였습니다. \nuser = {} com = {}'.format(user, com))
                else:   # Paper
                    user, com = '바위', '보'
                    print('com이 승리하였습니다. \nuser = {} com = {}'.format(user, com))

            elif user == 1: # 1, Scissor
                if com == 0:  # Rock
                    user, com = '가위', '바위'
                    print('com이 승리하였습니다. \nuser = {} com = {}'.format(user, com))
                else:   # Paper
                    user, com = '가위', '보'
                    print('user가 승리하였습니다. \nuser = {} com = {}'.format(user, com))
            else:   # 2, Paper
                if com == 0:  # Rock
                    user, com = '보', '바위'
                    print('user가 승리하였습니다. \nuser = {} com = {}'.format(user, com))
                else:   # Scissor
                    user, com = '보', '가위'
                    print('com이 승리하였습니다. \nuser = {} com = {}'.format(user, com))
        
        choice = regame()
        if choice == 0:
            break
        print()

if __name__ == '__main__':
    rcp()