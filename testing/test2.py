import unittest
import pytest
import pdb

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError('y != 0 !!!!!!')
    return x / y

class TestDivision(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'file not found'
    
class TestFileRead(unittest.TestCase):

    def test_existing_read(self):
        content = read_file('transactions.txt')
        self.assertIsInstance(content, str)

    def test_non_existing_read(self):
        content = read_file('goiteens.txt')
        self.assertIsInstance(content, 'file not found')


def is_even(number):
    return number % 2 == 0

@pytest.mark.parametrize('number expected',[
    (2, True),
    (3, False),
    (4, True),
    (5, False)
])

def test_is_even(number, expected):
    assert is_even(number) == expected

if __name__ == '__main__':
    unittest.main()


@pytest.fixture
def sample_data():
    return {'name': 'John', 'age': 30}

def test_sample_data(sample_data):
    assert sample_data['name'] == 'John'
    assert sample_data['age'] == 30


def divide(x,y):
    pdb.set_trace()
    return x / y


res = divide(10, 2)
print(res)


def average(nums):
    pdb.set_trace()
    total = sum(nums)
    count = len(nums)

    return total / count

numbers = [11,23,45,67]
result = average(numbers)
print(f'suma = {result}')