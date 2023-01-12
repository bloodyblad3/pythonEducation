# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def input_string(text: str) -> str:
    string = input(text)
    return string

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input_string("Введите текст для кодировки: ")
coded = coding(s)
decoded = decoding(coded)
print(f"Текст после кодировки: {coded}")
print(f"Текст после дешифровки: {decoded}")