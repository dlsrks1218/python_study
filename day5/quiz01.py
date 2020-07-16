import os
from typing import List
import string

def count_unique_words(input_dir: str) -> dict:
    words = {}
    # punctuation -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    with open(input_dir, encoding='utf-8') as input_file:
        for line in input_file:
            for word in line.split():
                word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1
    
    for word in sorted(words):
        print('{} : {}번'.format(word, words[word]))

    return words


def get_ascii() -> List[int]:
    """ 특수 문자를 걸러내기 위한 아스키코드로 된 리스트 반환

    upper -> 'A' ~ 'Z'에 해당하는 아스키코드
    small -> 'a' ~ 'z'에 해당하는 아스키코드
    chk = upper + small에 ['š', 'ď', 'é']에 해당하는 아스키코드 추가

    Args:
        List[int]: 알파벳과 'š', 'ď', 'é'의 아스키코드로 된 리스트 반환
    """
    upper = [i for i in range(65, 91)]
    small = [i for i in range(97, 123)]
    chk = upper + small
    chk.extend([ord('š'), ord('ď'), ord('é')])
    # print(chk)
    return chk


def word_count(input_dir: str, output_dir: str) -> dict:
    """모든 단어의 빈도 세기

    Args:
        input_dir (str): 단어의 빈도를 셀 input 파일
        output_dir (str): 계산된 빈도를 기록할 output 파일
    """
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
    print('구분자 : {}'.format(delimeter))

    # 위에서 구분자를 구하기 위해 한번 input_file 객체가 파일 순회를 1회 마쳤기에 새로 open()
    with open(input_dir, 'r', encoding='utf-8') as input_file, \
        open(output_dir, 'w', encoding='utf-8') as output_file:
        # 중복 포함 모든 단어 구하기 -> entire_word에 추가
        entire_word = []
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
        # print(entire_word)
        # 단어 집합 초기화
        for word in word_set:
            word_dict[word] = 0

        # count를 통해 빈도 세어 딕셔너리에 추가
        for key, val in word_dict.items():
            word_dict[key] = entire_word.count(key)
        print(word_dict)
        
        # 최다 빈출 단어, 빈도 출력
        for key, val in word_dict.items():
            if val == max(word_dict.values()):
                print('최다 빈출 단어 -> {} : {}'.format(key, val))
            # if val == min(word_dict.values()):
            #     print('최소 빈출 단어 -> {} : {}'.format(key, val))
        
        # output_file에 결과 쓰기
        word_dict_lst = sorted(word_dict.items())
        for item in word_dict_lst:
            output_file.write(str(item))

    return word_dict


if __name__ == '__main__':
    # 수정 시 본인 파일의 절대경로로 바꿀것
    input_dir = os.getcwd() + '/day5/' + 'the_little_prince.txt'
    # output_dir = os.getcwd() + '/day5/' + 'word_result.txt'
    # words = word_count(input_dir, output_dir)
    # print('word count 완료, 파일에 결과를 저장하였습니다.')
    # print(words['you'])

    words = count_unique_words(input_dir)
