#6. Преобразование строки без использования capitelyze()

def int_func(arg):
    s = str(arg)
    return s[0].upper() + s[1:len(s)]

s = input("Введите строку произвольных слов, разделённых пробелами (будет преобразована в строчные буквы): ").lower()
print(f"Исходная строка: '{s}'")
my_list = list([])
my_list.extend(s.split())  # Заполнили список элементами строки

s = ''
for item in my_list:
    s += (int_func(item) + ' ')
s = s.rstrip()
print(f"Итоговая строка: '{s}'")
