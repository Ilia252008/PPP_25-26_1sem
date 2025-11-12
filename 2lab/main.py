

def roman_to_int(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    
    for char in roman[::-1]:
        current = values[char]
        if current < prev:
            result -= current
        else:
            result += current
        prev = current
    
    return result

def int_to_roman(num):
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ''
    for val, symbol in values:
        while num >= val:
            result += symbol
            num -= val
    return result


a = input().strip()
b = input().strip()
op = input().strip()
x = roman_to_int(a)
y = roman_to_int(b)

if op == '+':
    res = x + y
elif op == '-':
    res = x - y
elif op == '*':
    res = x * y
elif op == '/':
    res = x // y
if res < 1:
    print("Ошибка")
else:
    print(int_to_roman(res))
