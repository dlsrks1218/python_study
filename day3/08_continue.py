s = 'C3H7'
total = 0
count = 0

for i in range(len(s)):
    if not s[i].isalpha():
        total += int(s[i])
        count += 1

print('total = {}, count = {}'.format(total, count))