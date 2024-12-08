lst = list()
lst1 = []

lst2 = [1, 2, 3, 4.45, 'December', True, [1,2,3], (4,5,6)]

# Створити список, який буде містити послідовність символів.

a = ['a', 'b', 'c']

# Створити список, який буде містити числові значення.

a = [1, 2, 3, 4, 5]

# Створити список, який буде містити ім’я, прізвище і кількість повних років учня.
b = ['Honyk', 'Mykhailo', 25]

# c = [True, False, False, False, True]

products = ['eggs', 'coke', 'chips', 'cheese', 'grapes', 'lemon']

# print(products[0])
# print(products[3])
# print(products[-1])

#slice - зріз    products[start : end -1 : step]

# print(products[0:3]) # від початку до 3 елемента
# print(products[:3]) # від початку до 3 елемента
# print(products[:]) # повертає весь список
# print(products[3:]) # від 3 елементу до кінця
# print(products[::2]) # від початку до кінця з кроком 2
# print(products[::-1]) # від початку до кінця обернене




vkl = [1, 2, 3, [4, 5, 6, [7, 8,], 9], 10, 11, 12]

# print(vkl[2])
# print(vkl[3][1])
# print(vkl[3][3][0])


# Написати програму, що рахує суму всіх елеметів у списку.

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma = 0

for i in spisok:
    suma += i

# print(suma)


# Написати програму, що дістає максимальне число зі списку.

spisok = [1, 2, 3, 4, 45, 5, 6, 7, 999, 8, 9, 10]

max_znach = spisok[0]

for i in spisok:
    if i > max_znach:
        max_znach = i

# print(max_znach)


# Піднести кожен із елементів списку до кубу

sp = [1, 2, 3, 4, 5]

for i in sp:
    print(i ** 3)


sp1 = [i ** 3 for i in sp]
print(sp1)


# Написати програму, що дістає мінімальне число зі списку.

spp = [2, 3, 4, -3, 5, -3, 0, 9]

min_znach = spp[0]

for i in spp:
    if i < min_znach:
        min_znach = i

print(min_znach)