import os, sys, csv

class Student:
    def __init__(self, name: str, kor: int, eng: int, mat: int) -> None:
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat


    def calc_sum(self) -> int:
        return self.kor + self.eng + self.mat


    def calc_avg(self) -> float:
        return self.calc_sum() / 3


def enter_score(score: dict) -> dict:
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
            """ 추후 데이터베이스 관련 추가 예정
            user1 = Stduent(user_score[0], user_score[1], user_score[2])
            score[0] = user1
            """
            score[user_name] = user_score
        except Exception as ex:
            print('** 성적 데이터를 정확하게 입력해주세요 **')
            continue
    # score에 총점, 평균 추가 후 총점 높은 순으로 정렬
    return score


def calc_score(score: dict) -> None:
    for user in score:
        tmp = score[user]
        total = tmp[0] + tmp[1] + tmp[2]
        avg = total / len(tmp)
        if len(tmp) < 5:
            tmp.extend([total, avg])
    return sorted(score.items(), key = lambda x: x[1][-2], reverse=True)


def show_all_score(score: dict) -> None:
    try:
        if not score:
            raise Exception
        else:
            print('#'*50)
            print('이름\t국어\t영어\t수학\t총점\t평균')
            print('#'*50)
            # print('{}\t{}\t{}\t{}\t{}\t{:.4f}'.format(user, \
            #     tmp[0], tmp[1], tmp[2], total, avg))
            new_list = score.items()
            for user in new_list:
                print(user[0], '\t', seperate_score(user[1]))
    except Exception as ex:
        print('등록된 사용자가 없습니다.')
        enter_score(score)


def search_user_score(score: dict, search_user: str) -> None:
    try:
        if search_user not in score.keys():
            raise Exception
        tmp = score[search_user]
        print('#'*50)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print('#'*50)
        # print('{}\t{}\t{}\t{}\t{}\t{:.4f}'.format(search_user, \
        #     tmp[0], tmp[1], tmp[2], total, avg)) 
        print(search_user, '\t', seperate_score(score[search_user]))
    except Exception as ex:
        # print(ex)
        search_user = input('사용자가 존재하지 않습니다. 다시 입력해주세요 -> ')
        search_user_score(score, search_user)


def save_all_score(score: dict) -> None:
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
    # for item in load_score.items():
        # print(item)
    return load_score


def seperate_score(data: list) -> None:
    result = ''
    for _num in range(len(data) - 1):
        result += str(data[_num]) + '\t'
    return result + ('%.4f' %(data[len(data) - 1]))


def generate_report(input_file: str, output_file: str) -> None:
    header_list = ['이름', '총점', '평균']
    my_columns = [0, 4, 5] # USER1,100,90,80,270,90.00,
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'w', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file) 
            filewriter = csv.writer(csv_out_file)
            filewriter.writerow(header_list)
            for row in filereader: 
                row_list_output = []
                for index_value in my_columns:
                    row_list_output.append(row[index_value])
                filewriter.writerow(row_list_output)


def start():
    score = {}
    while True:
        print('## 현재 등록자 수 : ', len(score))
        # 1~4만 허용
        # 입력값을 int()로 casting
        cmd = int(input('1) 성적 입력 2) 성적 출력 3) 성적 조회 4) 저장하기 \
            5) 읽어오기 6) 리포트 출력 9) 종료\n입력은 (1~9) 사이 숫자로 해주세요 -> '))
        if cmd == 1:
            score = enter_score(score)
            score = dict(calc_score(score))
        elif cmd == 2:
            show_all_score(score)
        elif cmd == 3:
            # 입력값이 존재하지 않을 때 예외처리 하기!
            search_user = input('검색할 사용자명을 입력하세요 -> ')
            search_user_score(score, search_user)
        elif cmd == 4:
            save_all_score(score)
            print('### 파일을 저장했습니다.')
        elif cmd == 5:
            load_all_score(score)
            print('### 파일을 읽어왔습니다.')
        elif cmd == 6:
            # dir = os.path.dirname(os.path.realpath(__file__))
            dir = os.getcwd()
            input_file = dir + '/day3/score.dat'
            output_file = dir + '/day3/report.csv'
            generate_report(input_file, output_file)
            print('### 리포트를 생성했습니다.')
        elif cmd == 9:
            quit()
        else:
            print('** 명령어는 1~9 사이의 숫자만 입력해 주세요. **\n')
            continue

        print()

if __name__ == '__main__':
    # 국 영 수 총점 평균 석차 구하기
    # 1. 입력
    # 2. 출력
    # 3. 조회
    # 4. 저장하기
    # 5. 읽어오기
    # 6. 리포트 출력
    # 9. 종료
    
    # score = {}
    # score['USER1'] = [100, 90, 80]
    # score['USER2'] = [70, 85, 99]
    # score['USER3'] = [45, 86, 90]
    # score['USER4'] = [80, 85, 81]

    # score[Student]
    # score[0] = Student('USER1', 100, 90, 80)
    # score[1] = Student('USER1', 70, 85, 99)
    # score[2] = Student('USER1', 45, 86, 90)

    start()
