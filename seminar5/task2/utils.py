def is_num(num):
    try:
        num = int(num)
        return num
    except ValueError:
        return False

def input_number(text: str):
    num = ''
    while not num:
        num = is_num(input(text))
    return num

def max_candies(text: str, max_candies: int):
    while True:
        max_for_step = input_number(text)
        if max_for_step > max_candies:
            print("На столе меньше конфет, чем ты пытаешься взять...")
            continue
        return max_for_step
