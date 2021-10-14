#2. Класс дороги и масса покрытия для неё

import task_6_2

class ChildRoad(task_6_2.Road):
    pass

print("\nИмпорт класса Road из файла task_6_2 в текущей папке.")
print("Использовать protected-члены за пределами класса не рекомендуется, но вызов работает (из другой папки тоже).")
print("В отличие от 'private' атрибуты и методы 'protected' базового класса наследуются потомками.")
print("Они не виды в окне Code Insight, но становятся видны в конкретном месте кода, если их вызвать явно,")
print("а затем стереть и снова поставить точку после имени объекта класса.")
r = task_6_2.Road(5800, 20)
asphalt_weight = 22 * 4.9 * r._length * r._width
print(f"Расчётная масса асфальта для участка дороги {r._width} на {r._length} м - {asphalt_weight * 0.001:.3f} т")
p = ChildRoad(6800, 24)
asphalt_weight = 22 * 6 * p._length * p._width
print(f"Расчётная масса покрытия экспериментальной дороги {p._width} на {p._length} м - {asphalt_weight * 0.001:.3f} т")
