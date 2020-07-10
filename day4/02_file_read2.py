import os

file_dir = os.getcwd() + '/python/day4/hopedale.txt'
with open(file_dir, 'r', encoding = 'utf-8') as hopedale_file:
    # 첫 줄 무시
    hopedale_file.readline()
    # 읽은 데이터의 앞뒤 공백 제거
    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()

    total_pelts = int(data)

    for data in hopedale_file:
        total_pelts = total_pelts + int(data.rstrip())
    
    print(data.rstrip())

print('Total number of pelts : {}'.format(total_pelts))