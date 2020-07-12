from typing import List

def netherlands(lst: List):
    rule = {}
    rule['red'] = 2
    rule['green'] = 1
    rule['blue'] = 0

    # front, rear = '', ''
    for i in range(len(rule) - 1):
        for j in range(len(lst) - 1):
            for k in range(len(lst) - 1):
                # front, rear = lst[k], lst[k+1]
                if rule[lst[k]] < rule[lst[k+1]]:
                    lst[k], lst[k+1] = lst[k+1], lst[k]
                    break
    print(lst)

if __name__ == '__main__':
    # 네덜란드 국기 문제
    # lst = ['red','green','blue', 'green', 'blue', 'red', 'red']
    lst = ['red','green','blue','green','blue','blue','green','green','green','blue','red']
    print(lst)
    netherlands(lst)