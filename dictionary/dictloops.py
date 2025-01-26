numbers = {
 1: "one",
 2: "two",
 3: "three"
}

# for i in numbers.keys():
#     numbers[i] = 'John'
# print(numbers)


# for i in numbers.values():
#     print(i)


# for k, v in numbers.items():
#     print(k, v)



# Оголосити словник, що має наступну структуру «ключ» — номерний знак транспортного засобу 
# (наприклад «АА2565ІН»), значення «власник авто» (наприклад, Іванов Іван)
# Додати в словник два нові авто
# Знайти власника за номером автомобіля
# Обійти словник і вивести прізвища людей, які мають більше одного авто


autos = {
    'AA2565IH': 'Іван Іванов',
    'BE0988BP': 'Петро Петров',
    'BO1234BO': 'Степан Степанов'
}

autos['AT7798AO'] = 'Іван Іванов'
autos['AК5666AP'] = 'Сидір  Сидоров'
autos['AК5666AL'] = 'Сидір  Сидоров'
autos['AК5666AA'] = 'Сидір  Сидоров'

carOwner = autos.get('BO1234BO')
# print(carOwner)

owners = {}

for own in autos.values():
    if own in owners:
        owners[own] += 1
    else:
        owners[own] = 1

# print(owners)

# for name, count in owners.items():
#     if count > 1:
#         print(f'{name} має авто: {count}')


# Створіть словник “stock”, який міститиме в собі (ключ — назва товару. Значення — кількість товару на складі). 
# Написати програму, яка запитує який товар та кількість, яку хоче купити користувач. 

stock = {
    "apple": 10,
    "banana": 5,
    "orange": 7,
    "milk": 20
}

# product = input('Enter name: ')
# quant = int(input('Enter quant: '))

# if product in stock and stock[product] >= quant:
#     print('horosho')


# if product in stock.keys():
#     if stock[product] >= quant:
#         print('HOROSHO')
#     else:
#         print('Nema tovaru')
# else:
#     print('Nema tovaru')


# Створіть словник, який містить дані про користувачів вашого веб-сайту. Ключами в цьому словнику будуть імена користувачів, 
# а значеннями — інформація про користувачів. Попросіть користувача ввести імена користувачів, про яких хоче дізнатися інформацію, 
# через пробіл. Вивести інформацію про цих користувачів у форматі (Ім’я: вік, стать, електронна пошта).

users = {
    'user1': {'age': 25, 'gender': 'male', 'email': 'ololo@example.com'},
    'user2': {'age': 30, 'gender': 'female', 'email': 'oazaza@example.com'}
}

info = input('Enter name or names: ').split()

for name in info:
    if name in users:
        user_info = users[name]
        print(f'{name}: {user_info['age']}, {user_info['gender']}, {user_info['email']}')
    else:
        print('nema takogo')
