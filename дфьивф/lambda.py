lambda x : x * 2

def f(x):
    return x * 2

# print(f(3))

multiply = lambda x, y: x * y

# print(multiply(4,6))

spisok = [2, 3, 4, 5, 6, 7, 8, 9]

squared = list(map(lambda x: x ** 2, spisok))
# print(squared)

max_n = lambda x, y: x if x > y else y

# print(max_n(9,6))


concat = lambda s1, s2: s1 + ' - ' + s2

# print(concat('hello', 'world'))

# Створіть лямбда-функцію для обчислення куба числа.
cubed = lambda x: x ** 3
# print(cubed(4))


# Напишіть лямбда-функцію, яка перевіряє, чи є одне число кратним іншому, і перевірте її для різних пар чисел.

is_cratne = lambda x,y: x % y == 0
# print(is_cratne(10, 3))

# Створіть лямбда-функцію для обчислення середнього арифметичного двох чисел.

sered = lambda x, y: (x + y) / 2
# print(sered(4,5))

# Напишіть лямбда-функцію для конвертації температури з Цельсія в Фаренгейт і навпаки.
cTOf = lambda x: x * 9/5 + 32

# print(cTOf(2))

fTOc = lambda x: (x - 32) * 5//9

# print(fTOc(35))

# Використовуючи теорему Піфагора, створіть лямбда-функцію для обчислення довжини гіпотенузи прямокутного трикутника за даними катетами.
from math import sqrt
h = lambda x, y: sqrt(x**2 + y**2)

# print(h(3,4))

# Створіть лямбда-функцію для перевірки, чи є заданий рік високосним. 
# Високосний рік ділиться на 4, але якщо він ділиться на 100, то має ділитися і на 400.

is_vis = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# print(is_vis(2022))

# Напишіть лямбда-функцію для визначення максимального з трьох чисел.

mn = lambda a,b,c: max(a,b,c)

print(mn(3,2,4))