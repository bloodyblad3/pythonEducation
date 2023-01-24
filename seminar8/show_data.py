def print_data(data):
    if len(data) > 0:
        for item in data:
            print(f'''Идентификатор: {item[0]}, Фамилия: {item[1]} Имя: {item[2]} Класс: {item[3]} Статус: {item[4]}
Город: {item[7]} Улица: {item[8]} Дом: {item[9]}
Ряд: {item[5]} Номер парты: {item[6]}\n''')
    else:
        print("В справочнике нет данных!")