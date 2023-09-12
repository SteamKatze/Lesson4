# Користувач вводить текст
input_text = input("Введіть текст: ")

# Змінюєм текст так, щоб кожне речення починалося з великої літери
sentences = input_text.split(".")
formatted_text = ". ".join(sentence.capitalize() for sentence in sentences)

# Рахуємо скільки разів цифри зустрічаються у тексті
digit_count = sum(1 for char in formatted_text if char.isdigit())

# Рахуємо скільки разів розділові знаки зустрічаються в тексті
punctuation_count = sum(1 for char in formatted_text if char in '.,;:!?()[]{}<>')

# Рахуємо кількість знаків оклику в тексті
exclamation_count = formatted_text.count('!')

# Виводимо результати
print("Текст з великою першою літерою у кожному реченні:")
print(formatted_text)
print("Кількість цифр у тексті:", digit_count)
print("Кількість розділових знаків у тексті:", punctuation_count)
print("Кількість знаків оклику у тексті:", exclamation_count)