# try:
#     number = int(input('Enter some num: '))
#     print(f'vi vvely chislo: {number}')
# except ValueError:
#     print('Error you type not a number')


# try:
#     file = open('recept.txt', 'r')
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print('Flie not found')


# try:
#     val = int(input('Enter num: '))
#     res = 100 / val
#     print(res)
# except ValueError:
#     print('not a num')
# except ZeroDivisionError:
#     print('cant divide by zero')

# try:
#     res = 10 + 'a'
# except TypeError:
#     print('str + int = nonono')

# try:
#     numbers = [1, 2, 3]
#     print(numbers[5])
# except IndexError:
#     print("Помилка: індекс виходить за межі списку!")

# try:
#     data = {"name": "Alice", "age": 25}
#     print(data["address"])
# except KeyError:
#     print("Помилка: ключ 'address' не знайдено в словнику!")
# file = None

# try:
#     file = open("example.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Помилка: файл не знайдено!")
# finally:
#     if file is not None:
#         file.close()
#     print("Файл було закрито.")

# try:
#     a = int(input("Введіть чисельник: "))  
#     b = int(input("Введіть знаменник: ")) 
#     result = a / b  
#     print(f"Результат: {result}")
# except ZeroDivisionError:
#     print("Помилка: не можна ділити на нуль!") 
# except ValueError:
#     print("Помилка: введіть число, а не текст!") 
# finally:
#     print("Операція завершена.")


# def divid(a, b):
#     if b == 0:
#         raise ZeroDivisionError('sproba dility na 0')
#     return a / b

# try:
#     res = divid(10, 0)
# except ZeroDivisionError as e:
#     print(e)


# def read_file(name):
#     try:
#         file = open(name, 'r')
#         cont = file.read()
#         print(cont)
#     except FileNotFoundError:
#         print('file not found')
#     finally:
#         try:
#             file.close()
#             print('file closed')
#         except NameError:
#             print('file not found')

# read_file('nnn.txt')
# read_file('exceptions/example.txt')


# def get_val(lst, index):
#     try:
#         elem = lst[index]
#         print(f'element = {elem}')
#     except IndexError:
#         print('out of range')

# get_val([1,2,3], 5)
# get_val([1,2,3,4,5,6], 2)


# def div():
#     a = int(input('E a: '))
#     b = int(input('E b: '))
#     try:
#         r = a / b
#         print(r)
#     except ValueError:
#         print('must be a num')
#     except ZeroDivisionError:
#         print('divide by zero')


class PasswordToShortError(Exception):
    pass


def check_pass(password):
    if len(password) < 8:
        raise PasswordToShortError('pass < 8 symbs')
    print('pass = ok')


try:
    passw = input('enter: ')
    check_pass(passw)
except PasswordToShortError as e:
    print(e)
finally:
    print('password checked')
