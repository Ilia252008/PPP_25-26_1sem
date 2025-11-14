

import random

def calculate_diagonals(matrix):
    n = len(matrix)
    main_diag = sum(matrix[i][i] for i in range(n))
    second_diag = sum(matrix[i][n-1-i] for i in range(n))
    return main_diag, second_diag


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
table = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1, 100))
    table.append(row)
print("Таблица:")
for row in table:
    print(row)
print("Максимумы по строкам:")
for i in range(n):
    print(f"Строка {i+1}: {max(table[i])}")
print("Максимумы по столбцам:")
for j in range(m):
    col_max = max(table[i][j] for i in range(n))
    print(f"Столбец {j+1}: {col_max}")
if n == m:
    main_diag = sum(table[i][i] for i in range(n))
    second_diag = sum(table[i][n-1-i] for i in range(n))
    print(f"Сумма главной диагонали: {main_diag}")
    print(f"Сумма побочной диагонали: {second_diag}")
max_sum = 0
max_row = 0
for i in range(n):
    row_sum = sum(table[i])
    if row_sum > max_sum:
        max_sum = row_sum
        max_row = i
print(f"Строка с наибольшей суммой: {max_row + 1}")
print(f"Сумма этой строки: {max_sum}")
sum_main_diag,sum_second_diag =calculate_diagonals(table)
print(f'Сумма первой диагонали :{sum_main_diag}')
print(f'Сумма первой диагонали :{sum_second_diag}')
