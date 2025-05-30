# Дан текст. Подсчитать, сколько одинаковых символов встречаются в нем. Вывести их на экран.

text = input("Введите текст: ")

char_count = {} # Словарь для хранения количества повторения

char_index = 0 # Начальная поциция символа в текста

while char_index < len(text):
    current_char = text[char_index]
    
    if current_char in char_count:
        char_count[current_char] = char_count[current_char] + 1
    else:
        char_count[current_char] = 1
    
    char_index = char_index + 1

keys = list(char_count.keys())

i = 0

print("Повторяющиеся символы:")
while i < len(keys):
    symbol = keys[i]
    count = char_count[symbol]
    if count > 1:
        print(f"Символ '{symbol}' встречается {count} раз(а).")

    i = i + 1

