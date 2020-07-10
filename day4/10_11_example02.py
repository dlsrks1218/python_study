import os

def read_text(file_name: str):
    file_dir = os.getcwd() + file_name

    contents = []

    with open(file_dir, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip().split(' ')
            contents.append(line)
    print(contents)

if __name__ == '__main__':
    read_text('/day4/alkaline_metals.txt')