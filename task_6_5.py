#5. Разное поведение канцелярских принадлежностей

class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print(f"В Ваших руках {self._title}. Золотое перо!")

class Pencil(Stationery):

    def draw(self):
        print(f"Вы взяли {self._title}. {str(self._title).title()} поможет Вам создать эскиз.")

class Handle(Stationery):

    def draw(self):
        print(f"{str(self._title).title()} нанесёт метку на CD-диск, не повредив его поверхность.")

s = Stationery("пишущая сущность")
s.draw()
print(f"{str(s._title).capitalize()} - на Ваш выбор.")
p = Pen("ручка 'Паркер'")
p.draw()
n = Pencil("карандаш")
n.draw()
h = Handle("маркер")
h.draw()
