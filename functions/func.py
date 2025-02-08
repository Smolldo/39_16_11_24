# def func():
#     print('Hello')


def dodavannya(x, y):
    print(x + y)


# dodavannya(4,7)


def find_max(x, y):
    if x > y:
        print(x, 'is bigger')
    elif x == y:
        print('equal')
    else:
        print(y, 'is bigger')


# find_max(4, 12)

a = 9
b = 9
# find_max(a,b)



def summa(a,b):
    return a + b


# print(summa(3,4))

res = summa(8,9)

# find_max(res, 23)



# t = 10

# def func():
#     t = 5
#     print('зміна локального t на ', t)

# func()
# print('t = ', t)


x = 30

def func():
    global x
    print('znachennya x = ', x)
    x = 5
    print('x teper = ', x)

# func()
# print('x = ', x)



def test(a, b = 5, c = 10):
    print(f'a = {a}, b = {b}, c = {c}')

# test(4)
# test(c = 10, b = 23, a = 2)
# test(34, 1, 2)
# test(7, c = 222)




def total(*numbers, **phone_book):

    for num in numbers:
        print('num = ', num)

    for name, phone in phone_book.items():
        print(f'{name}: {phone}')

total(2,3,23, 5656656,4,5,6, John = 123, Katty = 322, Peter = 3423423)
