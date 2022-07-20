# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter
import random as rnd

print("\nПредставляется целесообразным заменить ввод наименований и прибыли каждого из предприятий за 4 квартала"
      " генератором случайных чисел.")
try:
    plants_count = int(input("Введите количество предприятий от 5 до 100: "))
except:
    plants_count = 5

if plants_count < 5:
    plants_count = 5
elif plants_count > 100:
    plants_count = 100

# Формирование словаря предприятий

plants_dict = {}

for i in range(plants_count):
    c = Counter()
    c.update({1: rnd.randint(5000, 25000)*1000})            # Прибыль за 1-й квартал
    c.update({2: rnd.randint(6000, 30000)*1000})            # Прибыль за 2-й квартал
    c.update({3: rnd.randint(8000, 20000)*1000})            # Прибыль за 3-й квартал
    c.update({4: rnd.randint(5000, 25000)*1000})            # Прибыль за 4-й квартал
    c.update({0: sum(c.values())})                          # Прибыль за год (сумма кварталов)
    plants_dict.update({f'Предприятие {i+1}': c.copy()})    # Автонаименование : поквартальная прибыль

# печать списка предприятий
print(f"Количество предприятий для подсчёта прибыли за год - {plants_count}")
s = f'{"Наименование":<20}{"1-й квартал":<15}{"2-й квартал":<15}{"3-й квартал":<15}{"4-й квартал":<15}{"Итого за год"}'
sep_len = len(s) + 1
print(sep_len * "-")
print(s)
print(sep_len * "-")

# Агрегированные данные

c = Counter({1: 0, 2: 0, 3: 0, 4: 0, 0: 0})

# Суммарная прибыль по всем предприятиям поквартально и за год

for key, val in plants_dict.items():
    s = f'{key:<22}{val.get(1):<15}{val.get(2):<15}{val.get(3):<15}{val.get(4):<15}{val.get(0)}'
    c = c + val
    print(s)

print(sep_len * "-")
s = f'{"Всего прибыли:":<22}{c.get(1):<15}{c.get(2):<15}{c.get(3):<15}{c.get(4):<15}{c.get(0)}'
print(s)

# Средняя прибыль по всем предприятиям поквартально и за год

for key, val in c.items():
    c[key] /= plants_count

s = f'{"Средняя прибыль:":<22}{c.get(1):<15}{c.get(2):<15}{c.get(3):<15}{c.get(4):<15}{c.get(0)}'
print(s)

# Предприятия с прибылью за год выше/ниже средней

more_profit = [[key, val.get(0)] for key,val in plants_dict.items() if val.get(0) > c.get(0)]
less_profit = [[key, val.get(0)] for key,val in plants_dict.items() if val.get(0) < c.get(0)]

print(f'\nПредприятия с прибылью за год выше средней ({c.get(0):.2f}):\n')
for el in more_profit:
    print(f'{el[0]:<20}{el[1]:.2f}')

print(f'\nПредприятия с прибылью за год ниже средней ({c.get(0):.2f}):\n')
for el in less_profit:
    print(f'{el[0]:<20}{el[1]:.2f}')






