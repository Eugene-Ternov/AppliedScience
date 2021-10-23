#1. Валидация дня, месяца и года в строке даты; получение числовых частей даты; класс "Дата"

class Date:
    __DateParts = []

    def __init__(self, date_str):
        self.__valid_date = Date.is_valid_date_string(date_str)
        if self.__valid_date:
            date_parts = Date.__get_date_parts(date_str)
            self.__day, self.__month, self.__year = map(int, date_parts)
        else:
            self.__day, self.__month, self.__year = map(int, [0, 0, 0])

    def __str__(self):
        return f"объект класса Date: valid_date = {self.__valid_date}, day = {self.__day}," \
               f" month = {self.__month}, year = {self.__year}"

    # Пусть объект класса предоставляет четыре переменных только для чтения (вполне очевидного назначения):

    @property
    def valid_date(self):
        return self.__valid_date

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @staticmethod                               # Проверка года на високосность
    def is_leap_year(value):
        try:
            value = int(value)
            return value % 4 == 0 and (value % 100 != 0 or value % 400 == 0)
        except:
            return None

    @staticmethod                               # Вспомогательный - проверка составляющих даты на корректность
    def __check_date_parts(date_parts):
        day, month, year = map(int, list(date_parts))
        month_last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day < 1 or month not in range(1, 13):
            return False
        if Date.is_leap_year(year):             # Коррекция февраля для високосного года
            month_last_day[1] = 29
        return day <= month_last_day[month - 1]

    @staticmethod                               # Искомая проверка строки даты на корректность - public-метод
    def is_valid_date_string(date_str):
        result = False
        date_parts = Date.__get_date_parts(date_str)
        if date_parts:
            result = Date.__check_date_parts(date_parts)
        return result

    @staticmethod                               # Вспомогательный - разбиение строки даты на числовые элементы
    def __get_date_parts(date_str):
        result = None
        date_parts_sep = ('-', '.', '/')
        for sep in date_parts_sep:
            date_parts = date_str.split(sep)
            if len(date_parts) < 3:
                continue
            while len(date_parts) > 3:          # даже если начало строки будет корректным - двигаемся дальше
                date_parts.pop(3)
            try:
                date_parts = [int(el) for el in date_parts]
            except:
                pass
            else:
                result = date_parts
        return result

    # Искомое разбиение строки даты на числовые составляющие в методе класса (с полноценным использованием cls!)
    # Можно возвращать их списком (даже если некорректные - главное, что преобразовались в три числа)
    # Или вернуть None, если строка была некорректной.
    # Можно также благодаря cls создать и возвратить полноценный объект класса Date (см. дополнительный параметр)
    # Или вернуть список числовых составляющих даты, если они в итоге оказались некорректными числами

    @classmethod
    def extract_parts_from_date_string(cls, date_str, create_data_object_if_valid = True):
        cls.__DateParts = cls.__get_date_parts(date_str)
        if cls.__DateParts:
            if create_data_object_if_valid and cls.__check_date_parts(cls.__DateParts):
                return cls(date_str)
            else:
                return cls.__DateParts
        else:
            return None



# Проверка статического метода класса

def check_date_class_static_method(date_str):
    global true_dict
    print(f"Строка даты '{date_str}' {true_dict[Date.is_valid_date_string(date_str)]}")

# Проверка метода класса

def check_date_class_method(date_str):
    global true_dict
    date_object = Date.extract_parts_from_date_string(date_str)
    print(f"Строка даты '{date_str}' {true_dict[Date.is_valid_date_string(date_str)]}")

true_dict = {True: "действительная", False: "недействительная"}

# Основная функция

print('\nСтатический метод класса Date - проверка строки даты на корректность:')
print('---------------------------------------------------------------------')
check_date_class_static_method('28-02-2000')
check_date_class_static_method('29-02-2000')
check_date_class_static_method('29/02/1900')
check_date_class_static_method('29/02/1904')
check_date_class_static_method('12.12.1966')
check_date_class_static_method('12.13.1966')
check_date_class_static_method('31-06-2002')
check_date_class_static_method('30-06-2002')
check_date_class_static_method('Новый Год!')

print('\nМетод класса Date - проверка разбиения строки даты на числовые составляющие:')
print('----------------------------------------------------------------------------')
s_date = 'Новый Год!'
print(f"1) Строка с некорректными данными '{s_date}'. Результат разбиения:")
print(f"\t- без создания объекта класса из 'cls' - {Date.extract_parts_from_date_string(s_date, False)}")
print(f"\t- с созданием объекта класса из 'cls'  - {Date.extract_parts_from_date_string(s_date)}")
s_date = '31-06-2002'
print(f"2) Недействительная дата в строке '{s_date}'. Результат разбиения:")
print(f"\t- без создания объекта класса из 'cls' - {Date.extract_parts_from_date_string(s_date, False)}")
print(f"\t- с созданием объекта класса из 'cls'  - {Date.extract_parts_from_date_string(s_date)}")
s_date = '30-06-2002'
print(f"3) Действительная дата в строке '{s_date}'. Результат разбиения:")
print(f"\t- без создания объекта класса из 'cls' - {Date.extract_parts_from_date_string(s_date, False)}")
print(f"\t- с созданием объекта класса из 'cls'  - {Date.extract_parts_from_date_string(s_date)}")
print(f"4) Простое создание объекта класса Date вызовом конструктора:")
s_date = '28-02-1900'
print(f"\t- из строки с действительной датой '{s_date}'   - {Date(s_date)}")
s_date = '29-02-1900'
print(f"\t- из строки с недействительной датой '{s_date}' - {Date(s_date)}")
s_date = 'Новый Год!'
print(f"\t- из строки с некорректными данными '{s_date}'  - {Date(s_date)}")


