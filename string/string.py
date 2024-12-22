a1 = 'John'
a2 = "Karter"
a3 = """sumary_line
Keyword arguments:
argument -- description
Return: return_description
"""

a4 = "п'ятниця"

#  str()
r = [1,2,3,4]
t = str([1,2,3,4])
# print(type(t))

w = '123456'

# print(int(w))

u = 'ABCDEFGHIJK'

# print(u[-1])

# Створити рядок, який складається з імені і прізвища учня (Ivanov Ivan).
# Порівняти, чи перша літера імені співпадає з першою літерою прізвища і вивести відповідне повідомлення.
# При отриманні літери прізвища використати від’ємний індекс.

name = 'Mykhaylo Honyk'

# if name[0] == name[-5]:
#     print('bukvi odnakovi')
# else:
#     print('ne odnakovi')


# slice(start : end +1 : step)

p = 'aquapark'

# print(p[0:3]) # перші три символи
# print(p[:3]) # перші три символи

# print(p[::]) # всі символи

# print(p[3:]) # від третього символа до кінця

# print(p[2:4]) # від 2 індекса до 4

# print(p[::2]) # кожен другий

# print(p[::-1]) # від кінця до початку (зворотній напрямок)


# змінювання рядка

y = 'Hello'
# y[0] = 'K'
# print(y)


a = 'Hello '
b = 'World'
# print(a + b ) # конкатенація - склеювання рядків


# print(a * 100) # реплікація - повторення рядка за допомогою оператора *

d = '#'
size = d * 9

# print(f'{size} SLOVO {size}')

text = 'Jingle bells, jingle bells \nJingle all the way \nOh, what fun it is to ride \nIn a one horse open sleigh'
# print(text)


l = 'Hakuna, matata'

# print(len(l))


# for i in text:
#     print(i, end= ' ')

# Створіть програму, яка приймає від користувача дві строки та перетворює їх у список, 
# де перший елемент — це перша літера першої строки, 
# другий елемент — друга літера першої строки, 
# третій елемент — перша літера другої строки, 
# четвертий — друга літера другої строки і т.д. Виведіть цей список.

inp = input("Enter 1st word: ")
inp2 = input("enter 2nd word: ")

lst = []

max_len = max(len(inp), len(inp2))


for i in range(0, max_len + 1, 2):
    print(i)