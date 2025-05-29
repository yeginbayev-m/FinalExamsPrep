text = input("Введите текст: ")

count = 0
max_count = 0



for char in text:
    if char == 'р' or char == 'Р':
        count = count + 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print("Max count of 'р':", max_count)