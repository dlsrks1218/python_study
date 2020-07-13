import os
from typing import List

def get_ascii() -> List[int]:
    upper = [i for i in range(65, 91)]
    small = [i for i in range(97, 123)]
    chk = upper + small
    chk.extend([ord('š'), ord('ď'), ord('é')])
    # print(chk)
    return chk


def word_count(input_dir, output_dir):
    word_set = set()
    word_dict = dict()
    delimeter = set()
    chk = get_ascii()

    with open(input_dir, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip().split(' ')
            # print(line)
            for word in line:
                for ch in word:
                    if ord(ch) not in chk:
                        delimeter.add(ch)
    # print(delimeter)

    entire_word = []
    with open(input_dir, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            for deli in delimeter:
                if deli in line:
                    line = line.replace(deli, '').strip()
            # print(line)
            tmp_line = line.split()
            
            entire_word.extend(tmp_line)
            
            for word in tmp_line:
                word_set.add(word)

        for word in word_set:
            word_dict[word] = 0

        for key, val in word_dict.items():
            word_dict[key] = entire_word.count(key)
    # print(word_dict)
    
    for key, val in word_dict.items():
        if val == max(word_dict.values()):
            print('최다 빈출 단어 -> {} : {}'.format(key, val))
        # if val == min(word_dict.values()):
        #     print('최소 빈출 단어 -> {} : {}'.format(key, val))
    
    with open(output_dir, 'w', encoding='utf-8') as output_file:
        word_dict = sorted(word_dict.items())
        for item in word_dict:
            # print(item)
            output_file.write(str(item))


if __name__ == '__main__':
    input_dir = os.getcwd() + '/day5/' + 'the_little_prince.txt'
    output_dir = os.getcwd() + '/day5/' + 'word_result.txt'
    word_count(input_dir, output_dir)
    print('word count 완료, 파일에 결과를 저장하였습니다.')