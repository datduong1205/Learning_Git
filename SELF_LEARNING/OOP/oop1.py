
import datetime

class Employee:

    NumOfEmp = 0
    RaiseAmount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.NumOfEmp += 1

    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last) 

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * self.RaiseAmount)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    @classmethod
    def SetRaiseAmount(cls, amount):
        cls.RaiseAmount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)        

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)        

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    RaiseAmount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    RaiseAmount = 1.20

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



emp1 = Employee('Corey', 'Shafer', 50000)
emp2 = Employee('Test', 'Employee', 60000)

dev1 = Developer('Tran', 'Tao', 50000, 'Python')
dev2 = Developer('Louis', 'Duong', 60000, 'Java')

mgr_1 = Manager("Sue", "Smith", 90000, [dev1])

print(int.__add__(1, 2))
print(str.__add__("a", "b"))

del emp1.fullname