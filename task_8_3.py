#3. Собственное исключение при вводе списка чисел (проверяет введённую строку и заведует вставкой в список)

class OwnException(Exception):
    def __init__(self, *args):
        self.__nums = []
        if len(args) > 1:
            self.__nums = args[1]
        if len(args) > 2:
            self.__final_phrase = args[2]
        else:
            self.__final_phrase = "Вводите числа, продолжайте."
        try:
            self.__nums.append(float(str(args[0])))
            self.__ok = True
        except:
            self.__ok = False


    def __str__(self):
        s = ""
        if self.__ok:
            s = f"Ваш список: {self.__nums}"
        else:
            if len(self.__nums) > 0:
                s = f"До сих пор Вы вводили числа: {self.__nums}\nПоступайте так и впредь до завершения программы.\n"
            s = s + self.__final_phrase
        return s


my_list = []
while True:
    s = input("Введите любое число или # для завершения программы: ").strip()
    if s == '#':
        break
    try:
        raise OwnException(s, my_list, "Ещё раз, пожалуйста.")
    except OwnException as err:
        print(err)

if len(my_list) == 0:
    print("Не введено ни одного числа")
else:
    print(f"Введённые Вами числа: {my_list}")





