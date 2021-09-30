#1. Список из элементов различного типа с проверкой и выводом типа всех элементов

my_list = list([])

my_list.append(12.5)
my_list.append(0x16)
my_list.append(-343)
my_list.append(chr(33))
my_list.append(ord('!'))
my_list.append("Строка символов")
my_list.append(b'string of bytes')
my_list.append("А-Я".encode('utf-8'))
my_list.append(bytearray(b'array of bytes'))
my_list.append(None)
my_list.append(4 > -5)
my_list.append([1, 2, 3])
my_list.append((0, 2, 1))
my_list.append({4, 5, 6})
my_list.append({"Eugene": 54, "Roman": 22, "Polina": 26})

print(my_list)
print("\r")

for i, item in enumerate(my_list):
    print(f"Тип элемента {i:2d}:   {str(type(item)).ljust(20)}   Элемент {i:2d}:   {item}")


