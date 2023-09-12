# Користувач вводить текст
input_string = input("Введіть текст: ")

# Ініціалізуємо лічильники для літер і цифр
letter_count = 0
digit_count = 0

# Аналізуємо символи у рядку
for char in input_string:
    # Визначаємо чи є символ літерою або цифрою
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

# Виводимо результати
print("Кількість літер у рядку:", letter_count)
print("Кількість цифр у рядку:", digit_count)