def count_down(x):
    while x > 0:
        yield x
        x -= 1


numbers = (x*x for x in range(10) if x % 2 == 0)
# print(numbers)


def simole():
    yield 1
    yield 2
    yield 3

gen = simole()

# print(next(gen))


# Знайти квадрати парних чисел у списку

numbers = [1,2,3,4,5,6,7,8,9,10]

squares = (x ** 2 for x in numbers if x % 2 == 0)
# print(list(squares))
# for i in squares:
#     print(i)


# Генерувати нескінченну послідовність починаючи з певного числа

def infinity(start):
    return (start + x for x in range(0, int(1e10)))


sequence  = infinity(7)
print(next(sequence))
print(next(sequence))
print(next(sequence))



# Обчислення суми усіх парних чисел у списку

nums = [1,2,3,4,5,6,7,8,9,10]

sums = sum(x for x in nums if x % 2 == 0)
# print(sums)

# Виведення всіх унікальних слів з тексту у верхньому регістрі
text = "Hello world, hello Python, hello Coding"

uniq = set(w.upper() for w in text.split())

for w in uniq:
    print(w)


# Створіть генератор, що виробляє нескінченну послідовність парних чисел, починаючи з нуля.
