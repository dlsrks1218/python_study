word = input('단어를 하나 입력해주세요 : ')
word_list = list(word)

print(word_list)
print(len(word_list))

result = []

for element in range(len(word_list)):
    result.append(word_list.pop())

print(result)