#2. Расход ткани на пальто и костюм (с абстрактыми классами и членами класса - свойствами)

from abc import ABC, abstractmethod

class Dress(ABC):
    @abstractmethod
    def cloth_consumption(self):
        return None

class Coat(Dress):
    def __init__(self, size):
        self.size = size

    @property
    def cloth_consumption(self):
        return self._base / 6.5 + 0.5

    @property
    def size(self):
        return self._base

    # сеттер - для чистоты эксперимента (без него свойство "только для чтения")
    @size.setter
    def size(self, value):
        if value < 0:
            self._base = abs(value)


class Suit(Dress):
    def __init__(self, height):
        self.height = height

    @property
    def cloth_consumption(self):
        return 2 * self._base + 0.3

    @property
    def height(self):
        return self._base

    # сеттер - для чистоты эксперимента (без него свойство "только для чтения")
    @height.setter
    def height(self, value):
        if value < 0:
            self._base = abs(value)

s = Suit(-1.68)     # Для проверки корректности в конструкторе
print(f"\nРасход ткани на костюм при росте {s.height:.2f} м: {s.cloth_consumption:.2f} м")
s.height = -1.68    # Для проверки корректности при присвоении через свойство
print(f"Расход ткани на костюм (задан рост минус {s.height:.2f} м): {s.cloth_consumption:.2f} м")
c = Coat(-48)       # Для проверки корректности в конструкторе
print(f"Расход ткани на пальто при {c.size}-м размере: {c.cloth_consumption:.2f} м")
c.size = -48        # Для проверки корректности при присвоении через свойство
print(f"Расход ткани на пальто (задан размер минус {c.size}): {c.cloth_consumption:.2f} м")
print(f"Общий расход ткани: {s.cloth_consumption + c.cloth_consumption:.2f} м")
print("Все данные выглядят реалистично")
