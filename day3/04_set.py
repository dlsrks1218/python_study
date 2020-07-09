s = set([1,2,3,4,5,1,2,3])
print(s)

s.add(1)
print(s)

# 지우려는 요소가 없으면 KeyError 발생
s.remove(1)
print(s)

s.update([11,12,13,14,15])
print(s)

# 지우려는 요소가 없어도 에러 발생하지 않음
s.discard(11)
print(s)

s.clear()
print(s)