from os import name
from tkinter import scrolledtext
from typing import Self


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score 
bart = Student('Bart Simpson',59)
print(bart.name)
print(bart.score)
def print_score(std):
    print('%s:%s'%(std.name,std.score))
    print_score(bart)
    print('[]:[]',format(std.name,std.score))
    print(f'{std.name}:{std.score}')

class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_salary(self):
        print(f'{self.name}:{self.salary}')
    def get_grade(self):
        if self.salary <1000:
            return'low'
        elif self.salary <2000:
            return'middle'
        else:
            return'high'
emp = Employee('Bob', 2000)
emp.print_salary()
print(emp.get_grade())

# 私有变量
class Student(object):
    def __init__(self, name, score):
        self._name = name
        self.__score = score

        def print_score(self):
            print(f'{self._name}:{self.__score}')
            