def test(*nums, **peoples):
    for i in nums:
        print(i)

    for keys, vals in peoples.items():
        print(f'{keys}: {vals}')


# test(1,2,3,4,5,6,7,8,9, John = 'apple', Carl = 'grape')


# Написати функцію, яка приймає рядок і повертає кількість голосних букв у цьому рядку.
# text = input('Enter smth: ')

# def count_vowels(string):
#     vowels = 'aieouyAIEOUY'
#     count = 0
#     for i in string:
#         if i in vowels:
#             count += 1
#     return count


# print(count_vowels(text))




# Написати функцію, яка приймає два числа та повертає їх суму.
# def summa(x, y):
#     return x + y

# print(summa(3,4))

# Написати функцію, яка приймає список чисел і повертає найбільше число в цьому списку.

def print_max(spisok):
    return max(spisok)

# print(print_max([1,2,3,4,55555555555,6,7,8,9]))


# Написати функцію, яка приймає список і повертає список, який містить тільки унікальні елементи вихідного списку.
def uniq(spisok):
    # return  list(set(spisok))
    arr = []
    for i in spisok:
        if i in arr:
            continue
        else:
            arr.append(i)
    return arr


# print(uniq([1,1,1,2,3,4,4,4,4,5,5,6,7,7,7,]))

# Написати функцію, яка приймає список і повертає список, який складається з елементів вхідного списку у зворотному порядку.

def revers(spisok):
    return spisok[::-1]
    # return list(reversed(spisok))

# print(revers([1,2,3,4,5]))


# Написати функцію, яка приймає рядок та повертає True, якщо цей рядок є паліндромом, та False у протилежному випадку.

def palindrom(txt):
    replaced = str(txt).replace(' ', '').lower()
    if replaced == replaced[::-1]:
        print(True)
    else:
        print(False)

# palindrom('Taco cat')


# Написати функцію, яка приймає число та повертає його факторіал.
def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

print(factorial(25))