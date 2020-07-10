# 반환값을 리스트로 저장하기 위한 클래스
# from typing import List

# 국 영 수 총점 평균 석차 구하기
# 1. 입력
# 2. 출력
# 3. 조회
# 4. 저장하기
# 5. 읽어오기
# 9. 종료

import os

def enter_score(score):
    """
    # 이름,국어,영어,수학
    # 각 과목 점수는 0~100 사이
    """
    while True:
        try:
            user_data = input('성적을 입력하세요. (이름,국어,영어,수학) \
            그만 입력하시려면 0을 입력해주세요 -> ')
            if user_data == '0':
                break
            tmp = user_data.split(',')
            if len(tmp) != 4:
                raise Exception
            user_name = tmp[0]
            user_score = [int(i) for i in tmp[1:]]
            for scr in user_score:
                if scr < 0 or scr > 100:
                    raise Exception
            score[user_name] = user_score
        except Exception as ex:
            print('** 성적 데이터를 정확하게 입력해주세요 **')
            continue
    # score에 총점, 평균 추가 후 총점 높은 순으로 정렬
    return score

def calc_score(score):
    for user in score:
        tmp = score[user]
        total = tmp[0] + tmp[1] + tmp[2]
        avg = total / len(tmp)
        if len(tmp) < 5:
            tmp.extend([total, avg])
    return sorted(score.items(), key = lambda x: x[1][-2], reverse=True)

def show_all_score(score) ->int:
    if not score:
        return -1
    else:
        print('#'*50)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print('#'*50)
        # print('{}\t{}\t{}\t{}\t{}\t{:.4f}'.format(user, \
        #     tmp[0], tmp[1], tmp[2], total, avg))
        new_list = score.items()
        for user in new_list:
            print(user[0], '\t', seperate_score(user[1]))

def search_user_score(score, search_user):
    try:
        if not score:
            return -1
        tmp = score[search_user]
        print('#'*50)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print('#'*50)
        # print('{}\t{}\t{}\t{}\t{}\t{:.4f}'.format(search_user, \
        #     tmp[0], tmp[1], tmp[2], total, avg)) 
        print(search_user, '\t', seperate_score(score[search_user]))
    except:
        search_user = input('사용자가 존재하지 않습니다. 다시 입력해주세요 -> ')
        search_user_score(score, search_user)

def save_all_score(score: dict):
    dat_name = os.getcwd() + '/day4/score.dat'
    with open(dat_name, 'w', encoding='utf-8') as file:
        print(score)
        for k, v in score.items():
            _name = k
            _nums = v # [100, 80, 90, 270, 90.0]
            file.write('{},'.format(_name))
            for _num in _nums:
                file.write('{},'.format(_num))
                # if _num == _nums[-1]:
                #     file.write('{}'.format(_num))
                # else:
                #     file.write('{},'.format(_num))
            file.write('\n')

def load_all_score(score: dict) ->dict:
    load_score = {}
    dat_name = os.getcwd() + '/day4/score.dat'
    with open(dat_name, 'r', encoding='utf-8') as file:
        for line in file:
            _values = line.rstrip().split(',')
            load_score[_values[0]] = [_values[1], _values[2], _values[3], _values[4], _values[5]]
    for item in load_score.items():
        print(item)
    return load_score

def seperate_score(data: list):
    result = ''
    for _num in range(len(data) - 1):
        result += str(data[_num]) + '\t'
    return result + ('%.4f' %(data[len(data) - 1]))

def start():
    score = {}
    while True:
        print('## 현재 등록자 수 : ', len(score))
        # 1~4만 허용
        # 입력값을 int()로 casting
        cmd = int(input('1) 성적 입력 2) 성적 출력 3) 성적 조회 4) 저장하기 \
            5) 읽어오기 9) 종료\n입력은 (1~9) 사이 숫자로 해주세요 -> '))
        if cmd == 1:
            score = enter_score(score)
            score = dict(calc_score(score))
        elif cmd == 2:
            if show_all_score(score) == -1:
                print('데이터가 없습니다. 성적을 입력해주세요.\n')
                continue
            else:
                show_all_score(score)
        elif cmd == 3:
            # 입력값이 존재하지 않을 때 예외처리 하기!
            search_user = input('검색할 사용자명을 입력하세요 -> ')
            if search_user_score(score, search_user) == -1:
                print('데이터가 없습니다. 성적을 입력해주세요.\n')
                continue
            else:
                search_user_score(score, search_user_score)
        elif cmd == 4:
            save_all_score(score)
            print('### 파일을 저장했습니다.')
        elif cmd == 5:
            load_all_score(score)
            print('### 파일을 읽어왔습니다.')
        elif cmd == 9:
            quit()
        else:
            print('** 명령어는 1~9 사이의 숫자만 입력해 주세요. **\n')
            continue

        print()

if __name__ == '__main__':
    # score = {}
    # score['USER1'] = [100, 90, 80]
    # score['USER2'] = [70, 85, 99]
    # score['USER3'] = [45, 86, 90]
    # score['USER4'] = [80, 85, 81]
    start()
