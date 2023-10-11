
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Object-Oriented

class Employee:

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Amir', 'Khan', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

emp_1.first = 'Amir'
emp_1.last = 'Khan'
emp_1.email = 'amir.khan@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@company.com'
emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))

# both same
print(emp_1.fullname())
print(Employee.fullname(emp_1))

