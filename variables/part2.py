# name = input('Enter ur name: ')

# print('Hello ', name)



# str()  int()  float()  bool()

# number = input('Enter number: ') # 12   '12'
# print(23 + int(number))


name = 'John'

# print(int(name))

is_true = 'abba'
# print(bool(is_true))


# Оголосити дві змінні, одна з яких дорівнюватиме довільному числу. 
# Інша — значення попередньої змінної збільшене на 10.

num1 = 34
num2 = num1 + 10
# print(num1, num2)

# Оголосити змінну - довжина сторони квадрату. Обчислити площу квадрату і вивести на екран.

a = 10
S = a ** 2
# print(S)

# Оголосити змінні — радіус та число P (3.14). Визначити довжину кола та площу круга.

r = 5
P = 3.14
S = r**2 * P
L = 2 * r * P
# print(L, S)

# Оголосити змінні — 3 кути трикутника (їхня градусна міра). 
# Оголосити наступну змінну is_valid, аби отримати булеве значення (is_valid = angle1 + angle2 + angle3 == 180)

angle1 = 100
angle2 = 40
angle3 = 40

is_valid = angle1 + angle2 + angle3 == 180
# print(is_valid)

# Відомо, що X кг цукерок коштує A карбованців. Визначити, скільки коштує 1 кг та Y кг цих же цукерок.

x = float(input("Enter kgs: "))
a = float(input('Enter price: '))
y = float(input('Enter another kgs: '))

price_kg = a / x
Y_kg = price_kg * y

# print(f'1kg of konfety = {price_kg}. a Y kg = {Y_kg:.2f}')


# З початку доби пройшло N секунд (N — ціле). Знайти кількість повних хвилин з початку доби.
