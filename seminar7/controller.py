import os
from show_data import print_data
from insert_data import insert_data
from export_data import export_data

def input_data():
    surname = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    note = input("Введите примечание: ")
    return [surname, first_name, phone_number, note]

def input_separator():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice():
    choice = input('''Введите опцию > 
                   1 - импорт информации
                   2 - вывод информации в справочнике
                   3 - выход''')
    while True:
        if choice < 1 or choice > 3:
            print("Введите верную опцию.")
        elif choice == 1:
            sep = input_separator()
            insert_data(input_data, sep)
        elif choice == 2:
            data = export_data()
            print_data(data)
        else:
            print("Выход из справочника...")
            break
