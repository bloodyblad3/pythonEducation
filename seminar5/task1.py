# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def input_string(text: str) -> str:
    string = input(text)
    return string

def del_words(text, symb = "абв"):
    lst = [i for i in text.split() if symb not in i]
    return lst
    
txt = input_string("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
result_text = del_words(txt)
print(f"Результат: {' '.join(result_text)}")