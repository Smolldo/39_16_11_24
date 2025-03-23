# Напишіть функцію, яка приймає число та повертає його квадрат.

# class Car:
#     def __init__(self, model, brand, year):
#         self.model = model
#         self.brand = brand
#         self.year = year

#     def start(self):
#         print(f'{self.brand} {self.model} {self.year} start engine')

#     def stop(self):
#         print(f'{self.brand} {self.model} {self.year} stop engine')


# car1 = Car('lancer', 'mitsubishi', 2012)
# car2 = Car('Kodiak', 'Skoda', 2023)


# car1.start()
# car2.stop()




class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print(f'{self.name} видає звук')

    def describe(self):
        print(f'{self.name} належить до виду {self.species}')


dog = Animal('Sharik', 'pes')
cat = Animal('Rizhik', 'kit')

# dog.sound()
# cat.describe()
    

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 

    def read(self):
        print(f'чттаю книгу "{self.title}"')

    def add_pages(self, extra_pages):
        self.pages += extra_pages
        print(f'було додано {extra_pages} сторінок. поточна кількість сторінок: {self.pages}')

book1 = Book('Star Wars', 'George Lukas', 500)

# book1.read()
# book1.add_pages(50)


class Car:
    def __init__(self, brend, fuel):
        self.brend = brend
        self.fuel = fuel

    def drive(self, distance):
        fuel_needed = distance * .05  # 0.05
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f'{self.brend} проїхав {distance} км')
        else:
            print(f'недостатньо пального на {distance} км')

    def refuel(self, amount):
        self.fuel += amount
        print(f'було додано {amount} пального')

car1 = Car('Toyota', 10)

car1.drive(250)
car1.refuel(10)
car1.drive(250)
    