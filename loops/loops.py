# for - ітеруючий (є лічільник)  while - не ітеруючий

word = 'Hello'

# for char in word:
#     print(char)


colors = ['red', 'green', 'blue', 'magenta']

# for color in colors:
#     print(color)

# numbers = [int(i) for i in input().split()] #[1, 2, 3, 4, 5, 6, 7]
suma = 0

# for i in numbers:
#     suma += i  # suma = suma + i

# print(suma)

# for i in colors:
#     print(i)
# else:
#     print('Done!')


#range - проміжок  range(start, end, step)

# 0 1 2 3 4 5 6
# for i in range(0, 7, 1):
#     print(i)

# for i in range(7):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j)


#  while condition:
#   print(sdfsd)

# a = 1

# while a <= 5:
#     print('Hello')
#     a += 1
# else:
#     print('done')

# Порахувати середнє арифметичне всіх чисел кратних 3 з певного інтервалу

# a = int(input('Enter start num: '))
# b = int(input('Enter end num: '))

# summ = 0
# count = 0

# for i in range(a, b + 1):
#     if i % 3 == 0:
#         summ += i
#         count += 1

# print(summ / count)


a = 0

# while True:
#     print(a)
#     if a > 20:
#         break
#     else:
#         a += 1


# while True:
#     n = input('Action?: ')
#     if n == 'e':
#         break


# continue
# b = 0

# while b < 6:
#     b +=1
#     if b % 2:
#         continue
#     print(b)

# Організувати безперервне введення з клавіатури чисел. Якщо число більше 20, то вивести його на екран. 
# Якщо число більше 100 — закінчити роботу програми.

while True:
    n = int(input('Enter num: '))
    if n > 100:
        break
    elif n <= 20:
        continue
    elif n > 20:
        print(n)