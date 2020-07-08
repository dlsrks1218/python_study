def convert_to_celsius(fahrenheit: float) -> float:
    result = (fahrenheit - 32) * 5 / 9
    print('result = {}'.format(result))
    return result

def above_freezing(celsius: float) -> bool:
    return celsius > 0

celsius = convert_to_celsius(212)
print(above_freezing(celsius))