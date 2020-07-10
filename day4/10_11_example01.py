import os

def back_up(src_dir, dest_dir):
    with open(src_dir, 'r', encoding='utf-8') as input_file, \
        open(dest_dir, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            output_file.write(line)        

if __name__ == '__main__':
    src = input('복사할 파일명을 입력해주세요 -> ')
    dest = src.split('.')[0] + '.bak'
    src_dir = os.getcwd() + '/day4/' + src
    dest_dir = os.getcwd() + '/day4/' + dest

    back_up(src_dir, dest_dir)

