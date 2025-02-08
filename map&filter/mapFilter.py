# map(action, iterable)

numbers = [2, 3, 4, 5, 6, 7]

squared = map(lambda x: x ** 2, numbers)

# print(list(squared))


# def square(number):
#     return number ** 2
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)  



words = ['apple', 'banana', 'steam']

# words = 'Lorem ipsum'

upped = list(map(lambda x: x.upper(), words))

# print(upped)


# filter(function, iterable)

def is_even(number):
    return number % 2 == 0

x = [1,2,3,4,5,6,7,8,9]

even_nums = list(filter(is_even, x))
# print(even_nums)


words = ['text', '', 'ball', ' ', 'cyberpunk']

no_empty = list(filter(lambda x: x.strip(), words))

# print(no_empty)


names = ['JaMes', ' LiLLY', ' john ', 'JaMes']

norm = list(set(map(lambda x: x.strip().capitalize(), names)))

# print(norm)



w = ['Anna', '()()', 'atAtA']

# word == word[::-1]

palindroms = filter( lambda x: x == x[::-1]   ,list(map(lambda x: x.lower().replace(' ', ''), w,words)))

print(list(palindroms))