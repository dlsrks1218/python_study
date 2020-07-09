# # 1
# celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
# for item in celegans_phenotypes:
#     print(item)
# print()
# # 2
# half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
# for item in half_lives:
#     print(item, end=' ')
# print('\n')
# # 3
# whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
# more_whales = []
# for i in range(len(whales)):
#     more_whales.append(whales[i] + 1)
# print(more_whales)
# print()
# # 7
# country_populations = [1295, 23, 7, 3, 47, 21]
# total = 0
# for item in country_populations:
#     total += item
# print(total)
# print()
# # 8
# rat1 = [1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.2]
# rat2 = [0.8, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.9]
# # 8.a
# if rat1[0] > rat2[0]:
#     print('첫째 날 생쥐1이 생쥐2보다 몸무게가 더 많이 나간다.')
# else:
#     print('첫째 날 생쥐1이 생쥐2보다 몸무게가 더 적게 나간다.')
# # 8.b
# if rat1[0] > rat2[0]:
#     if rat1[-1] > rat2[-1]:
#         print('생쥐1은 여전히 생쥐2보다 무겁다')
# else:
#     print('생쥐2가 생쥐1보다 무거워졌다')
# # 8.c
# if rat1[0] > rat2[0] and rat1[-1] > rat2[-1]:
#         print('생쥐1은 여전히 생쥐2보다 무겁다')
# else:
#     print('생쥐2가 생쥐1보다 무거워졌다')
# print()
# # 10
# for i in range(10, 0, -1):
#     print(i, end=' ')
# print('\n')
# # 11
# total = 0
# for i in range(2, 23):
#     total += i
# avg = total / len(range(2, 23))
# print(avg)
# print()
# 13
# for i in range(7):
#     print('T'* (i+1))
# print()
for i in range(1, 7+1):
    print('T' * i, end='')
    for j in range(7, 0, -1):
        print(' ' * j, end='')
    print()
print()
# # 14
# for i in range(0, 7):
#     print(' ' * (7 - (i+1)) + 'T' * (i+1))
# print()
for i in range(7-1, -1, -1):
    print(' ' * i, end='')
    for j in range(7-i):
        print('T', end='')
    print()
print()
# for i in range(1, 7+1):
#     for j in range(7-i):
#         print(' ', end='')
#     for j in range(i):
#         print('T', end='')
#     print()
# 14.1
for i in range(1, 8):
    print(' ' * (7 - i), 'T' * (i*2-1), sep='')
# # 15
