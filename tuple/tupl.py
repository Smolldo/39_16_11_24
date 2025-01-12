a = (1,2,3,4, 'd', 'd', [1,2,3,4], True)

# b = tuple()


# print(a[2:5])

# for i in a:
#     print(i)


b = (1,2,3)
c = (4,5,7)
d = b + c
# print(d)

# print( d * 4)


r = (1,1,1,1,1,1,1,1,1,1,1,2)
# print(r.count(2))

# print(r.index(2))

# Створіть функцію, яка приймає два кортежі та повертає кількість елементів, які зустрічаються в обох кортежах

def common(t1, t2):
    counter = 0
    for i in set(t1):
        for j in set(t2):
            if j == i:
                counter += 1
            
    return counter


t1 = (1,2,3,4,5,6,7,8,9)
t2 = (2,3,12, 3)

# print(common(t1,t2))


# Напишіть функцію, яка приймає кортеж чисел та повертає кортеж, що містить мінімальний та максимальний елементи.


def min_max(x):
    return (max(x), min(x))

nums = (1,2,3,4,5)

# print(min_max(nums))


def rvrs(x):
    return x[::-1]

# print(rvrs(nums))


# Напишіть функцію, яка перевіряє, чи всі елементи в кортежі є унікальними

def uniq(x):
    return len(x) == len(set(x))
n = (1,1,1,1,1,2,3,4)

# print(uniq(n))


# Напишіть функцію, яка об'єднує два кортежі в один.

def ob(x, y):
    return x + y

print(ob(nums, n))









my_tuple = ('p', 'y', 't', 'h', 'o', 'n')

print(my_tuple[-2])

tuple([1,2,3])