# 1
country = 'United States of America'
for ch in country:
    if ch.isupper():
        print(ch)

# 2
print(list(range(10)))
print(list(range(3)))
print(list(range(1)))
print(list(range(0)))

# 3
print(list(range(2000, 2050, 4)))
print(list(range(2050, 2000, -4)))

# 4
total = 0
for i in range(1, 101):
    total += i
print(total)

names = ['A', 'B', 'C']
kor = [100, 90, 80]
eng = [90, 80, 70]
mat = [80, 70, 60]

for i in range(len(names)):
    print(names[i])
    total = kor[i] + eng[i] + mat[i]
    avg = total / len(names)