#4. Ввод строки, разделённой пробелами на слова, с печатью номера и до 10 символов каждого слова

s = input('Введите последовательность слов, разделённых пробелами: ')
my_list = s.split()
for i, item in enumerate(my_list):
    print(f"{i + 1}: {item[:10]}")

