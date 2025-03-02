print('hello world')

#all

a = [1,2,3,4,5,6, 'sdfsd', [1,2,3]]

print(all(a))

# any

b = [1, [],'',0]

print(any(b))


# sorted

c = [6,2,9,7,1,0,3,4]


print(sorted(c, reverse=True))

# Завдання 1.
# Створіть скрипт, який зчитує список цілих чисел (можна використовувати генератор випадкових чисел), 
# використовує all() для перевірки, чи всі числа позитивні, а потім застосовує sorted() для сортування цих чисел за зростанням.

import random

numbers = [random.randint(-5,20) for _ in range(10)]
print(numbers)

if all(i > 0 for i in numbers):
    print('all numbers are positive')
else:
    print('not all are positive')

sorted_numbers = sorted(numbers)
print(sorted_numbers)


# Завдання 3. 
#Використовуйте sorted() для сортування списку словників за кількома ключами 
# (наприклад, спочатку за іменем, потім за віком, якщо імена однакові). Включіть параметри key та reverse для зміни порядку сортування.

people = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Alex', 'age': 30},
    {'name': 'Alex', 'age': 17},
]

sorted_people = sorted(people, key= lambda x: (x['name'], -x['age']))
print(sorted_people)

for i in sorted_people:
    print(i)


# Напишіть програму, яка дозволяє користувачеві ввести рядок символів та використати any() для перевірки, 
# чи містить рядок будь-які голосні букви. Виведіть результат перевірки.

inp = input('Enter smth: ')

vowels = 'eyuioa'

print(any(i in vowels for i in inp))

# перевірити чи всі елементи списку мають довжину більше 6 символів
g = ['asdadadaa', 'asdfsadf', 'adgfgha']

print(all(len(i) > 6 for i in g))

#відсортувати за кількістю фруктів
data = [("apple", 2), ("banana", 1), ("cherry", 3)]