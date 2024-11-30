has_pet = True
name = ' John'
height = 1.84
# print(f'dfhuisufhsdui. pet: {has_pet}. {name} dfgdsfgdfgdf {height}')



# class = '34343'
# def if for while

# age = int(input('Enter age: '))

# if age >= 18:
#     print('U R adult')
# else:
#     print('U R not adult')

# num = int(input('Enter num: '))


# if num > 0:
#     print('positive')
# elif num < 0:
#     print('negative')
# else:
#     print('num is 0')



# grade = int(input('Enter ur score: '))

# if grade >= 90:
#     print('A. Super')
# elif grade >= 80:
#     print('B. good')
# elif grade >= 70:
#     print('C. Norm')
# else:
#     print('ne zdav')


# a = '' false 
# b = 3 True
# c = [] False


money = 75

if money:
    print(f'U have {money} hryvnas')
else:
    print('U have no money')



#  and or not

# Визначити, чи введений з клавіатури рік є високосним.
# Примітка: Високосний — це рік, який ділиться на 400 без остачі або рік, який ділиться на 4  без остачі та 100 з остачею

# year = int(input('Enter year: '))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print('visokosnyi')
# else:
#     print('ne visokosnyi')



result = True if 5 > 3 else False
# print(result)

# x = 9

# is_even = 'even' if x % 2 == 0 else 'odd'
# print(is_even)


# x = int(input('X: '))
# y = int(input('Y: '))

# if x == 0:
#     print('X cant be 0')
#     x = int(input('X: '))

#     if x == 0:
#         print('X cant be 0')
#         x = int(input('X: '))

#         if x == 0:
#             print('X cant be 0')
#             x = int(input('X: '))

# res = y / x
# print(res)


x = int(input('X: '))
y = int(input('Y: '))

if x > 0 and y > 0:
    print('1chv')
elif x < 0 and y > 0:
    print('2chv')
elif x < 0 and y < 0:
    print('3chv')
elif x > 0 and y < 0:
    print('4chv')
elif x == 0 and y == 0:
    print('center')
else:
    print('wrong action')