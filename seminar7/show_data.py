def print_data(data):
    if len(data) > 0:
        for item in data:
            print(f'''Фамилия: {item[0]}    Имя: {item[1]}
                      Телефон: {item[2]}    Примечание{item[3]}''')
    else:
        print("В справочнике нет данных!")
