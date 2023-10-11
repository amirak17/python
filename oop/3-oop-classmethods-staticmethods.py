
# https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Object-Oriented

class Employee:

    number_of_emps = 0;
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.number_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # decorator
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod 
    def from_string(cls, emp_str): 
        first, last, pay = emp_str.split('-') 
        return cls(first, last, pay) 
    
    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: 
            return False 
        return True    


emp_1 = Employee('Amir', 'Khan', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)

# Employee.set_raise_amt(1.05) # using classmethod
# print(Employee.raise_amount)
# print(emp_1.raise_amount)

emp_str_1 = 'John-Doe-70000' 
emp_str_2 = 'Steve-Smith-30000' 
emp_str_3 = 'Jane-Doe-90000'


# alternative constructor
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)


# static method
import datetime 
my_date = datetime.date(2016, 7, 10) 
print (Employee.is_workday (my_date))
my_date = datetime.date(2016, 7, 11) 
print (Employee.is_workday (my_date))


