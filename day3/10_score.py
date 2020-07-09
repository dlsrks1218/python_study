# 국 영 수 총점 평균 석차 구하기
# 1. 입력
# 2. 출력
# 3. 조회
# 4. 종료

def calc_score(score):
    for user in score:
        tmp = score[user]
        total = tmp[0] + tmp[1] + tmp[2]
        avg = total / len(tmp)
        tmp.extend([total, avg])
    return sorted(score.items(), key = lambda x: x[1][-2], reverse=True)

def show_all_score():
    print('#'*50)
    print('이름\t국어\t영어\t수학\t총점\t평균')
    print('#'*50)
    # print('{}\t{}\t{}\t{}\t{}\t{:.4f}'.format(user, \
    #     tmp[0], tmp[1], tmp[2], total, avg))
    new_list = score.items()
    for user in new_list:
        print(user[0], '\t', seperate_score(user[1]))

def search_user_score(search_user):
    try:
        tmp = score[search_user]
        print('#'*50)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print('#'*50)
        # print('{}\t{}\t{}\t{}\t{}\t{:.4f}'.format(search_user, \
        #     tmp[0], tmp[1], tmp[2], total, avg)) 
        print(search_user, '\t', seperate_score(score[search_user]))
    except:
        search_user = input('사용자가 존재하지 않습니다. 다시 입력해주세요 -> ')
        search_user_score(search_user)

def seperate_score(data: list):
    result = ''
    for _num in range(len(data) - 1):
        result += str(data[_num]) + '\t'
    return result + ('%.4f' %(data[len(data) - 1]))

def start():
    while True:
        print('## 현재 등록자 수 : ', len(score))
        # 1~4만 허용
        # 입력값을 int()로 casting
        cmd = int(input('1) 성적 입력 2) 성적 출력 3) 성적 조회 4) 종료(1~4) -> '))
        if cmd == 1:
            print('성적이 입력되었습니다.')
        elif cmd == 2:
            show_all_score()
        elif cmd == 3:
            # 입력값이 존재하지 않을 때 예외처리 하기!
            search_user = input('검색할 사용자명을 입력하세요 -> ')
            search_user_score(search_user)
            
        elif cmd == 4:
            print('프로그램을 종료합니다!')
            # 프로그램을 종료하는 내장 메소드
            quit()
        else:
            print('** 명령어는 1~4 사이의 숫자만 입력해 주세요. **\n')
            continue
        print()

if __name__ == '__main__':
    score = {}
    score['USER1'] = [100, 90, 80]
    score['USER2'] = [70, 85, 99]
    score['USER3'] = [45, 86, 90]
    score['USER4'] = [80, 85, 81]
    score = dict(calc_score(score))
    start()
