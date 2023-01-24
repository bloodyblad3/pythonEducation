from push_data import push_data
from read_data import read_data
from show_data import print_data

def run():
    choice = int(input('''Введите опцию > 
                1 - получить информацию об учениках
                2 - добавить ученика
                3 - выход\n'''))
    while True:
        if choice < 1 or choice > 3:
            print("Введите верную опцию.")
            run()
        elif choice == 1:
            data = read_data()
            print_data(data)
            break
        elif choice == 2:
            push_data()
            break
        else:
            print("Выход из справочника...")
            break
