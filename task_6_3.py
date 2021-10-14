#3. Работник и его "атрибуты"

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

deep_purple = [Position('Ritchie', 'Blackmore', 'solo-guitar', 12500, 3350),
               Position('Jon', 'Lord', 'keyboard', 12800, 3500),
               Position('Jan', 'Gillan', 'vocal', 12600, 3300),
               Position('Roger', 'Glover', 'bass-guitar', 12400, 3400),
               Position('Jan', 'Paice', 'drums', 12400, 3200)]

print("\n\tDo You know the most famous staff of 'Deep Purple' since 1971? Money are for the homework only :-)\n")
for mus in deep_purple:
    print(f"{mus.position:>20}:\t{mus.get_full_name():<20} (last_income - {mus.get_total_income()}"
          f" ({mus._income['wage']} + {mus._income['bonus']}) pounds)")

