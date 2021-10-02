#2. Функция с именованными параметрами и их печатью в одной строке

def pass_personal_data(first_name, second_name, birth_year, citizen_town, email_address, phone_number):
    s = str(first_name).strip() + " " + str(second_name).strip() + " " + str(birth_year).strip() + " "
    s += (str(citizen_town).strip() + " " + str(email_address).strip() + " " + str(phone_number).strip())
    return s

print(pass_personal_data(birth_year=1966, email_address='dziadok@tut.by', second_name="Тернов",
                         first_name='Евгений', phone_number="+375295733120", citizen_town='Минск'))
