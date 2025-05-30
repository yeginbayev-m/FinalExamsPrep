# Дан текст. Удалить из нее те слова, которые содержат хотя бы одного слога «ка».
text = "Практический опыт показывает, что рамки и место обучения кадров позволяет оценить значение ключевых компонентов планируемого..."


char_index = 0
current_word = ""
words = []

while char_index < len(text):
    current_char = text[char_index]

    if current_char != ' ': # обычно символы в ' ', а строки в ""
        current_word = current_word + current_char
    else:
        if current_word != "":
            words.append(current_word)
            current_word = ""
    char_index = char_index + 1

# Если текст не заканчивается пробелом, последнее слово нужно добавить вручную
if current_word != "":
    words.append(current_word)

# удаление слова с "ка"

filtered_words = []
word_index = 0

while word_index < len(words):
    word = words[word_index]

    if 'ка' not in word:
        filtered_words.append(word)

    word_index = word_index + 1

result_text = ""
i = 0

while i < len(filtered_words):
    result_text = result_text + filtered_words[i]

    if i < len(filtered_words) - 1:
        result_text = result_text + " " # добавление пробела между словами
    
    i = i + 1 # i += 1

print(f"""Исходный текст: 
      {text} 
      
Результат после удаления слов, содержащих 'ка':
      
      {result_text}
""")