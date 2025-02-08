import random

import sys

sys.path.append('/ufs/guido/lib/python')

import exampl as e

# from exampl import add

print(e.add(2,3))


# __name__ = '__main__'



if __name__ == '__main__':
    print('u imported hello')
    e.say_hello('user')



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)


plt.plot(x, x, label = 'linear')
plt.plot(x, x**2, label= 'quadratic')
plt.plot(x, x**3, label = 'qubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()

# plt.show()


# Створити власний модуль my_module.py, який містить функцію print_message(msg), 
# що приймає один аргумент msg та виводить його на екран. Потім імпортувати 
# функцію print_message() в головний файл програми та викликати її.

from my_module import print_msg, circle_area, rectangle_area

print_msg('Hello world')


# Створити власний модуль my_geometry.py, який містить 
# функції circle_area(radius) та rectangle_area(width, height). 
# Імпортувати модуль та використати ці функції для обчислення площі 
# кола та прямокутника.

print(circle_area(3))
print(rectangle_area(4,7))

