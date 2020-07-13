import os
from typing import List

def get_ascii() -> List[int]:
    """ 특수 문자를 걸러내기 위한 아스키코드로 된 리스트 반환
    upper -> 'A' ~ 'Z'에 해당하는 아스키코드
    small -> 'a' ~ 'z'에 해당하는 아스키코드
    chk = upper + small에 ['š', 'ď', 'é']에 해당하는 아스키코드 추가
    """
    upper = [i for i in range(65, 91)]
    small = [i for i in range(97, 123)]
    chk = upper + small
    chk.extend([ord('š'), ord('ď'), ord('é')])
    # print(chk)
    return chk


def word_count(input_dir, output_dir):
    # 모든 단어의 집합 (중복 X)
    word_set = set()
    # 중복 없는 모든 단어들의 빈도를 담은 딕셔너리
    word_dict = dict()
    # get_ascii를 통해서 알파벳을 제외한 모든 특수문자를 구분자로 추가
    delimeter = set()

    # 알파벳에 해당하는 아스키코드 리스트
    chk = get_ascii()
    with open(input_dir, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip().split(' ')
            # print(line)
            for word in line:
                for ch in word:
                    # 알파벳이 아닌 것들은 모두 특수문자 -> 구분자(delimeter)
                    if ord(ch) not in chk:
                        delimeter.add(ch)
    # print(delimeter)

    # 중복 포함 모든 단어 구하기 -> entire_word에 추가
    entire_word = []
    with open(input_dir, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            for deli in delimeter:
                if deli in line:
                    line = line.replace(deli, '').strip()
            # print(line)
            tmp_line = line.split()
            entire_word.extend(tmp_line)
            # 모든 단어의 중복을 제거하기위해 word_set에 추
            for word in tmp_line:
                word_set.add(word)

        for word in word_set:
            word_dict[word] = 0

        for key, val in word_dict.items():
            word_dict[key] = entire_word.count(key)
    
    # print(entire_word)      
    # print(word_dict)
    
    # 최다 빈출 단어, 빈도 출력
    for key, val in word_dict.items():
        if val == max(word_dict.values()):
            print('최다 빈출 단어 -> {} : {}'.format(key, val))
        # if val == min(word_dict.values()):
        #     print('최소 빈출 단어 -> {} : {}'.format(key, val))
    
    # output_file에 결과 쓰기
    with open(output_dir, 'w', encoding='utf-8') as output_file:
        word_dict = sorted(word_dict.items())
        for item in word_dict:
            output_file.write(str(item))


if __name__ == '__main__':
    # 수정 시 본인 파일의 절대경로로 바꿀것
    input_dir = os.getcwd() + '/day5/' + 'the_little_prince.txt'
    output_dir = os.getcwd() + '/day5/' + 'word_result.txt'
    word_count(input_dir, output_dir)
    print('word count 완료, 파일에 결과를 저장하였습니다.')