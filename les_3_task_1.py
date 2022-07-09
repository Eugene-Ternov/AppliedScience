# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов

multiple_2_9_count = [0 for _ in range(2, 10)]

for n in range(2, 100):
    for i, m in enumerate(range(2, 10)):
        if n % m == 0:
            multiple_2_9_count[i] += 1

s = '\nКоличество натуральных чисел в диапазоне от 2 до 99 кратных '
for i, m in enumerate(range(2, 10)):
    s += f'{m} - {multiple_2_9_count[i]}'
    if m < 9:
        s += ', '

print(s)
