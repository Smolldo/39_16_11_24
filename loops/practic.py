# Написати код який буде просити ім'я користувача до поки він його не напише

# while True:
#     name = input('Enter name: ')
#     if name.strip():            # .strip() - прибирає пробіли на початку і кінці рядка
#         print(f'hello {name}')
#         break

# Написати код який рахує суму всіх чисел в діапазоні який задав користувач
# start = int(input('Enter start: '))
# end = int(input('Enter end: '))

# summa = 0

# for i in range(start, end + 1):
#     summa += i   # suma = suma + i     1,2,3,4,5  0 + 1 = 1.    suma = 1 + 2 = 3   suma = 3 + 3  suma = 6 + 4   suma 10 + 5 = 15

# print(summa)

# Написати програму, яка виведе таблицю множення числа, яке задав користувач. Приклад (2 4 6 8 10 12 14 16 18 20)

# num = int(input('Enter number: '))

# for i in range(1, 11):
#     print(num * i)


# Написати програму, яка виведе число від -10 до -1 використовуючи цикл
# for i in range(-10, 0):
#     print(i)


# Дано змінну a = 1. Виводити a, поки a <= 15.

# a = 1
# while a <= 15:
#     print(a)
#     a += 1
# else:
#     print('a bigger than 15')

# Дано слово “Цивілізація”. За допомогою циклу порахувати скільки літер “і” містить в собі це слово.

# word = 'Цивілізація'

# count = 0

# for bukva in word:
#     if bukva == 'і':
#         count +=1  # count = count + 1   0 = 0 + 1  = 1   1 = 1 + 1  = 2
# print(count)

# Зробити попередню програму більш універсальною — Запитувати у користувача слово та літеру для пошуку.

# word = input("Enter word: ")
# letter = input('Enter letter: ')
# count = 0
# for i in word:
#     if i == letter:
#         count += 1
# print(count)


# Написати програму, яка порахує і виведе куби всіх чисел від 1 до числа, яке задасть користувач

# num = int(input('Enter num: '))

# for i in range(1, num + 1):
#     print(i ** 3)

# Дано діапазон чисел від 0 до 100. Вивести на екран лише парні числа

# for i in range(0, 101, 2):
#     print(i)

# Написати програму, яка виведе факторіал числа, яке задасть користувач (цикл while)

#  5!  = 1* 2* 3* 4* 5 = 120

num = int(input('Enter num: '))

factorial = 1

while num > 0:
    factorial *= num  # 1 * 5, 5 * 4, 20 * 3, 60 * 2, 120 * 1
    num -= 1
print(factorial)