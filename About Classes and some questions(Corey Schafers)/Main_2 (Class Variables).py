# Python Object-Oriented Programming

class Employee:
    num_of_empys = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_empys += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_empys)
#
emp_1= Employee('Akshay','Sharma', 50000)
emp_2= Employee('Test','User', 60000)


# emp_1.raise_amount = 1.05
# emp_2.raise_amount = 1.06

# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
print(Employee.num_of_empys)