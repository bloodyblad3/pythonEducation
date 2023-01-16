# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def input_string(text: str) -> str:
    string = input(text)
    return string

def remove_part(text: str, part: str):
    return "".join(filter(lambda pattern: part not in pattern, text.split()))

text = input_string("Введите текст через пробел:\n")
print(f"Исходный текст > {text}")
part = "абв"
result_text = remove_part(text, part)
print(f"Измененный текст без '{part}' > {result_text}")