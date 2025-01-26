d = dict()
d1 = {}

chars = {
    'a': 1,
    'b': 2,
}
# .get()

# c = chars.get('v', 'nema takogo')
# print(c)


chars['c'] = 3
# print(chars)


# .pop()
# p = chars.pop('b')
# print(chars)
# print(p)



# .clear()
# chars.clear()

# .update()

chars = {'a': 1, 'b': 2,}

chars.update({'d': 4})

# print(chars)

# .copy()
# chp = chars.copy()
# print( chp == chars)

# Створити словник «місяці».
# В якості ключа виступає порядковий номер місяця, в якості значення – його назва.

monthes = {
    1 : 'January',
    2 : 'February',
    3 : 'MArch',
    4 : 'April'
}
# print(monthes[2])


#курси валют

money = {
    'USD': 42.15,
    'EUR': 45.01,
    'PLN': 12.34
}


fruits = {
    'watermelon': 222,
    'banana': 124,
    'grapes': 444
}

# print(fruits['banana'])

# Створіть словник з назвами міст та їх кількістю населення. Виведіть на екран назву міста з найбільшою кількістю населення.

cities = {
    'Kyiv': 1500000,
    'Mykolaiv': 500000,
    'Ternopil': 250000,
}

# print(max(cities, key=cities.get))

# Напишіть програму, яка дозволяє користувачам реєструватися на сайті та зберігає їх дані у словнику. 
# Ключ — ім'я користувача, а значення — пароль.

# usr = input('Enter usr name: ')
# pswd = input('Enter password')

user = {}

# user[usr] = pswd

# print(user)

# Перетворення рядка у словник. Напишіть програму, яка перетворює рядок у словник, де ключ — перша буква слова, 
# а значення — саме слово. Рядок вводиться користувачем з клавіатури.

# txt = input('enter some text: ')

# words = txt.split()

# wd = {w[0]: w for w in words}

# print(wd)


# Гра "Хто є хто". У цій грі користувач повинен відгадати тварину, яку ми загадали.
#  Ми надаємо користувачеві опис цієї тварини, включаючи її колір, розмір, дії і т.д. 
# Користувач повинен ввести свій варіант тварини, а програма повинна повідомити користувачеві, чи він відгадав правильно, чи ні.

animals = {
    'cat': 'ця тварина мала, пухнаста, мявкає',
    'dog': 'ця тварина трохи більша, пухнаста гавкає'
}

import random

# ani, descr = random.choice(list(animals.items()))

# print(descr)

# inp = input('Enter zdohadku: ')

# if ani == inp:
#     print('Ви вгадали')
# else:
#     print('ви не вгадали')

# Напишіть програму, яка приймає від користувача список з імен та оцінок, та обчислює 
# середній бал для кожного учня. Результат виводиться у вигляді словника, де ключ — ім'я учня, а значення — середній бал.

def average(scores):
    return round(sum(scores) / len(scores))


students = {}

print('Enter name then scores')

while True:
    stud = input('Enter data: ')
    if not stud:
        break

    data = stud.split()
    name = data[0]
    scores = [int(score) for score in data[1:]]

    students[name] = average(scores)

print(students)