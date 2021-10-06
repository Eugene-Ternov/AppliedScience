#5. Произведение всех элементов списка из чётных чисел от 100 до 1000 (включительно) при помощи функции reduce()

from functools import reduce

mult = lambda prev_el, el: prev_el * el

def mult_func(par1, par2):
    return reduce(mult, [i for i in range(par1, par2 + 1) if i % 2 == 0])

i = 100
j = 1000
k = mult_func(i, j)
print(f"Произведение всех чётных чисел от {i} до {j} включительно:", k)
print("Это его длина:", len(str(k)))
i = 1
j = 10
print(f"Не надо бояться! Вот произведение всех чётных чисел от {i} до {j} включительно:", mult_func(i, j))
print("Вычислено той же функцией. Числа бывают разные :-)")



