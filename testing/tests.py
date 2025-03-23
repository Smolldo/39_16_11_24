# def add(x,y):
#     return x + y

# assert add(2,3) == 5, 'Test failed must be 5'
# assert add(-1, 1) == 0, 'Test failed must be 0'

# print('all tests passed')


# def mult(a, b):
#     return a * b

# def test_mult():
#     assert mult(3,4) == 12, 'Test failed'

# test_mult()
# print('All tests are passed')


def authentificate(username, password):
    return username == 'admin' and password == '1234'

def dashboard(user_authentificated):
    if user_authentificated:
        return 'welcome to dashboard'
    else:
        return 'access denied'
    

def integrate():
    user_authentificated = authentificate('admin', '1234')
    result = dashboard(user_authentificated)
    assert result == 'welcome to dashboard', 'Test failed'


    user_authentificated = authentificate('user', '43534')
    result = dashboard(user_authentificated)
    assert result == 'access denied', 'test failed. must deny this auth'

integrate()
print('all tests passed')
    


import unittest


def add(x,y):
    return x + y

def substruct(x, y):
    return x - y

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(3,4), 7)

    def test_substract(self):
        self.assertEqual(substruct(10, 5), 5)
        self.assertEqual(substruct(1, 5), -4)

    def substract_raises(self):
        with self.assertRaises(TypeError):
            substruct('10', 5)





class TestExample(unittest.TestCase):

    def setUp(self):
        self.data = [1,2,3,4,5]

    def tearDown(self):
        self.data = None

    def test_sum(self):
        reusult = sum(self.data)
        self.assertEqual(reusult, 15)

    def test_contains(self):
        self.assertIn(3, self.data)



def reverse_string(s):
    return s[::-1]

class TestString(unittest.TestCase):
    def test_simple_reveverse(self):
        self.assertEqual(reverse_string('Hell'), 'olleH')

    def test_empty_string(self):
        self.assertEqual(reverse_string(''), '')

    def test_palindrome(self):
        self.assertEqual(reverse_string('madm'), 'madam')


# Створіть тестові випадки для функції, яка обчислює факторіал числа.


if __name__ == '__main__':
    unittest.main()
