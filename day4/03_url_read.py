# 전체 숫자의 합 출력하기
import urllib.request

url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'

with urllib.request.urlopen(url) as webpage:
    total_pelts = 0

    for line in webpage:
        line = line.strip().decode('utf-8')
        
        if line.startswith('#'):
            continue

        # 첫번째 줄을 거르는 예외처리
        try:
            total_pelts += int(line)
        except Exception as ex:
            # print(ex)
            continue

print(total_pelts)
