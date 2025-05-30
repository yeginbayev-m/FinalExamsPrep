# Дан текст. Удалить из нее те слова, которые содержат хотя бы одного слога «ка».
# текст: Практический опыт показывает, что рамки и место обучения кадров позволяет оценить значение ключевых компонентов планируемого...
text = input("Введите текст: ")
words = text.split()

filtered_words = []

word_index = 0

while word_index < len(words):
    word = words[word_index]

    if 'ка' not in word:
        filtered_words.append(word)

    word_index = word_index = 1

result_text = ' '.join(filtered_words)

print(f"""Исходный текст: 
      {text} 
      
Результат после удаления слов, содержащих 'ка':
      
      {result_text}
""")
