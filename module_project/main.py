import os, module as m

def start():
    score = {}
    while True:
        print('## 현재 등록자 수 : ', len(score))
        # 1~4만 허용
        # 입력값을 int()로 casting
        cmd = int(input('1) 성적 입력 2) 성적 출력 3) 성적 조회 4) 저장하기 5) 읽어오기 6) 리포트 출력 9) 종료\n입력은 (1~9) 사이 숫자로 해주세요 -> '))
        if cmd == 1:
            score = m.enter_score(score)
            score = dict(m.calc_score(score))
        elif cmd == 2:
            m.show_all_score(score)
        elif cmd == 3:
            # 입력값이 존재하지 않을 때 예외처리 하기!
            search_user = input('검색할 사용자명을 입력하세요 -> ')
            m.search_user_score(score, search_user)
        elif cmd == 4:
            m.save_all_score(score)
            print('### 파일을 저장했습니다.')
        elif cmd == 5:
            m.load_all_score(score)
            print('### 파일을 읽어왔습니다.')
        elif cmd == 6:
            # dir = os.path.dirname(os.path.realpath(__file__))
            dir = os.getcwd()
            input_file = dir + '/output/score.dat'
            output_file = dir + '/output/report.csv'
            m.generate_report(input_file, output_file)
            print('### 리포트를 생성했습니다.')
        elif cmd == 9:
            quit()
        else:
            print('** 명령어는 1~9 사이의 숫자만 입력해 주세요. **\n')
            continue

        print()


if __name__ == '__main__':
    start()

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
