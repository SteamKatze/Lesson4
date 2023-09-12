# Отримуємо рядок від користувача
input_string = input("Введіть рядок: ")

# Спершу виводимо третій символ рядка
print("Третій символ рядка:", input_string[2])

# Виводимо передостанній символ рядка
last_index = len(input_string) - 2
print("Попередній символ рядка:", input_string[last_index])

# Виводимо перші п'ять символів рядка
print("Перші п'ять символів рядка:", end="")
for i in range(5):
    print(input_string[i], end="")

# Виводимо рядок без двох останніх символів
print("\nРядок без двох останніх символів:", end="")
for i in range(len(input_string) - 2):
    print(input_string[i], end="")

# Виводимо символи з парними індексами
print("\nСимволи з парними індексами:", end="")
for i in range(0, len(input_string), 2):
    print(input_string[i], end="")

# Виводимо символи з непарними індексами, починаючи з другого символу
print("\nСимволи з непарними індексами:", end="")
for i in range(1, len(input_string), 2):
    print(input_string[i], end="")

# Виводимо рядок у зворотному порядку
print("\nРядок у зворотному порядку:", end="")
for i in range(len(input_string) - 1, -1, -1):
    print(input_string[i], end="")

# Виводимо символи через один у зворотному порядку, починаючи з останнього
print("\nСимволи через один у зворотному порядку:", end="")
for i in range(len(input_string) - 1, -1, -2):
    print(input_string[i], end="")

# Виводимо довжину рядка
print("\nДовжина рядка:", len(input_string))