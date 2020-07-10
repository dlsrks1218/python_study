# encoding이 cp949이면 한글이 깨짐
# utf-8로 저장할 것
# 바이너리 파일 읽으려면 'rb'
import os

file_dir = os.getcwd() + '/python/day4/file_example.txt'

# file = open(file_dir, 'r', encoding='utf-8')
# print(file)
# contents = file.read()
# # 리소스 해제가 꼭 필요함
# file.close()
# print(contents)

# 리소스 자동 해제해줌
with open(file_dir, 'r', encoding='utf-8') as file:
    print(file)
    contents = file.read()
    print(contents)

