try:
    with open('exceptions/example.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print('file not found')
except IOError:
    print('problem with access')
else:
    print('File readed')
finally:
    print('mission complete')


# Припустимо, що ми запитуємо у користувача введення числа і хочемо перевірити, чи це дійсно число. 
# Якщо введення успішне, ми можемо виконати подальші обчислення в блоці else.

# try:
#     number = int(input('Enter num: '))
# except ValueError:
#     print('not a number')
# else:
#     result = number * 2
#     print(f'{number} * 2 = {result}')
# finally:
#     print('done')



# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else:
#     print('done')

# class MyFirstException(Exception):
#     def __init__(self, message = 'we have error here'):
#         self.message = message
#         super().__init__(self.message)

# try:
#     raise MyFirstException('smthng gone wrong')
# except MyFirstException as e:
#     print(f'own exception: {e}')



def divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError as e:
        print(f'cant divide by zero: {e}')
        return None
    return res

def proc_div(a,b):
    try:
        res = a/b
        if res is not None:
            print(res)
    except Exception as e:
        print(e)

# print(divide(5,0))
# proc_div(9,'sdfsd')


def reader(filename):
    try:
        with open(filename, 'r') as f:
            try:
                content = f.read()
                print(content)
            except IOError as e:
                print(f'Error: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'unknown error: {e}')

# reader('exceptions/example.txt')


import logging

# logging.basicConfig(level=logging.ERROR, filename='exceptions/app.log', filemode= 'a', format= '%(asctime)s - %(levelname)s - %(message)s')

# def division(a, b):
#     try:
#         return a / b
#     except Exception as e:
#         logging.error(f'Error catched: {e}', exc_info=True)

# print(division(10, 3))


logging.basicConfig(level=logging.WARNING, format= '%(asctime)s - %(message)s')

class CustomError(Exception):
    pass

def proc_data(data):
    try:
        if not isinstance(data, list):
            raise CustomError('wrong data type')
        
        res = sum(data)
        return res
    except CustomError as e:
        logging.warning(f'data process error: {e}')
    except Exception as e:
        logging.error(f'unknown error: {e}')


print(proc_data('sdsd'))
