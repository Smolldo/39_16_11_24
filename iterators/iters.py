lst = [1,2,3,4,5,6,7]

# for i in lst:
#     print(i)


iterator = iter(lst)

print(next(iterator))
print(next(iterator))



from itertools import count

counter = count(start= 10)

print(next(counter))
print(next(counter))


# count(), cycle(), repeat() - генерація нескінченних послідовностей


# Створіть ітератор, який буде ітерувати по кожному символу у заданому рядку.

s1 = 'Hello, world!'

iterator = iter(s1)

# print(next(iterator))

# for i in iterator:
#     print(i)


class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def about(self):
        print(f'this is {self.model} {self.brand}!!!!')
        

car1 = Car('Toyota', 'Camry')
car2 = Car('Mitsubishi', 'Lancer')


# car1.about()


class Polygon:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def square(self):
        return f'area of square = {self.length ** 2}'
    
    def rectangle(self):
        return f'area of rectangle = {self.length * self.width}'
    


poly1 = Polygon(23, 12)

print(poly1.rectangle())
print(poly1.square())


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num


lich = Countdown(10)

for i in lich:
    print(i)