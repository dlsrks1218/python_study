import os
file_dir = os.getcwd() + '/day4/my_recipe.txt'
with open(file_dir, 'w', encoding='utf-8') as file:
    print(type(file))
    text = """ * 라면 레시피
1. 물을 끓인다.
2. 라면과 스프를 넣는다.
3. 5분을 더 끓여 먹는다.
"""
    file.write(text)
