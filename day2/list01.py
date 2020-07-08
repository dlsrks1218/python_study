# colors = ['red', 'blue', 'green']

# print(colors[0])
# print(colors[1])
# print(colors[2])
# print(len(colors))

# cities = ['0 서울', '1 도쿄', '2북경', '3뉴욕', '4 런던', '5 시드니', '6 파리', '7 방콕']
# print(cities[0:4])
# print(cities[1:6])
# print(cities[-3:])
# print(cities[-3:-1])
# print(cities[:-1])

color1 = ['red', 'green', 'black']
color2 = ['blue', 'pink', 'orange']

total_color = color1 + color2

c1, c2, c3, c4, c5, c6 = total_color
print(c1, c2, c3, c4, c5, c6)

a = [1,2,3,4,5]
a.append(10)
print(a)

b = [100, 200, 300]
a.extend(b)
print(a)

a.pop()
print(a)