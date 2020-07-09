country_code = {'America': '1', 'Austrailia': '61', 'Japan': '81', 'Korea': '82', 'China': '86'}
# print(country_code)

country_code['Germany'] = '49'
print(country_code)
print()
print(country_code.keys())
print()
print(country_code.values())
print()
# 튜플 형태의 아이템들의 리스트
print(country_code.items())
print()
for item in country_code.items():
    print(item)
print()
# unpacking 기법
# for item in country_code.items():
#     key, value = item
#     print('key = {}, value = {}'.format(key, value))
for key, value in country_code.items():
    print('key = <{}>, value = <{}>'.format(key, value))
