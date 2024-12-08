lst = [1,2,3,4]

l1 = list((1,2,3,4,5,6))
# print(l1)


l2 = [1,2,3,4]
#append() - додає елемент в кінець списку
l3 = ['a', 'b']
l2.append(l3)
# print(l2)

# clear() - очищає список
l2.clear()
# print(l2)

# remove() - видаляє елемент зі списку. видає помилку, якщо елемента немає. працює не за індексами, а за ім'ям елемента

prods = ['kovbasa', 'sir', 'khlib', 'chipsi']
# print(prods)
prods.remove('sir')
# print(prods)


# pop() - повертає індекс і видаляє елемент. по замовчуванню видаляє -1 елемент(останній). працює за індексами
prods = ['kovbasa', 'sir', 'khlib', 'chipsi']

prods.pop(2)

# print(prods)

# del - видалє елемент за індексом

prods = ['kovbasa', 'sir', 'khlib', 'chipsi']

del prods[0]
# print(prods)


# exttend() - доповнює один список іншим
l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2)
# print(l1)


# insert(index, value) - вставляє новий елемент на вказаний індекс

c = ['a', 'b', 'c']

c.insert(1, 'd')

# print(c)

# index() - знаходить індекс першого входження елемента Х

d = ['a', 'b', 'c', 'c', 'c', 'd']

# print(d.index('c'))


# count() - підраховує кількість входжень елемента в список
d = ['a', 'b', 'c', 'c', 'c', 'd']

# print(d.count('c'))

# sort() - сортує список

sp = [1, 56, 2, 87, 34, -8]
sp.sort(reverse=True)
# print(sp)


# reverse() - перевертає список у зворотньому напрямку, але НЕ сортує

sp = [1, 56, 2, 87, 34, -8]
sp.reverse()
# print(sp)


#copy() - копіює список
a = [1,2,3]
a_copy = a.copy()

# print(a == a_copy)


# len() - lenght - довжина списку - загальна кількість елементів

# print(len(sp))


t = [1,2,3,4,5]

# if 6 in t:
#     print('+++++')
# else:
#     print('no')

# for i in t:
#     print(i, end=' ')



# enumerate(iterable, start = 0)

products = ['apple', 'grapes', 'lemon', 'lime', 'candys']

# for index, product in enumerate(products, 1):
#     print(index, product)

# for i in range(len(products)):
#     print(i + 1, products[i])

# Написати програму, яка видалить зі списку 0-й, 5-й і 7-й елементи зі списку
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del n[7]
del n[5]
del n[0]

# print(n)

# Створити програму, яка приймає список слів та повертає список слів у зворотньому порядку.
words = ['abc', 'def', 'ghi', 'jkl']
words.reverse()
print(words)
