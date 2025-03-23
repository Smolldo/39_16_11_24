class GoITeens_Student:
    def __init__(self, name, year, grade, current_lesson):
        self.name = name
        self.year = year
        self.grade = grade
        self.current_lesson = current_lesson

    def student_info(self):
        print(f'Студент {self.name} народився у {self.year} році, навчається у: {self.grade} класі, зараз проходить: {self.current_lesson} урок')


stud = GoITeens_Student('John', 1999, 11, '38 OOP')

# stud.student_info()


class Emplyee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def _calculate_bonus(self):
        return self._salary * .1
    
    def get_salary_with_bonus(self):
        return self._salary + self._calculate_bonus()
    
class Manager(Emplyee):
    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = departament

    def display_info(self):
        return f'Manager {self.name}. Departament: {self.departament}. Salary with bonus: {self.get_salary_with_bonus()}'
    

# worker = Emplyee('John', 5000)
# print(f'salary with bonus: {worker.get_salary_with_bonus()}')
        
# worker1 = Manager('Jane', 6000, 'Marketing')
# print(worker1.display_info())



class BankAccount:
    def __init__(self, holder, balance, pin_code ):
        self.holder = holder
        self._balance = balance
        self.__pin_code = pin_code


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if self._check_sufficient_balance(amount):
            self._balance -= amount
        return self._balance
    
    def _check_sufficient_balance(self, amount):
        return self._balance >= amount
    
    def __update_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin_code = new_pin
        else:
            raise ValueError('PIN must be a 4 digit number')
    
acc = BankAccount('Alex', 7000, '1242')
print(acc.holder)

new_balance = acc.deposit(5000)
print(f'new balance = {new_balance}')

new_balance = acc.withdraw(7000)
print(f' new balance = {new_balance}')

new_balance = acc.withdraw(10000)
print(f'{new_balance}')

# acc._BankAccount__update_pin('6789')
# print(f'password changed to')




class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError('Age cant be negative')
        
person = Person('Jack', 50)
print(person.get_age())

person.set_age(40)
print(person.get_age())

person.set_age(-5)
print(person.get_age())
        


        
        