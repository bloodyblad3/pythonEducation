from data_processing import count_ids

def input_data():
    data = dict()
    Id = count_ids("students.txt") 
    data["id"] = Id
    data["surname"] = input('Введите Фамилию: ')
    data["name"] = input('Введите Имя: ')
    data["class"] = input('Введите Класс: ')
    data["status"] = input('Введите Статус: ')
    data["row"] = input('Введите Ряд: ')
    data["col"] = input('Введите Номер парты: ')
    data["city"] = input('Введите Город: ')
    data["street"] = input('Введите Улица: ')
    data["house"] = input('Введите Дом: ')
    return data