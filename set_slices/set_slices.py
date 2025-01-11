# lorem ipsum ->  ore
#slice [start: end: step]


s = 'Lorem'
# print(s[1 : 4])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numbers[:11:2])

# print(numbers[1:11:2])

# print(numbers[2:11:3])

# Заданий рядок, який містить ім’я та прізвище користувача, що розділені пробілом:
# pip = 'Ivan Ivanov' delimiter = ' ' Написати програму з використанням зрізів, яка виокремить ім’я та прізвище.

pip = 'I Stepanov'
delimiter = ' '

pos = pip.find(delimiter)
# pos1 = pip.index(' ')
# print(pos)
# print(pos1)

name = pip[: pos]
surname = pip[pos:]

# print(name + ',' + surname)


# Задано список номерів мобільних телефонів: phones = ['+38(067) 999-99-99', '+38(066) 999-99-99','+38(067) 888-88-88', 
# '+38(068) 777-77-77'] Вважаючи, що всі номери записані у форматі +38 (код) 111-11-11, порахувати кількість абонентів оператора, 
# що має коди «067», «097», «068»

phones = ['+38(067) 999-99-99', '+38(066) 999-99-99','+38(067) 888-88-88', '+38(068) 777-77-77']

opers = ['067', '097', '068']

counter = 0

for n in phones:
    ops = n[4: 7]
    if ops in opers:
        counter += 1

# print(counter)



a = set('hello')
# print(a)

b = {1, 1, 2, 2,3,4}
# print(b)


# add(elem)

c = {1,2,3}
c.add('a')
# print(c)

#remove(elem)

# c.remove(7)
# print(c)


# discard(elem)
c.discard(8)
# print(c)


a = set('hello')  #  h e l o
b = set('hi there') # h i t e r ' '

print(a ^ b) # симетрична різниця. повертає всі елемени множин окрім спільних
# print(a.symmetric_difference(b))

#intersection - перетин. спільні для двох множин елементи
a = set('hello')  #  h e l o
b = set('hi there') # h i t e r ' '

print(a & b) #  & = і
# print(a.intersection(b))


# union - об'єднання

a = set('hello')  #  h e l o
b = set('hi there') # h i t e r ' '

print(a.union(b))
print(a | b)


#difference - різниця

a = set('hello')  #  h e l o
b = set('hi there') # h i t e r ' '

print(b.difference(a))
