# 국어kor 영어eng 수학mat 3과목의 총점과 평균을 구하는 함수 생성

def sum(kor:float, eng:float, mat:float) -> float:
    return kor + eng + mat

def avg(sum_score):
    return sum_score / 3

# 1. 사용자 이름 입력
# 2. 평균을 소수점 2자리에서 반올림
user_name = input('사용자 이름을 입력하세요 : ')
kor = input('국어 점수를 입력하세요 : ')
eng = input('영어 점수를 입력하세요 : ')
mat = input('수학 점수를 입력하세요 : ')

sum_of_user = sum(float(kor), float(eng), float(mat))
avg_of_user = avg(sum_of_user)

print('{}의 총점 : {}'.format(user_name, sum_of_user))
print('{}의 평균 : {}'.format(user_name, round(avg_of_user, 2)))
# print(user_name, '의 총점 : ', sum_of_user)
# print(user_name, '의 평균 : ', round(avg_of_user, 2))