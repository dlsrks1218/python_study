def refine_user_num(user_num) -> str:
    # 문자열 정제 ex) 1,2,3 or 1 2 3 -> 123
    delimeters = [',', ' ']
    for delimeter in delimeters:
        if delimeter in user_num:
            return user_num.replace(delimeter, '')

def check_input(user_num: str) -> bool:
    # input을 셋에 추가하여 길이가 3이 안되면 False 반환
    tmp_set = set()
    for ch in user_num:
        tmp_set.add(ch)
    if len(tmp_set) == 3:
        return True
    else:
        return False

inp = input('입력하셈 : ')

res = refine_user_num(inp)

print(res, len(res))

print(check_input(res))