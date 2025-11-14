def convert_roman_to_arabic(roman_num):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    if not roman_num:
        return None
    total = 0
    previous_value = 0
    
    for numeral in roman_num.upper():
        if numeral not in roman_dict:
            return None
        current_value = roman_dict[numeral]
        
        if previous_value < current_value:
            total += current_value - 2 * previous_value
        else:
            total += current_value
            
        previous_value = current_value
    
    return total

def convert_arabic_to_roman(arabic_num):
    if arabic_num <= 0:
        return None
        
    conversion_table = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_result = ''
    
    for value, symbol in conversion_table:
        while arabic_num >= value:
            roman_result += symbol
            arabic_num -= value
    return roman_result

def calculate_roman_numbers():
    print("Римский калькулятор")
    print("Введите два РИМСКИХ числа и операцию")
    print("Допустимые римские цифры: I, V, X, L, C, D, M")
    
    first_input = input("Первое число: ").strip()
    second_input = input("Второе число: ").strip()
    operation = input("Операция (+, -, *, /): ").strip()
    
    if any(char.isdigit() for char in first_input) or any(char.isdigit() for char in second_input):
        print("Ошибка: вводите только римские цифры (I, V, X, L, C, D, M)")
        return
    
    first_number = convert_roman_to_arabic(first_input)
    second_number = convert_roman_to_arabic(second_input)
    
    if first_number is None or second_number is None:
        print("Ошибка: введены некорректные римские числа")
        print("Проверьте, что используете только допустимые римские цифры")
        return
    
    if operation not in ['+', '-', '*', '/']:
        print("Ошибка: некорректная операция")
        print("Допустимые операции: +, -, *, /")
        return
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number == 0:
            print("Ошибка: деление на ноль")
            return
        result = first_number // second_number
    
    if result < 1:
        print("Ошибка: результат меньше I")
        return

    roman_result = convert_arabic_to_roman(result)
    
    if roman_result:
        print(f"Результат: {roman_result}")
    else:
        print("Ошибка при преобразовании результата")

calculate_roman_numbers()



