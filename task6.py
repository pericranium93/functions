def text(word_text):  # Не совсем понял зачем функция, но на всякий случай сделал
    word_text = word_text.title().split()
    word_text = ' '.join(word_text)
    return word_text


# Вариант 1
words = input('Введите вашу фразу').title().split()
words_list = ' '.join(words)
print(words_list)

# Вариант 2
print(text(input('Введите слово или фразу')))
