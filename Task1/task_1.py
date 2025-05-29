text = "Программирование — это про решения. Рррррреволюция в подходах происходит редко, но рррраз за разом мы соверррррррррррррршенствуемся"

max_count = 0

for word in text.split():
    count = 0
    max_word_count = 0
    for char in text:
        if char == 'р' or char == 'Р':
            count = count + 1
            if count > max_count:
                    max_count = count
        else:
            count = 0

    if max_word_count > max_count:
        max_count = max_word_count

print("Max count of 'р':", max_count)