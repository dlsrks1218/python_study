# encoding이 cp949이면 한글이 깨짐
# utf-8로 저장할 것
# 바이너리 파일 읽으려면 'rb'
import os

file_dir = os.getcwd() + '/python/day4/file_example.txt'
file = open(file_dir, 'r', encoding='utf-8')
# file = open(file_dir, 'r', encoding='cp949')
print(file)

contents = file.read()
file.close()
print(contents)
